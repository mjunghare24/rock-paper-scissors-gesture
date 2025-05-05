
import cv2
import mediapipe as mp
import random
import time

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Game values
choices = ["Rock", "Paper", "Scissors"]

def get_gesture(hand_landmarks):
    finger_states = []
    tip_ids = [8, 12, 16, 20]  # Index to pinky
    for i in tip_ids:
        finger_tip_y = hand_landmarks.landmark[i].y
        finger_dip_y = hand_landmarks.landmark[i - 2].y
        finger_states.append(finger_tip_y < finger_dip_y)
    if all(x is False for x in finger_states):
        return "Rock"
    elif finger_states[0] and finger_states[1] and not any(finger_states[2:]):
        return "Scissors"
    elif all(x is True for x in finger_states):
        return "Paper"
    return None

# Capture
cap = cv2.VideoCapture(0)
prev_gesture = None
timer_started = False
start_time = 0

print("Show Rock, Paper, or Scissors with your hand!")

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = None

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)
            gesture = get_gesture(handLms)
            if gesture:
                print(f"Detected gesture: {gesture}")

    if gesture and gesture != prev_gesture:
        timer_started = True
        start_time = time.time()
        prev_gesture = gesture

    if timer_started:
        cv2.putText(image, "Hold gesture...", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)
        if time.time() - start_time > 2:
            computer_choice = random.choice(choices)
            result_text = ""
            if gesture == computer_choice:
                result_text = "It's a tie!"
            elif (gesture == "Rock" and computer_choice == "Scissors") or                  (gesture == "Scissors" and computer_choice == "Paper") or                  (gesture == "Paper" and computer_choice == "Rock"):
                result_text = "You win!"
            else:
                result_text = "Computer wins!"

            result_display_time = time.time()
            while time.time() - result_display_time < 3:
                temp_img = image.copy()
                cv2.putText(temp_img, f"You: {gesture}", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                cv2.putText(temp_img, f"Computer: {computer_choice}", (10, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                cv2.putText(temp_img, result_text, (10, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)
                cv2.imshow("Rock Paper Scissors", temp_img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()
            timer_started = False

    cv2.imshow("Rock Paper Scissors", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
