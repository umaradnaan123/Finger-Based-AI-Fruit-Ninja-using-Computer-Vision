import cv2
import os
import random
import time
from blade_tracker import BladeTracker
from fruit import Fruit
from game_utils import line_intersects_rect

# ------------------ CAMERA SETUP ------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    # Render / cloud mode: No webcam available
    print("Camera not available. Running in Render mode (simulation).")
    # Keep process alive
    while True:
        time.sleep(60)

# Local mode: continue normal game
tracker = BladeTracker()

BASE = os.path.dirname(os.path.abspath(__file__))

def load_image(name, size=(60, 60)):
    path = os.path.join(BASE, "assets", name)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"❌ Missing asset: {name}")
    return cv2.resize(img, size)

apple = load_image("apple.png")
bomb = load_image("bomb.png")

# ------------------ GAME STATE ------------------
fruits = []
score = 0
game_over = False
paused = False
spawn_rate = 20

prev_time = time.time()

# ------------------ MAIN LOOP ------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from camera. Exiting.")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # ------------------ BLADE TRACKING ------------------
    prev, curr = tracker.get_blade_points(frame)

    if prev and curr:
        cv2.line(frame, prev, curr, (0, 0, 255), 4, cv2.LINE_AA)

    # ------------------ SPAWN FRUITS ------------------
    if not game_over and not paused:
        if random.randint(1, spawn_rate) == 1:
            is_bomb = random.random() < 0.18
            fruits.append(Fruit(bomb if is_bomb else apple, w, is_bomb))

    # ------------------ UPDATE FRUITS ------------------
    for fruit in fruits[:]:
        if not paused:
            fruit.move()

        fruit.draw(frame)

        if not paused and line_intersects_rect(prev, curr, fruit.rect()):
            fruits.remove(fruit)
            if fruit.is_bomb:
                game_over = True
            else:
                score += 10
        elif fruit.y > h:
            fruits.remove(fruit)

    # ------------------ DIFFICULTY SCALING ------------------
    spawn_rate = max(6, 20 - score // 40)

    # ------------------ FPS CALCULATION ------------------
    now = time.time()
    delta = now - prev_time
    fps = int(1 / delta) if delta > 0 else 0
    prev_time = now

    # ------------------ UI ------------------
    cv2.putText(frame, f"Score: {score}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.putText(frame, f"FPS: {fps}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.putText(frame, "P = Pause | R = Restart | ESC = Quit",
                (20, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    if paused:
        cv2.putText(frame, "PAUSED",
                    (w // 2 - 100, h // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)

    if game_over:
        cv2.putText(frame, "GAME OVER",
                    (w // 2 - 200, h // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 5)
        cv2.putText(frame, "Press R to Restart",
                    (w // 2 - 170, h // 2 + 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("VisionBlade v3.3 — Finger Knife AI Fruit Ninja", frame)

    # ------------------ CONTROLS ------------------
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break
    elif key == ord('p'):
        paused = not paused
    elif key == ord('r'):
        fruits.clear()
        score = 0
        game_over = False
        paused = False

# ------------------ CLEANUP ------------------
cap.release()
cv2.destroyAllWindows()
