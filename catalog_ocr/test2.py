
# %%
import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res
from PIL import Image
from bs4 import BeautifulSoup

# %%
table_engine = PPStructure(table=False, show_log=False)

# %%

img_path = './test.png'
img = cv2.imread(img_path)
result = table_engine(img)

# %%

