from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import tensorflow as tf
import cv2
import numpy as np
width = 200
height = 200
center = height // 2
white = (255, 255, 255)
green = (0, 128, 0)
mylist = []
flag = 1
operand1 = 0
operand2 = 0
operator = '+'


def answer():
    global operand1
    global operand2
    global operator
    if operator == '+':
        print(operand1 + operand2)
    if operator == '-':
        print(operand1 + operand2)
    if operator == '*':
        print(operand1 + operand2)
    if operator == '/':
        print(operand1 + operand2)


def predictor():
    new_model = tf.keras.models.load_model('epic_num_reader.model')
    global flag
    global operand1
    global operand2
    if flag == 2:
        img = cv2.imread('image.jpg',0)
    else:
        img = cv2.imread('image1.jpg',0)
    dim = (28,28)
    img1 = cv2.resize(img, dim)
    img1 = cv2.bitwise_not(img1)
    l = []
    l.append(img1)
    l = np.array(l)
    predictions = new_model.predict(l)
    temp = np.argmax(predictions[0])
    if flag == 2:
        operand1 = temp
    if flag == 1:
        operand2 = temp
        answer()

def save1(event = None):
    global operator
    if (event == "+"):
        mylist.append(event)
        operator = '+'
    elif (event == "-"):
        mylist.append(event)
        operator = '-'
    elif (event == "*"):
        mylist.append(event)
        operator = '*'
    elif (event == "/"):
        mylist.append(event)
        operator = '/'
    print(operator)

def save():
    global mylist
    global operator
    global flag
    if  flag == 1:
        filename = "image.jpg"
        flag = 2
    elif flag == 2:
        filename = "image1.jpg"
        flag = 1
    image1.save(filename)
    cv.delete("all")
    predictor()


def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black", width=5)
    draw.line([x1, y1, x2, y2], fill="black", width=5)


root = Tk()
root.geometry("400x300")

frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=TRUE)

# Tkinter create a canvas to draw on
cv = Canvas(frame1, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)

frame2 = Frame(root)
frame2.pack(fill=BOTH, expand=TRUE)
button = Button(frame2, text="save", command=save, bg="yellow", width=10, height=3)
plus = Button(frame2, text="Add", bg="pink", width=10, height=3)
minus = Button(frame2, text="Subtract", bg="pink", width=10, height=3)
multiply = Button(frame2, text="Product", bg="pink", width=10, height=3)
devide = Button(frame2, text="Devision", bg="pink", width=10, height=3)

plus.bind('<Button-1>', lambda x: save1("+"))
minus.bind('<Button-1>', lambda x: save1("-"))
multiply.bind('<Button-1>', lambda x: save1("*"))
devide.bind('<Button-1>', lambda x: save1("/"))

button.pack(side=LEFT)
plus.pack(side=LEFT)
minus.pack(side=LEFT)
multiply.pack(side=LEFT)
devide.pack(side=LEFT)


# button.place(width=50,height=30, x=620,y=600)
#
# plus.place(width=50,height=30, x=530,y=650)
#
# minus.place(width=50,height=30, x=590,y=650)
#
# multiply.place(width=50,height=30, x=660,y=650)
#
# devide.place(width=50,height=30, x=720,y=650)
root.mainloop()