import pyautogui
import os
from tkinter import *
from PIL import Image
from PIL import ImageTk
def callback(event):
    print("clicked", event.x, event.y)


def video2gif(event):
    print()


os.environ['DISPLAY'] = ':0'
area = pyautogui.size()
print(pyautogui.position())
print(pyautogui.size())
folder_name = 'url'
try:
    os.mkdir(f'./{folder_name}')
except:
    print("already exist")
pyautogui.screenshot(f'./{folder_name}/test.png', region=(0, 0, area[0], area[1]))
w = area[0]
h = area[1]
x = w//2
y = h//2

root=Tk()
root.title('capture 도구')

scale_w = w/x
scale_h = h/y

my_canvas = Canvas(root, width=w, height=h, bg='white') #캔버스
my_canvas.pack(pady=20)
 
image = Image.open('a.gif') #이미지 불러오기
image=image.resize((1920, 1080), Image.ANTIALIAS)
img =  ImageTk.PhotoImage(image)
my_image = my_canvas.create_image(0,125, anchor=NW, image=img) #x,y 위치 /
root.geometry('2560x1440')
 
def left(event):
    x = -10
    y = 0
    my_canvas.move(my_image, x, y)
def right(event):
    x = 10
    y = 0
    my_canvas.move(my_image, x, y)
def up(event):
    x = 0
    y = -10
    my_canvas.move(my_image, x, y)
def down(event):
    x = 0
    y = 10
    my_canvas.move(my_image, x, y)

def move(e):
    global img
    img = PhotoImage(file='test.png')  # 이미지 불러오기
    my_image = my_canvas.create_image(e.x, e.y,  image=img)  # x,y 위치 /
    my_label.config(text='위치는 : x| ' + str(e.x) + ' y|' + str(e.y))

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("clicked", callback)
#my_canvas.create_rectangle()

my_label = Label(root, text="")
my_label.pack(pady=20)
# my_canvas.bind('<B1-Motion>', move) 이미지 움직이게 하기
root.mainloop()