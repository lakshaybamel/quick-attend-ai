import streamlit as st
from typing import Optional
from supabase import create_client, Client

# Initialize Supabase client using Streamlit secrets
try:
    supabase: Optional[Client] = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"],
    )
except Exception:
    supabase = None
