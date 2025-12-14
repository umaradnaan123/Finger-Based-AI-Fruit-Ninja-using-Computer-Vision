import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

class SwordTracker:
    def __init__(self):
        self.prev_point = None

    def get_points(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            lm = result.multi_hand_landmarks[0].landmark[8]
            h, w, _ = frame.shape
            point = (int(lm.x * w), int(lm.y * h))
            prev = self.prev_point
            self.prev_point = point
            return prev, point

        self.prev_point = None
        return None, None
