import streamlit as st

def check_session():
    if 'supabase_session' in st.session_state:
            return True
    else:
        return False
    
def show_user_info():
     session = st.session_state['supabase_session']
     st.write(f'Hello 👋 {session.user.user_metadata["email"], session.user.user_metadata}')

def get_user_id():
    session = st.session_state['supabase_session']
    return session.user.user_metadata['sub']
