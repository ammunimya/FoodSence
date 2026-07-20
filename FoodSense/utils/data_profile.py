def get_data_sum(df):

    summary = {
        "total_restaurants": len(df),
        "total_cities": df["location"].nunique(),
        "total_cuisines": df["cuisines"].nunique(),
        "average_rating": round(df["rate"].mean(), 2)
    }

    return summary