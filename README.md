# 🔪 VisionBlade — AI Fruit Ninja Using Computer Vision

VisionBlade is a real-time **AI-powered Fruit Ninja game** built using **OpenCV and MediaPipe**.  
The player’s **index finger acts as a virtual knife**, allowing fruits to be sliced in mid-air using a webcam — no controller, no pen required.

---

## 🎮 Features

- 🖐️ Finger-based slicing (index finger = knife)
- 🎥 Real-time webcam interaction
- 🍎 Dynamic fruit spawning
- 💣 Bomb detection (game over logic)
- ⚡ Motion-based slicing using finger trajectory
- 📈 Score & FPS counter
- 🧠 AI-powered hand landmark detection
- 💻 Runs on CPU (no GPU required)

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to detect hand landmarks
- Tracks the **index finger tip**
- Converts finger movement into a slicing line
- Detects intersections between the slicing line and fruits
- Removes fruits and updates score in real time

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **OpenCV**
- **MediaPipe Hands**
- **NumPy**
- **Pygame**

---

## 📁 Project Structure

