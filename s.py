import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = st.secrets['SUPABASE_URL']
SUPABASE_KEY = st.secrets['SUPABASE_KEY']
supabase:Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def main():
    st.write(SUPABASE_URL)



if __name__ == "__main__":
    main()
