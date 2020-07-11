import win32gui
import win32ui
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io

class charRect:
    l = 0
    t = 0
    width = 60
    height = 30
    
    def Right(self):
        return self.l + width

    def Bottom(self):
        return self.t + height

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

def drawFont(dc, fontName, row):
    font = win32ui.CreateFont  ({ "height": 30    # Height
                                ,  "width" : 60    # width
                                ,  "name"  : fontName
     })

    dc.SelectObject(font)
    rc = charRect

    rc.t = row * rc.height

    for c in range(ord(' '), ord('~')):
        dc.DrawText(chr(c), (rc.l, rc.t, rc.Right(rc), rc.Bottom(rc)), 0)
        rc.l = rc.Right(rc)

    return dc


def drawFontPil(img, font, row):
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(font)

    rc = charRect

    rc.t = row * rc.height

    for c in range(ord(' '), ord('~')):
        draw.text((rc.l, rc.t, rc.Right(rc), rc.Bottom(rc)), chr(c), (0,0,0), fnt)
        rc.l = rc.Right(rc)

    return


if __name__ == "__main__":
    fontnames = []
    basedc = win32ui.CreateDC()
    dc = basedc.CreateCompatibleDC()

    win32gui.EnumFontFamilies(dc.GetHandleOutput(), None, callback, fontnames)

    # Determine the size of the bitmap
    width = 60 * (ord('~') - ord(' '))
    height = 30 * len(fontnames)

    # Create the bitmap
    bm = win32ui.CreateBitmap()
    bm.CreateCompatibleBitmap(dc, width, height)

    dc.SelectObject(bm)

    dc.FillSolidRect((0,0,width,height), 0xff)

    im = Image.open("output.png")

    row = 0

    for font in fontnames:
    #    dc = drawFont(dc, font, row)
       drawFontPil(im, font, row)
       row += 1

    # bmpinfo = bm.GetInfo()
    # bmpstr = bm.GetBitmapBits(True)

    # img = open("output.bmp", 'wb')
    # img.write(bmpstr)
    # img.close()

    # im = Image.open(io.BytesIO(bmpstr))

    # im = Image.frombytes(
    #     '1',
    #     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    #     bmpstr
    # )

    im.save("output.png")


    print("\n".join(fontnames))