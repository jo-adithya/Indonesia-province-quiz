import turtle

screen = turtle.Screen()
screen.setup(width=1240, height=616)
screen.title('Indonesian Provinces Quiz')
image_path = 'Indonesian Map (easy).gif'
screen.addshape(image_path)

turtle.shape(image_path)


def get_mouse_click(x, y):
    print(f'({x}, {y})\n')


# Get the mouseclick coordinates relative to the image
turtle.onscreenclick(get_mouse_click)
turtle.mainloop()

