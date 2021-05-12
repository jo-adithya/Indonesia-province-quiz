import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=1240, height=616)
screen.title('Indonesian Provinces Quiz')

# Choose level of difficulty
while True:
    difficulty = screen.textinput(title='Difficulty Level',
                                  prompt='Choose the level of difficulty, easy or hard?').lower()
    if difficulty not in ['easy', 'hard']:
        continue
    image_path = 'Indonesian Map (' + difficulty + ').gif'
    screen.addshape(image_path)
    turtle.shape(image_path)
    break

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed('fastest')
df = pd.read_csv('Indonesian_province.csv')
provinces = [' '.join(x.lower().split()) for x in df['province']]
score = 0

while score < 34:
    guess = screen.textinput(title=f'{score}/34 Provinces Correct', prompt='Province name in Indonesia:').lower()
    if guess in provinces:
        prov_data = df.iloc[provinces.index(guess)]
        tim.goto(prov_data['x'], prov_data['y'])
        tim.color(prov_data['color'])
        tim.write(prov_data['province'], align='right', font=('Arial', 14, 'bold'))
        score += 1

turtle.mainloop()
