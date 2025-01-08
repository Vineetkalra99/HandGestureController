import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture webcam feed
cap = cv2.VideoCapture(0)

# Screen size for mapping hand movements
screen_width, screen_height = pyautogui.size()

# Define a flag for "holding" state
holding = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get coordinates of the index finger tip and thumb tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert normalized coordinates to pixel values
            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Move the cursor based on index finger position
            cursor_x = int(index_finger_tip.x * screen_width)
            cursor_y = int(index_finger_tip.y * screen_height)
            pyautogui.moveTo(cursor_x, cursor_y)

            # Check if index finger and thumb are close (distance threshold for "pick up")
            distance = np.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)
            if distance < 40:  # Threshold for "picking up"
                if not holding:
                    pyautogui.mouseDown()
                    holding = True
            else:
                if holding:
                    pyautogui.mouseUp()
                    holding = False

    # Display the frame
    cv2.imshow('Hand Gesture App Controller', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()