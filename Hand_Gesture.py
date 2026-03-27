import cv2
import mediapipe as mp
import serial
import time
print("🚀 Program started")
# 🔌 Arduino Connection (CHANGE COM PORT)
try:
    arduino = serial.Serial('COM4', 9600)
    time.sleep(2)
    print("✅ Arduino connected")
except Exception as e:
    print("❌ Arduino error:", e)
    arduino = None

# 🧠 MediaPipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# 🎥 Camera Setup
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not working")
    exit()

print("✅ System Started")
print("Show 👍 for ON | ✋ for OFF | Press ESC to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to capture frame")
        break

    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = "No Hand"

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Landmark positions
            thumb_tip = handLms.landmark[4]
            index_tip = handLms.landmark[8]

            # 🎯 Gesture Logic
            if thumb_tip.y < index_tip.y:
                gesture = "ON"
                arduino.write(b'1')
            else:
                gesture = "OFF"
                arduino.write(b'0')

    # Display Gesture
    cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show Camera
    cv2.imshow("Hand Gesture Control", frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()