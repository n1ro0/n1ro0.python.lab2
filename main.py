#ILYA CHABAN
from drawer import draw_option, draw, draw_parser
from textanalyzer import word_frequencies
import turtle



colors = ("red", "green", "purple", "yellow", "blue", "pink", "orange", "violet")

@draw_option("sectors") #Registers draw_sectors as sectors
def draw_sectors(data: dict) -> None:
    """Takes one argument - dict data. Draws sector plot using it."""
    angle_coef = 360 / sum(data.values())
    cur_angle = 0
    i = 0
    l = len(colors)
    for word in data:
        sector_angle = data[word] * angle_coef
        turtle.color(colors[i % l])
        turtle.setheading(cur_angle)
        turtle.begin_fill()
        turtle.fd(100)
        turtle.left(90)
        turtle.circle(100, sector_angle)
        turtle.setheading((cur_angle + 180 + sector_angle) % 360)
        turtle.fd(100)
        turtle.end_fill()
        i += 1
        cur_angle += sector_angle
    i, x, y = 0, 170, 200
    for word in data:
        turtle.color(colors[i % l])
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x+15, y-12)
        turtle.pendown()
        turtle.write("{} - {} time(-s)".format(word, data[word]), move=False, align="left", font=("Arial", 12, "normal"))
        y -= 22
        i += 1
    turtle.hideturtle()

@draw_option("rays") #Registers draw_rays as rays
def draw_rays(data: dict) -> None:
    """Takes 1 argument - dict data. Draws rays plot using it."""
    length_coef = 250 / max(data.values())
    angle_coef = 360 / len(data)
    cur_angle = 0
    i = 0
    l = len(colors)
    for word in data:
        turtle.color(colors[i % l])
        turtle.setheading(cur_angle)
        length = data[word] * length_coef
        turtle.fd(length)
        turtle.up()
        turtle.fd(30)
        turtle.write(word, move=False, align="center", font=("Arial", 12, "normal"))
        turtle.bk(30)
        turtle.pendown()
        turtle.bk(length)
        i += 1
        cur_angle += angle_coef
    turtle.hideturtle()

if __name__ == "__main__":
    output = draw_parser.parse_args()
    draw(word_frequencies(output.text), output.method)
    input()
