# 🔪 VisionBlade — AI Fruit Ninja Using Computer Vision

VisionBlade is a real-time **AI-powered Fruit Ninja game** built using **OpenCV and MediaPipe**.
The player’s **index finger acts as a virtual knife**, allowing fruits to be sliced in mid-air using a webcam — no controller, no pen required.

---

## 🎮 Features

* 🖐️ Finger-based slicing (index finger = knife)
* 🎥 Real-time webcam interaction
* 🍎 Dynamic fruit spawning
* 💣 Bomb detection (game over logic)
* ⚡ Motion-based slicing using finger trajectory
* 📈 Score & FPS counter
* 🧠 AI-powered hand landmark detection
* 💻 Runs on CPU (no GPU required)

---

## 🧠 How It Works

* Uses **MediaPipe Hands** to detect hand landmarks
* Tracks the **index finger tip**
* Converts finger movement into a slicing line
* Detects intersections between the slicing line and fruits
* Removes fruits and updates score in real time

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **OpenCV**
* **MediaPipe Hands**
* **NumPy**
* **Pygame**

---

## 📁 Project Structure

```text
VisionBlade/
│
├── main.py              # Main game loop
├── blade_tracker.py     # Finger (knife) tracking logic
├── fruit.py             # Fruit physics and rendering
├── game_utils.py        # Collision detection utilities
├── requirements.txt     # Dependencies
├── README.md
└── assets/
    ├── apple.png
    └── bomb.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/umaradnaan123/Finger-Based-AI-Fruit-Ninja-using-Computer-Vision.git
cd VisionBlade
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Game

```bash
python main.py
```

---

## 🕹️ Controls

* ✋ Move **index finger** to slice fruits
* 💣 Avoid bombs
* ⎋ `ESC` → Quit the game
---

## 🚀 Future Enhancements

* Multi-hand support
* Combo scoring system
* Sound effects & animations
* YOLO-based object detection
* Mobile or Web version

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* OpenCV
* Google MediaPipe
* Fruit Ninja (inspiration)
