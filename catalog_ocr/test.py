# %%
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


# %%

ocr = PaddleOCR(use_angle_cls=True)

# %%

img_path = './test.png'
ocr_result = ocr.ocr(img_path, cls=True)

# %%


for idx in range(len(ocr_result)):
    res = ocr_result[idx]
    for line in res:
        print(line)


# %%

result = ocr_result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result.png')
