from tkinter import *
from tkinter import ttk

width = 500
height = 300

def f(x):
    return (x*x+9) / (x - 26)

x_begin = -5
x_end = 10


def graphic(frame, dx, smooth=False):
    c = Canvas(frame, width=width, height=height, bg="white")
    c.pack()

    arr = []

    x = x_begin
    while x <= x_end:
        arr.append((x, f(x)))
        x += dx

    x_coords = list(map(lambda point: point[0], arr)) #список для X
    y_coords = list(map(lambda point: point[1], arr)) #список для Y

    mx = width / (max(x_coords) - min(x_coords)) #масштаб
    my = height / (max(y_coords) - min(y_coords))

    my_padding = 50  # px
    my *= (height - my_padding * 2) / height

    mx_padding = 10  # px
    mx *= (width - mx_padding * 2) / width

    dy_pixel = max(y_coords)
    y_pixels = list(map(lambda y: (dy_pixel - y) * my + my_padding, y_coords))

    dx_pixel = min(x_coords)
    x_pixels = list(map(lambda x: (x - dx_pixel) * mx + mx_padding, x_coords))

    pixel_points = [(x_pixels[i], y_pixels[i]) for i in range(len(x_pixels))]

    c.create_line(pixel_points, smooth=smooth) #график

    x0 = (abs(min(x_coords))) / (max(x_coords) - min(x_coords)) * width
    c.create_line([(x0, 0), (x0, height)], arrow=FIRST)
    c.create_text(x0 + 10, 10, text='Y') #ОУ

    y0 = (max(y_coords)+1) / (max(y_coords) - min(y_coords)) * height
    c.create_line([(0, y0), (width, y0)], arrow=LAST)
    c.create_text(width - 5, height - 282, text='X') #ОХ

    if dx == 1:
        x_points_indexes = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        y_points_indexes = [-5, 0, 2, 10, 12, 13,14]
    else:
        x_points_indexes = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500]
        y_points_indexes = [250, 320, 400, 450, 500]

    for i in x_points_indexes:
        c.create_text(x_pixels[i], y0 + 15, text=f'{x_coords[i]:.1f}')
        c.create_line([(x_pixels[i], y0 - 5), (x_pixels[i], y0 + 5)])

    for i in y_points_indexes:
        c.create_text(x0 - 20, y_pixels[i], text=f'{y_coords[i]:.2f}')
        c.create_line([(x0 - 5, y_pixels[i]), (x0 + 5, y_pixels[i])])


root = Tk()
root.resizable(0,0)
root.title('Богданов Максим 19-ИЭ-1')

nb = ttk.Notebook(root)
nb.pack()

f1 = Frame(nb)
nb.add(f1, text="Первый")

f2 = Frame(nb)
nb.add(f2, text="Второй")

f3 = Frame(nb)
nb.add(f3, text="Третий")


graphic(f1, 1)# шаг x

dx = (x_end - x_begin) / width # шаг по пикселям
graphic(f2, dx)

graphic(f3, 1, smooth=True) # сглаживание

root.mainloop()

