import streamlit as st
from utils.data_loader import load_data
from utils.preprocess import clean_data
from utils.data_profile  import get_data_sum



st.set_page_config(
    page_title = "FoodSense",
    page_icon = "🍽",
    layout = "wide"

)
df = load_data("data/zomato_dataset.csv")
df = clean_data(df)
summary = get_data_sum(df)
#st.write(summary)
#st.write(df[["name","rate","location","cuisines"]].head())


# creating overview of restaurants in metrics way for brtter buisness kinda analysis

st.subheader("📊 Restaurant Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        "Total Restaurants",
        summary["total_restaurants"]
    )

with metric2:
    st.metric(
        "Cities Covered",
        summary["total_cities"]
    )

with metric3:
    st.metric(
        "Cuisines Available",
        summary["total_cuisines"]
    )

with metric4:
    st.metric(
        "Average Rating",
        summary["average_rating"]
    ) 
    #code for getting most popular cuisines in the visualization form

st.subheader("🍽️ Most Popular Cuisines 🍽️ ")
cuisine_counts = (df["cuisines"]
    .value_counts()
    .head(10))
st.bar_chart(cuisine_counts)



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