
import streamlit as st
from supabase import create_client, Client
from functions import check_session

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()


# Print results.
def print_query(query):
    for row in query.data:
        st.write(f"{row['name']} has a :{row['pet']}:")


def sign_up():
    user = supabase.auth.sign_up({"email":"ahuwindsor@gmail.com","password":"password"})

def sign_in(email, password):
    try:
        session = supabase.auth.sign_in_with_password({"email" : email, "password" : password})
        st.session_state['supabase_session'] = session
        st.success("Signed in successfully")
        return session
    except Exception as e:
        st.write(f"Authentication failed {e}")

def show_user_info():
    user = supabase.auth.get_user()
    if user:
        st.write("Logged in as:", user.user.email)
    else:
        st.write("No User is currently logged in")

def main():

    if not check_session():

        with st.form(key = 'login_form'):
            email = st.text_input("Email")
            password = st.text_input("Password", type = "password")
            submit_button = st.form_submit_button(label = "Sign In")

        if submit_button:
            session = sign_in(email, password)
            if session:
                st.switch_page("pages/tools.py")
            else:
                st.error("Sign in failed")

if __name__ == "__main__":
    main()