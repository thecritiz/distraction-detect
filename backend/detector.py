import cv2
import mediapipe as mp
from utils.head_pose import estimate_head_pose  # ✅ Use relative import

mp_face_mesh = mp.solutions.face_mesh

# Reuse the FaceMesh model across frames
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    refine_landmarks=True,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Eye landmark indices (MediaPipe)
LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]

def calculate_ear(landmarks):
    def eye_aspect_ratio(eye):
        A = ((eye[1][0] - eye[5][0]) ** 2 + (eye[1][1] - eye[5][1]) ** 2) ** 0.5
        B = ((eye[2][0] - eye[4][0]) ** 2 + (eye[2][1] - eye[4][1]) ** 2) ** 0.5
        C = ((eye[0][0] - eye[3][0]) ** 2 + (eye[0][1] - eye[3][1]) ** 2) ** 0.5
        return (A + B) / (2.0 * C)

    left_eye = [landmarks[i] for i in LEFT_EYE_IDX]
    right_eye = [landmarks[i] for i in RIGHT_EYE_IDX]

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    return (left_ear + right_ear) / 2.0

def analyze_frame(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]
        h, w, _ = frame.shape
        landmarks = [(int(p.x * w), int(p.y * h)) for p in face.landmark]

        ear = calculate_ear(landmarks)
        yaw = estimate_head_pose(landmarks, frame.shape)

        if ear < 0.20 or abs(yaw) > 20:
            return "distracted"
        return "attentive"
    return "no_face"
