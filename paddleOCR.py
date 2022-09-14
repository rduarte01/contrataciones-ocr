from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR(lang='es') # need to run only once to download and load model into memory
img_path = 'Output_3.jpg'
result = ocr.ocr(img_path, cls=False)
for line in result:
    print(line)

# draw result
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='OpenSans-Bold.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')