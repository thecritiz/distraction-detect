import cv2
import mediapipe as mp
import numpy as np

class AttentivenessChecker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.LEFT_EYE_IDX = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]

    def _eye_aspect_ratio(self, landmarks, eye_indices):
        def get_point(i):
            return np.array([landmarks[i].x, landmarks[i].y])

        p2 = get_point(eye_indices[1])
        p3 = get_point(eye_indices[2])
        p4 = get_point(eye_indices[5])
        p5 = get_point(eye_indices[4])
        p1 = get_point(eye_indices[0])
        p6 = get_point(eye_indices[3])

        vertical1 = np.linalg.norm(p2 - p4)
        vertical2 = np.linalg.norm(p3 - p5)
        horizontal = np.linalg.norm(p1 - p6)
        return (vertical1 + vertical2) / (2.0 * horizontal)

    def detect_attentiveness(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            left_ear = self._eye_aspect_ratio(landmarks, self.LEFT_EYE_IDX)
            right_ear = self._eye_aspect_ratio(landmarks, self.RIGHT_EYE_IDX)
            avg_ear = (left_ear + right_ear) / 2.0

            attentive = avg_ear >= 0.25
            return attentive, avg_ear
        return None, None
