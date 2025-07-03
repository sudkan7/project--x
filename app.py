import streamlit as st

st.set_page_config(page_title="Project X", layout="wide")

st.title("🎵 Project X - Music as Equity Platform")

# Mock login
role = st.sidebar.selectbox("Login as", ["Viewer", "Artist"])

# Sidebar navigation
page = st.sidebar.radio("Go to", ["Trending Songs", "Upcoming Songs", "Dashboard", "Upload IPO", "Search"])

if page == "Trending Songs":
    st.subheader("🔥 Trending Songs")
    st.info("List of most interacted songs (mock data)")

elif page == "Upcoming Songs":
    st.subheader("🚀 Upcoming Songs")
    st.info("Upcoming IPOs and unreleased tracks")

elif page == "Dashboard":
    if role == "Viewer":
        st.subheader("📊 Your Viewer Dashboard")
        st.success("You own 3 song shares (mock)")
    else:
        st.subheader("🎤 Your Artist Dashboard")
        st.success("Your IPO: 1200/2000 shares sold")

elif page == "Upload IPO":
    if role == "Artist":
        st.subheader("🎶 Launch New IPO")
        st.text_input("Song Title")
        st.number_input("Total Shares", 100, 100000, step=100)
        st.file_uploader("Upload Cover Art")
        st.button("Release IPO")

elif page == "Search":
    st.subheader("🔍 Search Songs / Artists")
    st.text_input("Type to search...")

st.caption("Project X Alpha – Demo build")
