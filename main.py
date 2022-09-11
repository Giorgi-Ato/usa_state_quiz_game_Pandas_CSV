from turtle import Turtle, Screen
import pandas as pd
from name_model import NameTurtle

screen = Screen()
screen.title('U.S. Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

state_data = pd.read_csv('50_states.csv')
states = list(state_data.state)
right_guesses_states = []


score = 0
while score < 50:

    user_answer = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()

    if user_answer == "Exit":
        missing_states = [state for state in states if state not in right_guesses_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_lear.csv')
        break

    if user_answer in states and user_answer not in right_guesses_states:
        score += 1
        right_guesses_states.append(user_answer)

        x_cor = int(state_data[state_data.state == user_answer].x)
        y_cor = int(state_data[state_data.state == user_answer].y)
        txt = NameTurtle(user_answer, x_cor, y_cor)
