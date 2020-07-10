import win32gui

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

def drawFont(hdc, hbm, font):
    pass





if __name__ == "__main__":
    fontnames = []
    hdc = win32gui.GetDC(None)

    win32gui.EnumFontFamilies(hdc, None, callback, fontnames)

    # Determine the size of the bitmap
    width = 30 * (ord('~') - ord(' '))
    height = 30 * len(fontnames)

    # Create the bitmap
    hbm = win32gui.CreateCompatibleBitmap(hdc, width, height)

    for font in fontnames:
        drawFont(hdc, hbm, font)

    print("\n".join(fontnames))
    win32gui.ReleaseDC(hdc, None)