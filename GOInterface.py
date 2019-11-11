import tkinter  as tk
import pil as pil
from pil import ImageTk,Image
from cv2 import cv2 
class GOInterface:
    window = tk.Tk()
    # windowWith = '1000'
    # windowHeight = '600'
    cv_image = cv2.imread("C:/Users/ismah/Documents/prive/bezigheidsTherapie/GO/ImageForGUI/GO9by9.png")
    height, width, no_channels = cv_image.shape
    canvas = tk.Canvas(window, width = width, height = height)
    canvas.pack()
    photo = pil.ImageTk.PhotoImage(image = pil.Image.fromarray(cv_image))
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    window.title("GO")
    # window.geometry(windowWith+"x"+windowHeight)
    #GOBoardElement(window)
    window.mainloop()

    def GOBoardElement(self,window):
        imgWidth = "500"
        imgHeight = "500"
        img = Image.open("GO9by9.png")
        img = img.resize(imgWidth+"x"+imgHeight)
        img = ImageTk.PhotoImage(img)
        panel = window.Label(window, image=img)
        panel.image = img
        panel.place(relheight=.095,relwidth=0.25,relx=0.7,rely=0.03)