
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# from tkinter import Tk, filedialog

# def get_file_path():
#     # Create a Tkinter root window (it won't be shown)
#     root = Tk()
#     root.withdraw()

#     # Open a file dialog to choose the WAV file
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])

#     return file_path

# def plot_wav(file_path):
#     # Read the WAV file
#     sample_rate, data = wavfile.read(file_path)

#     # If the WAV file has two channels, take the first two columns (channels)
#     if len(data.shape) > 1:
#         channel1 = data[:, 0]
#         channel2 = data[:, 1]
#     else:
#         # If the WAV file has only one channel, duplicate it for plotting
#         channel1 = channel2 = data

#     # Time axis
#     time = np.arange(0, len(channel1)) / sample_rate

#     # Plotting
#     plt.figure(figsize=(10, 6))

#     plt.subplot(2, 1, 1)
#     plt.plot(time, channel1, label='Channel 1')
#     plt.title('Channel 1')
#     plt.xlabel('Time (seconds)')
#     plt.ylabel('Amplitude')
#     plt.legend()

#     plt.subplot(2, 1, 2)
#     plt.plot(time, channel2, label='Channel 2', color='orange')
#     plt.title('Channel 2')
#     plt.xlabel('Time (seconds)')
#     plt.ylabel('Amplitude')
#     plt.legend()

#     plt.tight_layout()
#     plt.show()

# # Get the file path from the user
# file_path = get_file_path()

# # Check if a file was selected
# if file_path:
#     # Plot the selected WAV file
#     plot_wav(file_path)



# import numpy as np
# from scipy.io import wavfile
# from tkinter import Tk, filedialog
# from PIL import Image, ImageDraw

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_wav(file_path):
#     sample_rate, data = wavfile.read(file_path)

#     if len(data.shape) > 1 and data.shape[1] == 2:
#         channel1 = data[:, 0]
#         channel2 = data[:, 1]
#     else:
#         print("Error: The audio file should be stereo.")
#         return

#     total_samples = len(channel1)
#     if total_samples % 2 != 0 or total_samples >= 65536:
#         print("Error: The total number of samples should be an even number less than 65536.")
#         return

#     time = np.arange(0, total_samples) / sample_rate

#     normalized_channel1 = (channel1 - np.min(channel1)) / (np.max(channel1) - np.min(channel1))
#     normalized_channel2 = (channel2 - np.min(channel2)) / (np.max(channel2) - np.min(channel2))

#     img_width, img_height = total_samples // 2, 200  # Adjusted img_width
#     img1 = Image.new("RGB", (img_width, img_height), "white")
#     draw1 = ImageDraw.Draw(img1)

#     img2 = Image.new("RGB", (img_width, img_height), "white")
#     draw2 = ImageDraw.Draw(img2)

#     plot_channel(draw1, time, normalized_channel1, color=(0, 0, 0))
#     img1.show()

#     plot_channel(draw2, time, normalized_channel2, color=(255, 165, 0))
#     img2.show()

# def plot_channel(draw, time, channel, color):
#     img_height = draw.im.size[1]
#     x_values = (time * draw.im.size[0]).astype(int)
#     y_values = (channel * img_height).astype(int)

#     for i in range(len(x_values) - 1):
#         draw.line([(x_values[i], img_height - y_values[i]), (x_values[i + 1], img_height - y_values[i + 1])], fill=color)

# file_path = get_file_path()

# if file_path:
#     plot_wav(file_path)

# from PIL import Image, ImageDraw
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path


# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5):
#     image = Image.new("RGB", (image_width, image_height), "black")
#     draw = ImageDraw.Draw(image)

#     # Draw the waveform
#     for i, amplitude in enumerate(audio_data):
#         x = int(i * (image_width / len(audio_data)))
#         y = int(image_height / 2 + amplitude * scale_factor)
#         draw.line([(x, image_height // 2), (x, y)], fill="green", width=int(line_width))

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5)

#     print("Number of chanel: ", wave_file.getnchannels()) ## we need plot for two separate channels

# from PIL import Image, ImageDraw
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel):
#     draw = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw.line([(x, image.height // 2), (x, y)], fill="green", width=int(line_width))

# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5):
#     image = Image.new("RGB", (image_width, image_height), "black")

#     # Get the number of channels
#     num_channels = wave_file.getnchannels()

#     # Plot waveform for each channel
#     for channel in range(num_channels):
#         plot_channel_waveform(audio_data, image, scale_factor, line_width, channel)

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5)

#     print("Number of channels:", wave_file.getnchannels())

# from PIL import Image, ImageDraw
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_channel_waveform1(audio_data, image, scale_factor, line_width, channel, color):
#     draw1 = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw1.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))

# def plot_channel_waveform2(audio_data, image, scale_factor, line_width, channel, color):
#     draw2 = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw2.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))


# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5):
#     image = Image.new("RGB", (image_width, image_height), "black")

#     # Get the number of channels
#     num_channels = wave_file.getnchannels()

#     # Define colors for each channel
#     channel_colors = ["green", "blue", "red", "yellow"]  # Add more colors if needed

#     # Plot waveform for each channel with a different color
#     # for channel, color in zip(range(num_channels), channel_colors):
#     #     plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)

#     plot_channel_waveform1(audio_data, image, scale_factor, line_width, 0, "green")
#     plot_channel_waveform2(audio_data, image, scale_factor, line_width, 1, "blue")

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5)

#     print("Number of channels:", wave_file.getnchannels())















# from PIL import Image, ImageDraw
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color):
#     draw = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))

# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5):
#     image = Image.new("RGB", (image_width, image_height), "black")

