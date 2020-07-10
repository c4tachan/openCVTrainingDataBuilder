import win32gui

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

fontnames = []
hdc = win32gui.GetDC(None)
win32gui.EnumFontFamilies(hdc, None, callback, fontnames)
print("\n".join(fontnames))
win32gui.ReleaseDC(hdc, None)