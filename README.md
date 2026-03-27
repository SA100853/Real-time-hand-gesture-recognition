# Real-time-hand-gesture-recognition
This project uses computer vision and hand gesture recognition to control an Arduino device (like an LED) in real-time.
# ✋ Hand Gesture Control System using Arduino

This project uses **computer vision and hand gesture recognition** to control an Arduino device (like an LED) in real-time.

---

## 🚀 Features

* Real-time hand tracking using webcam
* Gesture recognition using MediaPipe
* Arduino control via serial communication
* Touchless ON/OFF system

---

## 🧠 Tech Stack

* Python
* OpenCV
* MediaPipe
* PySerial
* Arduino

---

## 📂 Project Structure

```id="tree1"
├── Hand_Gesture.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```id="clone1"
git clone https://github.com/your-username/hand-gesture-arduino.git
cd hand-gesture-arduino
```

### 2️⃣ Install Dependencies

```id="install1"
pip install -r requirements.txt
```

### 3️⃣ Connect Arduino

* Connect Arduino via USB
* Update COM port in code:

```python id="com1"
arduino = serial.Serial('COM4', 9600)
```

---

## ▶️ Run the Project

```id="run1"
python Hand_Gesture.py
```

---

## 🎮 Gesture Controls

* 👍 Thumb Up → LED ON
* ✋ Open Hand → LED OFF

---

## 🔌 Arduino Logic

* Receives `'1'` → LED ON
* Receives `'0'` → LED OFF

---

## 📸 How It Works

1. Webcam captures hand
2. MediaPipe detects landmarks
3. Gesture is recognized based on thumb & finger position
4. Signal sent to Arduino

---

## 🏆 Applications

* Touchless control systems
* Smart home automation
* Assistive technology

---

## 👨‍💻 Author

**Sarfaraj Alam**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