#     # Get the number of channels
#     num_channels = wave_file.getnchannels()

#     # Define colors for each channel
#     channel_colors = ["green", "blue", "red", "yellow"]  # Add more colors if needed

#     # Plot waveform for each channel with a different color
#     for channel, color in zip(range(num_channels), channel_colors):
#         plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5)

#     print("Number of channels:", wave_file.getnchannels())

# from PIL import Image, ImageDraw, ImageFont
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color):
#     draw = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))

# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5, total_samples=0, sampling_frequency=0):
#     image = Image.new("RGB", (image_width, image_height), "black")

#     # Get the number of channels
#     num_channels = wave_file.getnchannels()

#     # Define colors for each channel
#     channel_colors = ["green", "blue", "red", "yellow"]  # Add more colors if needed

#     # Plot waveform for each channel with a different color
#     for channel, color in zip(range(num_channels), channel_colors):
#         plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)

#     # Display total samples and sampling frequency on the image
#     draw = ImageDraw.Draw(image)
#     text = f"Total Samples: {total_samples}\nSampling Frequency: {sampling_frequency} Hz"

#     # Adjust the position and font size of the text
#     font_size = 30
#     font = ImageFont.load_default()  # You can use a different font if needed

#     text_bbox = draw.textbbox((10, 10), text, font=font)
#     text_position = (image_width - text_bbox[2] - 10, 10)

#     draw.text(text_position, text, font=font, fill="white")

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5, total_samples=wave_file.getnframes(), sampling_frequency=wave_file.getframerate())

#     print("Number of channels:", wave_file.getnchannels())
# from PIL import Image, ImageDraw, ImageFont
# import wave
# import numpy as np
# from tkinter import Tk, filedialog

# def get_file_path():
#     root = Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
#     return file_path

# def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color):
#     draw = ImageDraw.Draw(image)

#     # Draw the waveform for the specified channel
#     for i, amplitude in enumerate(audio_data[channel::2]):  # Adjust the index to select the desired channel
#         x = int(i * (image.width / len(audio_data)))
#         y = int(image.height / 2 + amplitude * scale_factor)
#         draw.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))

# def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5, total_samples=0, sampling_frequency=0):
#     image = Image.new("RGB", (image_width, image_height), "black")

#     # Get the number of channels
#     num_channels = wave_file.getnchannels()

#     # Define colors for each channel
#     channel_colors = ["green", "blue", "red", "yellow"]  # Add more colors if needed

#     # Plot waveform for each channel with a different color
#     for channel, color in zip(range(num_channels), channel_colors):
#         plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)

#     # Display total samples and sampling frequency on the image
#     draw = ImageDraw.Draw(image)
#     text = f"Total Samples: {total_samples}\nSampling Frequency: {sampling_frequency} Hz"

#     # Adjust the position and font size of the text
#     font_size = 30
#     font = ImageFont.load_default()  # You can use a different font if needed

#     text_bbox = draw.textbbox((10, 10), text, font=font)
#     text_position = (image_width - text_bbox[2] - 10, 10)

#     # Use font_size in the draw.text call
#     draw.text(text_position, text, font=font, fill="white")

#     image.show()

# if __name__ == "__main__":
#     audio_file = get_file_path()
#     wave_file = wave.open(audio_file, 'r')

#     # Get the audio data
#     audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

#     # Set up the image and plot the waveform with even thinner lines
#     plot_waveform(audio_data, line_width=0.5, total_samples=wave_file.getnframes(), sampling_frequency=wave_file.getframerate())

#     print("Number of channels:", wave_file.getnchannels())

from PIL import Image, ImageDraw, ImageFont
import wave
import numpy as np
from tkinter import Tk, filedialog

def get_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV files", "*.wav")])
    return file_path

def plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color):
    draw = ImageDraw.Draw(image)

    # Draw the waveform for the specified channel
    for i, amplitude in enumerate(audio_data[channel::2]):
        x = int(i * (image.width / len(audio_data)))
        y = int(image.height / 2 + amplitude * scale_factor)
        draw.line([(x, image.height // 2), (x, y)], fill=color, width=int(line_width))

def plot_waveform(audio_data, image_width=5000, image_height=2000, scale_factor=0.5, line_width=0.5, total_samples=0, sampling_frequency=0):
    image = Image.new("RGB", (image_width, image_height), "black")

    # Get the number of channels
    num_channels = wave_file.getnchannels()

    # Define colors for each channel
    channel_colors = ["green", "blue", "red", "yellow"]

    # Plot waveform for each channel with a different color
    for channel, color in zip(range(num_channels), channel_colors):
        plot_channel_waveform(audio_data, image, scale_factor, line_width, channel, color)

    # Display total samples and sampling frequency on the image
    draw = ImageDraw.Draw(image)
    text = f"Total Samples: {total_samples}\nSampling Frequency: {sampling_frequency} Hz"

    # Adjust the position and font size of the text
    font_size = 100  # Adjust the font size as needed
    font = ImageFont.load_default().font_variant(size=font_size)

    text_bbox = draw.textbbox((100, 100), text, font=font)
    text_position = (image_width - text_bbox[2] - 10, 10)

    # Use the larger font_size in the draw.text call
    draw.text(text_position, text, font=font, fill="white")

    image.show()

if __name__ == "__main__":
    audio_file = get_file_path()
    wave_file = wave.open(audio_file, 'r')
    audio_data = np.frombuffer(wave_file.readframes(-1), dtype=np.int16)

    plot_waveform(audio_data, line_width=0.5, total_samples=wave_file.getnframes(), sampling_frequency=wave_file.getframerate())

