# Text from Image

Text from Image is a graphical user interface (GUI) application built with Python and Tkinter that performs Optical Character Recognition (OCR) on an image. It allows you to select an image file and extract text from the image using the Tesseract OCR engine.

## Features

- Load an image file (supports PNG, JPG, and JPEG formats).
- Perform OCR on the loaded image.
- Display the extracted text.
- Copy the text to the clipboard.

## Requirements

- Python 3.x
- Tkinter
- Pillow (PIL)
- pytesseract
- Tesseract-OCR

## Installation

1. Clone the repository:
2.Install the required dependencies:
  pip install -r requirements.txt 
  #Note: Make sure Tesseract-OCR is installed on your system and the path to the Tesseract executable is correctly set in the code (pytesseract.pytesseract.tesseract_cmd).

Usage
Run the following command to start the application:
python text_from_image.py
Click the "Load Image" button to select an image file.
Once the image is loaded, click the "Export Text" button to perform OCR and display the extracted text in the text area.
To copy the text, click the "Copy Text" button.

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Credits
This project was created by Hossein qashqaeii. (qashqaeii.ps4@gmail.com)
