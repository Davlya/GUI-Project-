# GUI-Project-
import mandatory libraries/modules
from PIL import Image
import os


d=(40,40,1080,1080)

water=Image.open(r"C:\Users\Davlya\Downloads\PL drafts\watermark.png")
folder = r"C:\Users\zhasm\Downloads\PL drafts\PIL"


for img in os.listdir(folder):

    
    if (img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jpeg")):

        
        x=Image.open(img)
        y=x.crop(d)
        z=y.convert("L")
        z.paste(water, (825 ,700))

        
        z.save(str("editted_")+img)
        x.close()

def buttons(self):
        bw_filter = Button(self.root, width=18, height=5, text="Apply a BW filter", command=self.bw_filter_command)
        rotate_right = Button(self.root, width=18, height=5, text="Rotate image right", command=self.rotate_right_command)
        rotate_left = Button(self.root, width=18, height=5, text="Rotate image left", command=self.rotate_left_command)
        upside = Button(self.root, width=18, height=5, text="Upside image", command=self.upside_command)
        mirror = Button(self.root, width=18, height=5, text="Mirror image", command=self.mirror_command)
        negative = Button(self.root, width=18, height=5, text="Negative image", command=self.negative_command)
        bw_filter.grid(row=1, column=0)
        rotate_right.grid(row=1, column=2)
        rotate_left.grid(row=1, column=3)
        upside.grid(row=2, column=0)
        mirror.grid(row=2, column=2)
        negative.grid(row=2, column=3)
