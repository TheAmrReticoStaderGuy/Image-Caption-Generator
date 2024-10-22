# Function to generate a caption for a given input image 
def generate_input_img_caption(image):
    # You can modify the way to extract the ID from the image path if needed
    image_id = os.path.splitext(image.filename)[0]
    predicted_caption = predict_caption(model, features[image_id], tokenizer, max_length)
    return predicted_caption
# Streamlit app
st.title("Image Caption Generator")

# Option for uploading image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Option for entering  URL
image_url = st.text_input("Or enter image URL:")

# Displaying the image and predicting the caption
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    predicted_caption = generate_input_img_caption(uploaded_file)
elif image_url:
    try:
        response = requests.get(image_url)
        image = Image.open(requests.get(image_url, stream=True).raw)
        st.image(image, caption="Image from URL", use_column_width=True)
        predicted_caption = generate_input_img_caption(image_url)
    except Exception as e:
        st.error("Error loading image from URL. Please check the URL.")

if 'predicted_caption' in locals():
    st.subheader("Predicted Caption:")
    st.write(predicted_caption)