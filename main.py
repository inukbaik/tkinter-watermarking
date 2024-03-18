import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        self.image_path = ""
        self.logo_path = ""
        self.text = "Your Watermark"
        self.font_size = 30
        self.color = "white"

        self.create_widgets()

    def create_widgets(self):
        # Upload Image Button
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        # Upload Logo Button
        self.upload_logo_button = tk.Button(self.root, text="Upload Logo", command=self.upload_logo)
        self.upload_logo_button.pack()

        # Watermark Text Entry
        self.text_entry = tk.Entry(self.root, width=30)
        self.text_entry.insert(0, self.text)
        self.text_entry.pack()

        # Watermark Font Size Scale
        self.font_size_scale = tk.Scale(self.root, label="Font Size", from_=10, to=50, orient="horizontal", command=self.update_font_size)
        self.font_size_scale.set(self.font_size)
        self.font_size_scale.pack()

        # Choose Color Button
        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

        # Add Watermark Button
        self.add_watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

    def upload_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

    def update_font_size(self, value):
        self.font_size = int(value)

    def choose_color(self):
        self.color = tk.colorchooser.askcolor()[1]

    def add_watermark(self):
        if self.image_path:
            img = Image.open(self.image_path)
            draw = ImageDraw.Draw(img)

            # Add Text Watermark
            if self.text_entry.get():
                font = ImageFont.truetype("arial.ttf", self.font_size)
                text_width, text_height = draw.textsize(self.text, font=font)
                text_position = ((img.width - text_width) // 2, img.height - text_height - 20)
                draw.text(text_position, self.text, fill=self.color, font=font)

            # Add Logo Watermark
            if self.logo_path:
                logo = Image.open(self.logo_path)
                img.paste(logo, (0, 0), logo)

            img.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
