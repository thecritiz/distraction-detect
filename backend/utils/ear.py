import numpy as np

# Left and right eye indices from MediaPipe
LEFT_EYE_IDX = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]

def calculate_ear(landmarks):
    def _get_coords(indices):
        return [(landmarks.landmark[i].x, landmarks.landmark[i].y) for i in indices]

    def _distance(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    left_eye = _get_coords(LEFT_EYE_IDX)
    right_eye = _get_coords(RIGHT_EYE_IDX)

    def _ear(eye):
        A = _distance(eye[1], eye[5])
        B = _distance(eye[2], eye[4])
        C = _distance(eye[0], eye[3])
        return (A + B) / (2.0 * C)

    left_ear = _ear(left_eye)
    right_ear = _ear(right_eye)

    return (left_ear + right_ear) / 2
