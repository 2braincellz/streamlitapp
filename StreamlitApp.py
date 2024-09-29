
import streamlit as st
from PIL import Image, ImageDraw, ImageGrab
import numpy as np
from io import StringIO



def take_image():
      
    img_file_buffer = st.camera_input("Take a photo")

    if img_file_buffer is not None:

        img = Image.open(img_file_buffer)

        st.image(img)

        picture = "im.jpg"

        img.save(picture)

        
        img_array = np.array(img)

        st.write(type(img_array))
        st.write(img_array.shape)


def process_image(image):
     
     im = Image.open(image)

     st.image(im)


def file_upload():

    img_saved = st.file_uploader('upload an image file', type = ['png', 'jpg'])

    if img_saved is not None:

        print(img_saved.type)

        process_image(img_saved)
        
             



        # bytes_data = img_saved.getvalue()
        # st.write(bytes_data)

        # # To convert to a string based IO:
        # stringio = StringIO(img_saved.getvalue().decode("utf-8"))
        # st.write(stringio)

        # # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)


def main():
        file_upload()




if __name__ == "__main__":
    main()