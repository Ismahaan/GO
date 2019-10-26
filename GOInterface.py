import tkinter  as tk
from PIL import ImageTk,Image
class GOInterface:
    window = tk.Tk()
    windowWith = '1000'
    windowHeight = '600'
    window.title("GO")
    window.geometry(windowWith+"x"+windowHeight)
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