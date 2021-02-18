from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_turtles = []

is_race_on = False
user_bet = screen.textinput(title="Make your bet 🧚", prompt="Which turtle will win the race? \nEnter a rainbow color")


y_position = -100.0
for turtle_index in range(6):
    y_position += 30.0
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 215:
            is_race_on = False
            if user_bet.lower() == turtle.pencolor():
                screen.title(f"You win ! The {turtle.pencolor()} turtle won the race! 🧚")
            else:
                screen.title(f"You lose. The {turtle.pencolor()} turtle won the race.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
