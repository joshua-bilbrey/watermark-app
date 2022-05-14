from PIL import Image, ImageDraw, ImageFont
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from tkinter import filedialog
from tkinter import Tk


def add_watermark(img, text):
    with Image.open(img).convert('RGBA') as base:
        # empty image with no transparency for text
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

        base_w, base_h = base.size
        # calculate font size based on the width of the image and the length of text
        fnt_size = int(base.width / len(text))
        fnt = ImageFont.truetype(font='fonts/ALGER.TTF', size=fnt_size)

        d = ImageDraw.Draw(txt)
        w, h = d.textsize(text, font=fnt)
        txt_coord = (base_w - w) / 2, (base_h - h) / 2
        d.text(txt_coord, text, font=fnt, fill=(211, 211, 211, 128))

        # combine base image and watermark
        out = Image.alpha_composite(base, txt)
        out.save(f'{text}img.png')


class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    def choose_file(self, watermark):
        root = Tk()
        root.withdraw()

        image = filedialog.askopenfilename()
        add_watermark(image, watermark)


class WatermarkApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    WatermarkApp().run()
