import streamlit as st
from handlers import downloadFile, generate_image, get_files

desired_size = (600, 400)

# Streamlit App
st.title("🖼️ Image Generation Gallery ✨")  # Add a title
margin = '<div style="margin: 20px 5px;"></div>'

# User input
with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Type something")
    submit_button = st.form_submit_button(label="Send")

# Press Enter to generate response from chatbot
if submit_button:
    with st.spinner("Generating image..."):
        image = generate_image(user_input)
        st.image(image, use_column_width=True)
        saved_image = downloadFile(user_input, image)
        st.success("Image successfully generated and saved to media folder")


def display_gallery():
    images = get_files()
    length = len(images)

    for i in range(length):
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                image_resized = images[i]["file"].resize(desired_size)
                st.image(image_resized, use_column_width=True,
                         caption=images[i]["title"])
            with col2:
                if i < length-1:
                    image_resized = images[i+1]["file"].resize(desired_size)
                    st.image(image_resized, use_column_width=True,
                             caption=images[i+1]["title"])


if __name__ == "__main__":
    display_gallery()
