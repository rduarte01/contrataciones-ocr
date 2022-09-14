import ocrmypdf

from utils import FILES_DIR
from utils.utils import OCRMYPDF_FILES_DIR

class Ocrmypdf_service:

    def scanned_pdf_converter(self, file_path, save_path):
        ocrmypdf.ocr(f"{FILES_DIR}/{file_path}", f"{OCRMYPDF_FILES_DIR}/{save_path}", skip_text=True)
        print('ocrmypdf completed')
