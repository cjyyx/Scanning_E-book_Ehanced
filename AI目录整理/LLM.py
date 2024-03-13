# %%
import os

from zhipuai import ZhipuAI

zhipu_api_key = os.environ.get("ZHIPU_API_KEY", None)

zhiouClient = ZhipuAI(api_key=zhipu_api_key)


def chatLLM(
    messages,
    temperature=0.95,
    top_p=0.7,
    max_tokens=1024,
):
    response = zhiouClient.chat.completions.create(
        # model="glm-4",
        model="glm-3-turbo",
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


# %%

if __name__ == "__main__":

    content = "请用一个成语介绍你自己"

    resp = chatLLM([{"role": "user", "content": content}])
    print(resp)
