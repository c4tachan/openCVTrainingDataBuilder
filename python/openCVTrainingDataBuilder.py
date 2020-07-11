import io
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class charRect:
    def __init__(self):
        self.l = 0
        self.t = 0
        self.width = 60
        self.height = 30
    
    def Right(self):
        return self.l + self.width

    def Bottom(self):
        return self.t + self.height

def drawFont(img, font, row):
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype(f".\\trainedFonts\\{font}", size=20)

    rc = charRect()

    rc.t = row * rc.height

    # draw.text((0, rc.t), font, font=(ImageFont.truetype("arial", size=10)), align="left")

    for c in range(ord('!'), (ord('~') + 1)):
        #draw.rectangle(((rc.l, rc.t), (rc.Right(), rc.Bottom())), fill="black")
        draw.text((rc.l + 10, rc.t), chr(c), font=fnt, align="right")
        rc.l = rc.Right()

    return


if __name__ == "__main__":
    # get list of installed fonts from C:\Windows\Fonts
    fontnames = os.listdir(".\\trainedFonts")


    # Determine the size of the bitmap
    width = 60 * (ord('~') - ord(' '))
    height = 30 * len(fontnames)

    im = Image.new("RGB", (width, height)) #, (255,255,255))

    row = 0

    for font in fontnames:
        if font.endswith(".ttf"):
            drawFont(im, font, row)
            
            row += 1
            # input()

    
    im.show()
    im.save("output.png")


    print("\n".join(fontnames))