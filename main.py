
from tkinter import *
from tkinter.ttk import Notebook

from PIL import Image, ImageOps

import os


class Photo_editor:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="Choose a Button")
        self.label.grid(row=0,column=0)
        self.image_tabs = Notebook(self.root)
        self.count_bw = 1
        self.count_r = 1
        self.count_l = 1
        self.init()
# Windows settings 
    def init(self):
        self.root.geometry('400x400')
        self.root.title('Photo editor')
        self.image_tabs.enable_traversal()
        
        
      #  water=Image.open(r"C:\Users\Dovl\Downloads\PL drafts\watermark.png")
      #  folder = r"C:\Users\Dovl\Downloads\PL drafts\PIL"


# Method thta creates windows and call buttons
    def window(self):
        self.buttons()
        self.root.mainloop()


    #Method that creates buttoms in TKinter Window
    def buttons(self):
        bw_filter = Button(self.root, width=18, height=5, text="Apply a BW filter", bg = 'grey', command=self.bw_fil)
        rotate_right = Button(self.root, width=18, height=5, text="Rotate image right", bg='red', command=self.right_com)
        rotate_left = Button(self.root, width=18, height=5, text="Rotate image left", bg='blue', command=self.left_com)
        bw_filter.grid(row=1, column=0)
        rotate_right.grid(row=1, column=2)
        rotate_left.grid(row=1, column=3)



    

    
#Method that applies b/w filter
    def bw_fil(self):
        os.mkdir(f"bw filter {str(self.count_bw)}")
        folder_name = (f'bw filter {str(self.count_bw)}'+'/{}_bw{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.convert('L')
                new_img.save(folder_name.format(img_n, img_ext))
        
        self.count_bw += 1

#Method for rotating images to the Right
    def right_com(self):
        #There is I created new folder
        os.mkdir(f"rotate right {str(self.count_r)}")
        folder_name = (f'rotate right {str(self.count_r)}'+'/{}_right{}')

        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            img = Image.open(i)
            new_img = img.rotate(angle=-90, expand=True)

            new_img.save(folder_name.format(img_n, img_ext))
        self.count_r += 1


    
# Rotating images to the Left
    def left_com(self):
        os.mkdir(f"rotate left {str(self.count_l)}")
        folder_name = (f'rotate left {str(self.count_l)}'+'/{}_left{}')

        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            img = Image.open(i)
            new_img = img.rotate(angle=90, expand=True)
            new_img.save(folder_name.format(img_n, img_ext))

        self.count_l += 1




if __name__ == "__main__":
    Photo_editor().window()
