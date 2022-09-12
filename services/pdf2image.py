import platform
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

from utils import FILES_DIR


class Pdf2image_services:

    def pdf_to_text(self, filename):
        # Path of the Input pdf
        PDF_file = Path(f"{FILES_DIR}/{filename}_ocrmypdf.pdf")

        # Store all the pages of the PDF in a variable
        image_file_list = []

        text_file = Path(f"{FILES_DIR}/{filename}_pdf2image.txt")

        ''' Main execution point of the program'''
        with TemporaryDirectory() as tempdir:
            """
            Part #1 : Converting PDF to images
            """

            if platform.system() == "Windows":
                pdf_pages = convert_from_path(
                    PDF_file, 500, poppler_path=path_to_poppler_exe
                )
            else:
                pdf_pages = convert_from_path(PDF_file, 500)
            for page_enumeration, page in enumerate(pdf_pages, start=1):
                filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
                page.save(filename, "JPEG")
                image_file_list.append(filename)

            """
            Part #2 - Recognizing text from the images using OCR
            """

            with open(text_file, "a") as output_file:
                for image_file in image_file_list:
                    text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                    text = text.replace("-\n", "")
                    output_file.write(text)
        print('pdf_to_text completed')