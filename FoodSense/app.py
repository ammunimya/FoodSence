import streamlit as st

st.set_page_config(
    page_title = "FoodSense",
    page_icon = "🍽",
    layout = "wide"

)

st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

.big-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#E23744;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

st.divider()

col1,col2=st.columns(2)

with col1:

    city=st.selectbox(
        "Select City",
        [
            "Bangalore",
            "Delhi",
            "Mumbai",
            "Hyderabad",
            "Chennai"
        ]
    )

    cuisine=st.selectbox(
        "Cuisine",
        [
            "North Indian",
            "Chinese",
            "Italian",
            "Cafe",
            "South Indian"
        ]
    )

with col2:

    budget=st.slider(
        "Budget (₹)",
        100,
        3000,
        1000
    )

    rating=st.slider(
        "Minimum Rating",
        1.0,
        5.0,
        4.0
    )

st.write("")

if st.button("🍕 Recommend Restaurants",use_container_width=True):

    st.success("Recommendation Engine will be connected in the next step.")

st.divider()

st.subheader("✨ Features")

col1,col2,col3=st.columns(3)

with col1:
    st.info("🤖 AI Recommendation")

with col2:
    st.info("📊 Analytics Dashboard")

with col3:
    st.info("📍 Interactive Maps")