# %%
from lxml import etree
import html

ddd = ""

with open("ddd.xml", "r", encoding="gb2312", errors="ignore") as f:
    ddd = f.read()

xml_string=ddd[40:]

root = etree.fromstring(xml_string)

# %%
tags = root.xpath('.//字符串')

# %%

a = 0
b = 100

for i in range(a,b):
    tag= tags[i]
    ncr = etree.tostring(tag).decode()
    unicode_str = html.unescape(ncr)
    print(repr(r"{}".format(unicode_str)))

# %%

for tag in tags:
    ncr = etree.tostring(tag).decode()
    unicode_str = html.unescape(ncr)
    print(repr(r"{}".format(unicode_str)))
