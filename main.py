import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # can be image shape.
turtle.shape(image)
writer_turtle = turtle.Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()

states_data = pandas.read_csv("50_states.csv")
states_names_list = states_data["state"].to_list()  # converting a Series to a List.
correct_guess = []
while len(correct_guess) < 51:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name.").title()
    if answer_state == "Exit":
        learn_states = [name for name in states_names_list if name not in correct_guess]
        learn_states_file = pandas.DataFrame(learn_states)
        learn_states_file.to_csv("learn_states.csv")
        break
    if answer_state in states_names_list:
        state_data = states_data[states_data["state"] == answer_state]  # If state matches answer_state then get
        # particular state's row. #state_data.state.item() will fetch the specific data with out other information.
        writer_turtle.goto(float(state_data.x), float(state_data.y))
        writer_turtle.write(f"{answer_state}", False, align="center", font=("Arial", 8, "normal"))
        if answer_state not in correct_guess:
            correct_guess.append(answer_state)

