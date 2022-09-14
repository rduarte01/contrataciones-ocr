from paddleocr import PaddleOCR,draw_ocr
# draw result
from PIL import Image

import aspose.words as aw

from utils import PADDLE_DRAW_RESULT_DIR, FILES_DIR, PADDLE_IMAGES_DIR


class PaddleOCR_service:

    def process_document(self, filename):
        img_path = f'{PADDLE_IMAGES_DIR}/{filename}.jpg'
        ocr = PaddleOCR(lang='es') # need to run only once to download and load model into memory
        result = ocr.ocr(img_path, cls=False)
        #for line in result:
        #    print(line)
        return result

    def draw_result(self,result, filename, filename_save = 'result' ):
        img_path = f'{PADDLE_IMAGES_DIR}/{filename}.jpg'
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='utils/ttf/OpenSans-Bold.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save(f"{PADDLE_DRAW_RESULT_DIR}/{filename_save}.jpg")
    
    def pdf_to_image(self, filename):
        doc = aw.Document(f"{FILES_DIR}/{filename}.pdf")

        for page in range(0, doc.page_count):
            extractedPage = doc.extract_pages(page, 1)
            extractedPage.save(f"{PADDLE_IMAGES_DIR}/{filename}_{page + 1}.jpg")
