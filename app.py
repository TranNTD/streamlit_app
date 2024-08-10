import requests
import streamlit as st
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Thuy Dung Webpage", page_icon = "🥰", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_code = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---- HEADER SECTION ---
with st.container(): # optional
    st.subheader("subheader of this web :wave:")
    st.title("Web Title")
    st.write("describtion 1")
    st.write("describtion 2")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Left column header")
        st.write("write something")

    with right_column:
        st.header("right header")