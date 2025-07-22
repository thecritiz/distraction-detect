# backend/utils/head_pose.py

import cv2
import numpy as np

def estimate_head_pose(landmarks, shape):
    # Nose tip, chin, eyes, mouth corners
    points = [1, 199, 33, 263, 61, 291]
    image_points = np.array([landmarks[i] for i in points], dtype="double")

    model_points = np.array([
        (0.0, 0.0, 0.0),
        (0.0, -63.6, -12.5),
        (-43.3, 32.7, -26),
        (43.3, 32.7, -26),
        (-28.9, -28.9, -24.1),
        (28.9, -28.9, -24.1)
    ])

    focal_length = shape[1]
    center = (shape[1] / 2, shape[0] / 2)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")

    dist_coeffs = np.zeros((4, 1))
    _, rot_vec, _, _ = cv2.solvePnPRansac(model_points, image_points, camera_matrix, dist_coeffs)
    rot_matrix, _ = cv2.Rodrigues(rot_vec)

    yaw = np.arctan2(rot_matrix[1][0], rot_matrix[0][0]) * 180 / np.pi
    return yaw
