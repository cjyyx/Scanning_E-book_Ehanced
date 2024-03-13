# %%
from tqdm import tqdm

from LLM import chatLLM

# %%

with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

with open("ocr_result.txt", "r", encoding="utf-8") as f:
    ocr_result = f.read()

# 分割字符串

n = 1800
ocr_result_list = [ocr_result[i : i + n] for i in range(0, len(ocr_result), n)]

# %%

format_result = []

with open("format_result.txt", "w", encoding="utf-8") as f:
    for ocr in tqdm(ocr_result_list):
        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "明白了。等待你提供OCR结果。"},
            {"role": "user", "content": ocr},
        ]

        response = chatLLM(
            messages=messages,
            temperature=0.7,
            max_tokens=4096,
        )

        start_keyword = "[格式化后的目录]"
        end_keyword = "[存在的问题]"

        start_index = response.find(start_keyword) + len(start_keyword)
        end_index = response.find(end_keyword)

        f.write(response[start_index:end_index].strip() + "\n")
        format_result.append(response)


# %%
