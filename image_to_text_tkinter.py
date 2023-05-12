import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
import os
import sys



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# Create the Tkinter window
window = tk.Tk()
window.title("Text from Image")
window.configure(bg="#222222")  # Set background color to dark gray

# Variables to store image and result
image = None
result = ""


# Function to perform OCR on the image
def perform_ocr():
    global image, result

    if image:
        # Perform OCR
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        result = pytesseract.image_to_string(image, lang="eng+fas")

        # Display the result
        result_text.delete("1.0", tk.END)  # Clear the previous result
        result_text.insert(tk.END, result)
        result_text.configure(state="disabled")  # Disable editing

# Function to copy the text
def copy_text():
    window.clipboard_clear()
    window.clipboard_append(result)


# Function to load and display the image
def load_image():
    global image

    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if filepath:
        # Open the image
        image = Image.open(filepath)

        # Display the image
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo


# Load Image button
load_button = tk.Button(window, text="Load Image", command=load_image, padx=10, pady=5, bg="#555555", fg="#ffffff")
load_button.grid(row=0, column=0, pady=10)

# Copy Text button
copy_button = tk.Button(window, text="Copy Text", command=copy_text, padx=10, pady=5, bg="#555555", fg="#ffffff")
copy_button.grid(row=0, column=2, pady=10)


# Perform OCR button
ocr_button = tk.Button(window, text="Export Text", command=perform_ocr, padx=10, pady=5, bg="#555555", fg="#ffffff")
ocr_button.grid(row=0, column=1, pady=10)

# Label to display the image
image_label = tk.Label(window, bg="#222222")
image_label.grid(row=1, column=0, columnspan=2)

# Text area to display the result
result_text = tk.Text(window, height=10, width=50, bg="#ffffff", fg="#222222")
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_text.tag_configure("right_align", justify="right")  # Configure left alignment tag

# Configure grid weights to make the image label expandable
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)


# Label to display the creator name
creator_label = tk.Label(window, text="Created by | Hossein Qashqaeii |", bg="#222222", fg="#ffffff")
creator_label.grid(row=3, column=0, columnspan=2, pady=(20, 10), sticky="n")

# Start the Tkinter event loop
window.mainloop()

#made by Qashqaeii
