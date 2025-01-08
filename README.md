# Hand Gesture Controller 👐💻

This Python project lets you control your computer using hand gestures in real-time! Using a webcam and a few powerful Python libraries, you can move the mouse cursor, pick up, and drop windows with simple hand movements. 🎮

## Features 🌟

- **Real-time hand tracking** using OpenCV and MediaPipe. 🎥
- **Mouse control via hand gestures**:
  - 🖱️ Move the cursor by moving your hand.
  - ✋ Pick up (mouse down) by pinching your thumb and index finger.
  - 👆 Drop (mouse up) by releasing the pinch gesture.

## Tech Stack 🛠️

- **Python** 🐍
- **OpenCV**: For capturing and processing video frames. 📸
- **MediaPipe**: For accurate hand landmark detection. ✋
- **PyAutoGUI**: For simulating mouse movements and actions. 🖱️
- **NumPy**: For numerical operations. 🔢

## Installation ⚙️

1. Clone the repository:

    ```bash
    git clone https://github.com/vineetkalra99/HandGestureController.git
    cd HandGestureController
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the program:

    ```bash
    python gesture_control.py
    ```

## How It Works 🤔

- The program accesses your webcam and captures video frames. 📹
- MediaPipe detects the hand landmarks (fingertips, joints) in each frame. 👋
- The program tracks the index finger and thumb to detect gestures:
  - **Pinch gesture**: Simulates a mouse click-and-drag (pick up). 🤲
  - **Release gesture**: Simulates a mouse drop. 🖱️
- **PyAutoGUI** moves the mouse cursor and performs actions based on these gestures. 👆

## Usage Instructions 📋

1. Move your hand in front of the webcam to control the cursor. 👋
2. Pinch your thumb and index finger to pick up. ✋
3. Release the pinch to drop. 🤚
4. Press 'q' to quit the program. ❌

## License 📄

This project is licensed under the MIT License. 🎉

Feel free to contribute by opening issues or submitting pull requests. If you like this project, don’t forget to star the repository! 🌟

## Author ✍️

Vineet Kalra
