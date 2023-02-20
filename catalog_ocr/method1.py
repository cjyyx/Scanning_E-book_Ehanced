# %%
import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res
from PIL import Image
from bs4 import BeautifulSoup
from tqdm import tqdm

table_engine = PPStructure(layout=False,show_log=False)
catalog_list=[]

# %%

# 检索catalog文件夹下的所有文件并按名称排序
folder_path = "./catalog"
file_names = os.listdir(folder_path)
sorted_file_names = sorted(file_names)

for img_name in tqdm(sorted_file_names):
    img = cv2.imread("./catalog/{}".format(img_name))
    result = table_engine(img)
    html=result[0]["res"]["html"]

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    catalog_list.extend(list(map(
        lambda x:x.td.text,
        rows
    )))

# %%

with open("catalog.txt","w",encoding="utf-8") as f:
    for row in catalog_list:
        f.write(row+"\n")
