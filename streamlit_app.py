import streamlit as st
import google.generativeai as genai

# Configure GenAI API key
genai.configure(api_key="AIzaSyAL94E1WaxlpYhewI9sQlfhXoBo9fnRog4")

# Set up the model configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
  "stop_sequences": ["พอแล้ว"]
}

safety_settings = [
  {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]

system_instruction = "คุณคือ Chatbot ที่ไม่มีความรู้อะไรเลย แต่เข้าใจภาษาไทยได้ดี คุณจะเรียนรู้จากคำถามและจดจำการพูดคุย ถ้าคุณไม่รู้ก็จะถามว่าคืออะไร"

# Initialize the GenerativeModel
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

# Create a form to input the question
with st.form(key='chatbot_form'):
    question = st.text_input("คำถาม")
    submit_button = st.form_submit_button(label='Submit')

# If the form is submitted
if submit_button:
    # Generate response from the question
    response = model.predict([question])

    # Display the response
    st.write("คำตอบ:", response[0])
