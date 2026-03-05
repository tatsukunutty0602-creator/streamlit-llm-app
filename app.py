from dotenv import load_dotenv
load_dotenv()

def run_llm(selected_item, input_text):

    from openai import OpenAI
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage


    if selected_item == "お金の専門家":
        system_message = "あなたはお金の専門家です。"
    elif selected_item == "健康の専門家":
        system_message = "あなたは健康の専門家です。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    result = llm.invoke(messages)

    output_text = result.content
    return output_text


import streamlit as st

st.title("LLMアプリ")

st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでAIからの回答を表示します。")

selected_item = st.radio(
    "相談したい専門家を選択してください。",
    ["お金の専門家", "健康の専門家"]
)
input_text = st.text_input(label="テキストを入力してください。")

st.divider()

if st.button("実行"):
    st.divider()
    output_text = run_llm(selected_item, input_text)
    st.write(f"回答: **{output_text}**")

