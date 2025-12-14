import random
import cv2
import numpy as np

class Fruit:
    def __init__(self, img, screen_width, is_bomb=False):
        self.img = img
        self.h, self.w = img.shape[:2]
        self.x = random.randint(0, max(1, screen_width - self.w))
        self.y = -self.h
        self.speed = random.randint(6, 12)
        self.is_bomb = is_bomb

    def move(self):
        self.y += self.speed

    def draw(self, frame):
        fh, fw, _ = frame.shape

        # Calculate visible region on frame
        x1 = max(self.x, 0)
        y1 = max(self.y, 0)
        x2 = min(self.x + self.w, fw)
        y2 = min(self.y + self.h, fh)

        # Completely outside screen
        if x1 >= x2 or y1 >= y2:
            return

        # Corresponding region on fruit image
        fx1 = x1 - self.x
        fy1 = y1 - self.y
        fx2 = fx1 + (x2 - x1)
        fy2 = fy1 + (y2 - y1)

        fruit_part = self.img[fy1:fy2, fx1:fx2]

        # ----- HANDLE PNG ALPHA CHANNEL -----
        if fruit_part.shape[2] == 4:
            alpha = fruit_part[:, :, 3] / 255.0
            for c in range(3):
                frame[y1:y2, x1:x2, c] = (
                    alpha * fruit_part[:, :, c] +
                    (1 - alpha) * frame[y1:y2, x1:x2, c]
                )
        else:
            frame[y1:y2, x1:x2] = fruit_part[:, :, :3]

    def rect(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)
