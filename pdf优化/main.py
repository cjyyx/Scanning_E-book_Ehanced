# %%
import re

# %%

ddd = ""
matches = []

with open("ddd.xml", "r", encoding="gb2312", errors="ignore") as f:
    ddd = f.read()

pattern = r"[\u4e00-\u9fa5]\s+[\u4e00-\u9fa5]"

for match in re.finditer(pattern, ddd):
    matches.append((match.start(), match.end()))

# %%


def print_match(a, b, L=3):
    for i in range(a, b):
        print(r"{}".format(ddd[
            matches[i][0]-L:matches[i][1]+L
        ]))

print_match(0,100)

# %%

excluded_items = ["签 文", "数 类"]

new_matches = []

for m in matches:
    if ddd[m[0]:m[1]] in excluded_items:
        pass
    else :
        new_matches.append(m)

matches = new_matches

# %%


# %%

result = ddd[matches[0][0]:matches[0][1]]
