import streamlit as st
import requests

API_TOKEN = "r_zDRWXF9l-oGQy_RlIFDifbiVAPm5oqehjr9E9T"
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/4d54f5adbf4f7a20935077ee9ad2dd52/ai/run/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def run(model, inputs):
    input = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


def generate_response(uploaded_file, query_text):
    # Load document if file is uploaded
    if uploaded_file is not None:
        documents = [uploaded_file.read().decode()]
        source = documents[0]
        inputs = [
            {
                "role": "system",
                "content": "You are an expert, who responds to user's questions according to the source document they provide. The Source document will be in between the symbol of #####. And the user query will be inside XXXXX",
            },
            {
                "role": "user",
                "content": f"Answer the following question according to ##### \n {source} \n##### \n\n\n\n\n , Question is XXXXX \n{query_text}\n XXXXX",
            },
        ]
        output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
        return output["result"]["response"]


# Page title
st.set_page_config(page_title=" App")
st.title("🦜🔗 Ask the Doc App")

# File upload
uploaded_file = st.file_uploader("Upload an article", type="txt")
# Query text
query_text = st.text_input(
    "Enter your question:",
    placeholder="Please provide a short summary.",
    disabled=not uploaded_file,
)

# Form input and query
result = []

submitted = st.button("Run", disabled=False, type="primary")
if submitted:
    with st.spinner("Running LLM..."):
        response = generate_response(uploaded_file, query_text)
        result.append(response)

if len(result):
    st.info(response)
