#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

os.environ["REPLICATE_API_TOKEN"] = "r8_PbwGQdOdihHTKSTYzhJc97NoNCT1oNe0kk9t8"


# In[6]:


import replicate

# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is the capital of France?"

# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters


# In[7]:


full_response = ""

for item in output:
  full_response += item

print(full_response)


# In[10]:


import streamlit as st
import os
import replicate

# Set your API token (ensure this is stored securely in production)
os.environ["REPLICATE_API_TOKEN"] = "r8_PbwGQdOdihHTKSTYzhJc97NoNCT1oNe0kk9t8"

# Streamlit app
st.title("LLM Chat Interface")
st.subheader("Powered by LLaMA13B-v2 Chat Model")

# User input
pre_prompt = st.text_area("System Prompt", "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.", height=150)
user_input = st.text_input("User Prompt", "What is the capital of France?")

# Button to generate a response
if st.button("Generate Response"):
    if user_input.strip() == "":
        st.error("Please enter a prompt.")
    else:
        try:
            # Call the model
            st.info("Generating response...")
            output = replicate.run(
                'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                input={
                    "prompt": f"{pre_prompt} {user_input} Assistant: ",
                    "temperature": 0.1,
                    "top_p": 0.9,
                    "max_length": 128,
                    "repetition_penalty": 1
                }
            )
            # Combine the output chunks
            full_response = "".join(output)
            st.success("Response Generated:")
            st.text_area("Assistant Response", full_response, height=200)
        except Exception as e:
            st.error(f"An error occurred: {e}")


# In[ ]:




