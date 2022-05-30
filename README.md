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
