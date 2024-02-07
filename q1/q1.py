
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageDraw, ImageFont
import wave
import numpy as np

def get_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
    return file_path

def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color):
    draw = ImageDraw.Draw(image)
    y_buffer = 3500
    for i in range(0, len(audio_data[channel::2])-1):
        amplitude1 = audio_data[channel::2][i]
        amplitude2 = audio_data[channel::2][i+1]
        x1 = int(i * (image.width / (len(audio_data) // 2)))
        x2 = int((i+1) * (image.width / (len(audio_data) // 2)))
        y1 = int(image.height / 2 - amplitude1 * scale_factor) + channel * y_buffer
        y2 = int(image.height / 2 - amplitude2 * scale_factor) + channel * y_buffer
        draw.line([(x1, y1), (x2, y2)], fill=color, width=int(line_width))

def plot_waveform(wave_file, audio_data, image_width=17500, image_height=14000, scale_factor=0.3, line_width=0.5, total_samples=0, sampling_frequency=0):
    image = Image.new("RGB", (image_width, image_height), "black")
    num_channels = wave_file.getnchannels()
    channel_colors = ["green", "blue", "red", "yellow"]
    for channel, color in zip(range(num_channels), channel_colors):
        plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)
    draw = ImageDraw.Draw(image)
    text = f"Total Samples: {total_samples}\nSampling Frequency: {sampling_frequency} Hz"
    font_size = 1000
    font = ImageFont.load_default().font_variant(size=font_size)
    text_bbox = draw.textbbox((100, 100), text, font=font)
    text_position = (image_width - text_bbox[2] - 10, 10)
    draw.text(text_position, text, font=font, fill="white")
    image.show()

class Application:
    def __init__(self, master=None):
        self.master = master
        self.label = Label(text="Select a WAV file to plot its waveform")
        self.label.pack()
        self.button = Button(text="Select WAV File", command=self.load_file)
        self.button.pack()
        self.button = Button(text="Quit", command=self.master.quit)
        self.button.pack()

    def load_file(self):
        audio_file = get_file_path()
        wave_file = wave.open(audio_file, 'r')
        audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)
        plot_waveform(wave_file, audio_data, line_width=0.5, total_samples=wave_file.getnframes(), sampling_frequency=wave_file.getframerate())

root = Tk()
app = Application(master=root)
root.mainloop()

