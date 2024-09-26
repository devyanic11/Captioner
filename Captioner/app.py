import streamlit as st
import os
from PIL import Image
from brain import get_image_description, get_instagram, get_twitter, get_linkedin

st.set_page_config(page_title="Social Media Captioner App",
                   page_icon="🧊",
                   layout="wide")

st.title(":blue[Social Media] Captioner")
st.caption(
    "Enter the details and get cool captions for your posts! :sunglasses:")

col1, col2 = st.columns(2)

# st.write(" ")
# st.write(" ")
# st.write(" ")
caption = ""
with col1:
    # st.subheader("", divider="gray")
    with st.form(key='my_form'):
        instructions = st.text_area("Describe what you want.")
        platform = st.radio("Platform:", ["Linkedin", "Instagram", "Twitter"])
        option = st.selectbox(
            "Tone",
            ("Cheerful", "Professional", "Sad"),
            placeholder="Select tone of caption...",
        )

        uploaded_file = st.file_uploader("Choose an image...",
                                         type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Submit')

    if uploaded_file is not None:
        save_path = os.path.join("uploads", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        image = Image.open(save_path)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        st.write("Image path:", save_path)
        image_description = get_image_description(save_path)
        if platform == "Linkedin":
            caption = get_linkedin(instructions, image_description)
        if platform == "Instagram":
            caption = get_instagram(instructions, image_description)
        if platform == "Twitter":
            caption = get_twitter(instructions, image_description)
    else:
        st.write("Please upload an image file.")

with col2:
    st.subheader("Results:")
    if submit_button:
        st.write(caption)
