# from tkinter import Tk, Button
# from tkinter.filedialog import askopenfilename
# from PIL import Image

# def select_image():
#     file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#     if file_path:
#         img = Image.open(file_path)
#         img.show()

# def create_window():
#     window = Tk()
#     open_button = Button(window, text="Open TIF File", command=select_image, bg="black", fg="white")
#     open_button.pack()
#     exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#     exit_button.pack()
#     window.mainloop()

# create_window()

# from tkinter import Tk, Button, Label
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk
# try:
#     def select_image(label):
#         file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#         if file_path:
#             img = Image.open(file_path)
#             # Resize the image to fit within the window if necessary
#             img.thumbnail((400, 400))
#             photo = ImageTk.PhotoImage(img)
#             label.config(image=photo)
#             label.image = photo

#     def create_window():
#         window = Tk()
#         window.title("Image Viewer")

#         image_label = Label(window)
#         image_label.pack()

#         open_button = Button(window, text="Open TIF File", command=lambda: select_image(image_label), bg="black", fg="white")
#         open_button.pack()

#         exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#         exit_button.pack()

#         window.mainloop()

#     create_window()
# except Exception as e:
#     print(e)


# from tkinter import Tk, Button, Label
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk
# import io

# try:
#     def select_image(label):
#         file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#         if file_path:
#             # Open the TIF image using Pillow
#             img = Image.open(file_path)
            
#             # Convert the TIF image to PNG format in memory
#             with io.BytesIO() as mem:
#                 img.save(mem, format="PNG")
#                 mem.seek(0)
#                 png_img = Image.open(mem)
                
#                 # Resize the image to fit within the window if necessary
#                 png_img.thumbnail((400, 400))
                
#                 # Convert the PNG image to Tkinter PhotoImage
#                 photo = ImageTk.PhotoImage(png_img)
                
#                 # Update the label with the PNG image
#                 label.config(image=photo)
#                 label.image = photo

#     def create_window():
#         window = Tk()
#         window.title("Image Viewer")

#         image_label = Label(window)
#         image_label.pack()

#         open_button = Button(window, text="Open TIF File", command=lambda: select_image(image_label), bg="black", fg="white")
#         open_button.pack()

#         exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#         exit_button.pack()

#         window.mainloop()

#     create_window()
# except Exception as e:
#     print(e)

# from tkinter import Tk, Button, Label
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk
# import io

# def select_image(label):
#     file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#     if file_path:
#         # Open the TIF image using Pillow
#         img = Image.open(file_path)
        
#         # Convert the TIF image to PNG format in memory
#         with io.BytesIO() as mem:
#             img.save(mem, format="PNG")
#             mem.seek(0)
#             png_img = Image.open(mem)
            
#             # Resize the image to fit within the window if necessary
#             png_img.thumbnail((400, 400))
            
#             # Convert the PNG image to Tkinter PhotoImage
#             photo = ImageTk.PhotoImage(png_img)
            
#             # Update the label with the PNG image
#             label.config(image=photo)
#             label.image = photo

# def create_window():
#     window = Tk()
#     window.geometry('800x600')  # Set a default size for the window
#     img_label = Label(window)
#     img_label.pack()
#     open_button = Button(window, text="Open TIF File", command=lambda: select_image(img_label), bg='red', fg='white')
#     open_button.pack()
#     exit_button = Button(window, text="Exit", command=window.quit)
#     exit_button.pack()
#     window.mainloop()

# create_window()

# from tkinter import Tk, Button, Label
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk

# def select_image(label):
#     file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#     if file_path:
#         # Open the TIF image using Pillow
#         img = Image.open(file_path)
        
#         # Convert the TIF image to RGB mode
#         img = img.convert("RGB")
        
#         # Resize the image to fit within the window if necessary
#         img.thumbnail((704, 576))
        
#         # Convert the image to Tkinter PhotoImage
#         photo = ImageTk.PhotoImage(img)
        
#         # Update the label with the image
#         label.config(image=photo)
#         label.image = photo

# def create_window():
#     window = Tk()
#     window.title("Image Viewer")

#     image_label = Label(window)
#     image_label.pack()

#     open_button = Button(window, text="Open File", command=lambda: select_image(image_label), bg="black", fg="white")
#     open_button.pack()

#     exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#     exit_button.pack()

#     window.mainloop()

# create_window()

# from tkinter import Tk, Button, Label
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk
# import os

# def select_image(label):
#     file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#     if file_path:
#         # Open the TIF image using Pillow
#         img = Image.open(file_path)
        
#         # Convert the TIF image to RGB mode
#         img = img.convert("RGB")
        
#         # Resize the image to fit within the window
#         img = img.resize((704, 576))
        
#         # Save the image as PNG
#         png_path = os.path.splitext(file_path)[0] + ".png"
#         img.save(png_path, 'PNG')
        
#         # Open the PNG image
#         img = Image.open(png_path)
        
#         # Convert the image to Tkinter PhotoImage
#         photo = ImageTk.PhotoImage(img)
        
#         # Update the label with the image
#         label.config(image=photo)
#         label.image = photo

# def create_window():
#     window = Tk()
#     window.title("Image Viewer")

#     image_label = Label(window)
#     image_label.pack()

#     open_button = Button(window, text="Open File", command=lambda: select_image(image_label), bg="black", fg="white")
#     open_button.pack()

#     exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#     exit_button.pack()

#     window.mainloop()

# create_window()

# from tkinter import Tk, Button, Label, Frame, BOTH
# from tkinter.filedialog import askopenfilename
# from PIL import Image, ImageTk
# import os

# def select_image(label):
#     file_path = askopenfilename(title="Select Image File", filetypes=[("Image files", "*.tif")])
#     if file_path:
#         # Open the TIF image using Pillow
#         img = Image.open(file_path)
        
#         # Convert the TIF image to RGB mode
#         img = img.convert("RGB")
        
#         # Resize the image to fit within the window
#         img = img.resize((704, 576))
        
#         # Convert the image to Tkinter PhotoImage
#         photo = ImageTk.PhotoImage(img)
        
#         # Save the image as PNG
#         png_path = os.path.splitext(file_path)[0] + ".png"
#         img.save(png_path, 'PNG')
        
#         # Update the label with the image
#         label.configure(image=photo)
#         label.image = photo  # Retain a reference to the PhotoImage object


# def create_window():
#     window = Tk()
#     window.title("Image Viewer")
    
#     # Create a frame to contain the label
#     frame = Frame(window)
#     frame.pack(fill=BOTH, expand=True)  # Expand frame to fill window
    
#     image_label = Label(frame)
#     image_label.pack(fill=BOTH, expand=True)  # Expand label to fill frame
    
#     open_button = Button(window, text="Open File", command=lambda: select_image(image_label), bg="black", fg="white")
#     open_button.pack()

#     exit_button = Button(window, text="Exit", command=window.quit, bg="black", fg="white")
#     exit_button.pack()

#     window.mainloop()


# create_window()


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Display App")

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.open_button = tk.Button(self.master, text="Open Image", command=self.open_image_dialog)
        self.open_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack(side=tk.RIGHT)

    def open_image_dialog(self):
        # file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tif;*.tiff")])
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tif;*.tiff")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo  # Keep a reference to prevent garbage collection

def main():
    root = tk.Tk()
    app = ImageDisplayApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

