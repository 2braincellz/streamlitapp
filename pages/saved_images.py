import streamlit as st
from app import supabase
from functions import get_user_id, check_session
from io import BytesIO
import base64
from PIL import Image

if not check_session():
    st.switch_page('app.py')

def retrieve_images():

    user_id = get_user_id()
    responses = supabase.table("Image_files").select("*").eq("user_id", user_id).execute()
    
    
    # col_idx = 0

    # col1, col2, col3 = st.columns(3)


    for response in responses.data:
        
        # if response['file']:
        #     Base64_decoded = base64.b64decode(response['file'])
        #     img_bytes = BytesIO(Base64_decoded)
        #     img = Image.open(img_bytes)

            # if col_idx % 3 == 0:
            #     with col1:
            #         st.write(img)
            # if col_idx % 3 == 1:
            #     with col2:
            #         st.write(img)
            # if col_idx % 3 == 2:
            #     with col3:
            #         st.write(img)
            # col_idx = col_idx + 1

        st.write(response)
                

def saved():


    retrieve_images()



saved()

