from langchain.chains import OpenAIChain
from langchain.schema import Message


def chatLLM(messages: list, temperature=0.85, top_p=0.8, stream=False) -> dict:
    # 初始化LangChain对象，这里以OpenAI的GPT模型为例
    chain = OpenAIChain(model="gpt-3.5-turbo", temperature=temperature, top_p=top_p)

    # 转换用户的消息格式
    lc_messages = [Message(content=msg['content'], role=msg['role']) for msg in messages]

    # 使用LangChain的聊天功能发送消息并接收回复
    response = chain.chat(lc_messages, stream=stream)

    # 如果stream为True，处理流式输出
    if stream:
        # 在LangChain中，流式输出通常以生成器的形式返回
        # 我们可以遍历生成器获取连续的回复
        return ({"content": resp.content, "total_tokens": resp.total_tokens} for resp in response)
    else:
        # 如果不是流式请求，则直接返回第一条回复
        resp = next(response)
        return {"content": resp.content, "total_tokens": resp.total_tokens}
