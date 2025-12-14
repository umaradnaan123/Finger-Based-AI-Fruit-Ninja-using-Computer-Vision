import cv2
import mediapipe as mp

class BladeTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        self.prev_point = None

    def get_blade_points(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if not result.multi_hand_landmarks:
            self.prev_point = None
            return None, None

        hand = result.multi_hand_landmarks[0]

        # Index finger tip (knife point)
        lm = hand.landmark[8]

        h, w, _ = frame.shape
        curr_point = (int(lm.x * w), int(lm.y * h))

        prev = self.prev_point
        self.prev_point = curr_point

        return prev, curr_point
