import streamlit as st
from supabase import create_client, Client
from app import supabase
from functions import check_session, show_user_info, get_user_id
from PIL import Image
from io import StringIO, BytesIO
import base64


if not check_session():
    st.switch_page('app.py')

def save_image(image_file):

    user_id = get_user_id()

    name = image_file.name
    bytes_data = image_file.getvalue()
    base64_image = base64.b64encode(bytes_data).decode('utf-8')
    # st.write(base64_image)

    supabase.table('Image_files').insert({"user_id":user_id, "file_name" : name, "file" : base64_image}).execute()

    
    # img_byte_arr = BytesIO()

    # image_file.save(img_byte_arr, format = "JPEG")
    # img_byte_arr.seek(0)
    # st.write(img_byte_arr)


    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(image_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)



    # str_image = str(image_file)

    # st.write(str_image)


    

def upload_file():

    try:
        img_buffer = st.file_uploader("Upload an Image file", type = ['jpg', 'png'])
        if img_buffer:
            st.write(img_buffer.name)
            img = Image.open(img_buffer)
            st.image(img)
            return img_buffer

    except Exception as e:
        str.error("Unable to Upload file")
        st.write(e) 
        return


def tools():

    show_user_info()
    img= upload_file()

    if st.button("Save Image"):
        save_image(img)

    if st.button("See Past Images"):
        st.switch_page("pages/saved_images.py")

    # img_buffer = st.file_uploader("Upload an Image file", type = ['jpg', 'png'])

    # uploaded_file = st.file_uploader("Choose a file")
    # if uploaded_file is not None:
    #     # To read file as bytes:
    #     # bytes_data = uploaded_file.getvalue()
    #     # st.write(bytes_data)

    #     # To convert to a string based IO:
    #     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #     st.write(stringio)

    #     # To read file as string:
    #     string_data = stringio.read()
    #     st.write(string_data)


    


    # upload_file()


    #     return
    # img = upload_file()
    # save_image(img)




tools()