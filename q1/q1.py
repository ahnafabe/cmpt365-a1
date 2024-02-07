import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import wave
import numpy as np
import os

def get_file_path(): # Function to get the file path of the WAV file
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("WAV files (*.wav)")
    file_dialog.setWindowTitle("Select WAV File")
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]
        return file_path
    else:
        return None

def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color): # Function to plot the waveform of a single channel iteratively
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

def plot_waveform(wave_file, audio_data, image_width=17500, image_height=14000, scale_factor=0.3, line_width=0.5, total_samples=0, sampling_frequency=0, save_path=None): # Function to plot the waveform of the WAV file
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
    
    if save_path:
        image.save(save_path, 'PNG')
        return save_path

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Waveform Viewer")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)  # Enable scaling of image content
        self.setCentralWidget(self.label)
        
        self.open_button = QPushButton("Open WAV File", self)
        self.open_button.setGeometry(20, 10, 160, 30)
        self.open_button.clicked.connect(self.open_waveform)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(220, 10, 160, 30)
        self.exit_button.clicked.connect(self.close)

    def open_waveform(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "WAV files (*.wav)")
        if file_path:
            wave_file = wave.open(file_path, 'r')
            audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)
            save_path = os.path.splitext(file_path)[0] + ".png"  # Construct the save path
            plot_waveform(wave_file, audio_data, line_width=0.5, total_samples=wave_file.getnframes(), sampling_frequency=wave_file.getframerate(), save_path=save_path)
            pixmap = QPixmap(save_path)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
