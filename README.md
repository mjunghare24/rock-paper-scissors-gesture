# 🤖 Rock-Paper-Scissors Using Hand Gestures

This is a real-time **Rock-Paper-Scissors game** that uses your **hand gestures** detected via webcam, built using **OpenCV** and **MediaPipe**. Play against the computer using just your hand—no keyboard or mouse required!

## ✨ Features

- 👋 Hand gesture recognition using MediaPipe
- 🧠 Real-time game logic and computer choice generation
- 🎮 Interactive UI using OpenCV to display game results
- ⏱️ Fast and responsive gesture-based gameplay

## 📽️ How It Works

1. The webcam captures your hand.
2. MediaPipe analyzes your gesture (rock, paper, or scissors).
3. The computer makes a random choice.
4. The result is displayed instantly on screen!

## 🖥️ Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

Install dependencies using:
```bash
pip install -r requirements.txt
▶️ Running the Game
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/rock-paper-scissors-gesture.git
Navigate to the folder:

bash
Copy
Edit
cd rock-paper-scissors-gesture
Run the game:

bash
Copy
Edit
python main.py
Show one of these gestures in front of the webcam:

✊ Rock

✋ Paper

✌️ Scissors

📂 Project Structure
bash
Copy
Edit
rock-paper-scissors-gesture/
├── main.py               # Main game logic
├── hand_tracking_module.py  # (If modularized)
├── README.md
├── requirements.txt
💡 Future Improvements
Add GUI using Tkinter or PyQt

Gesture calibration step

Sound effects or background music

Multiplayer over network

🙌 Acknowledgements
MediaPipe by Google

OpenCV Library
