import pandas as pd
import numpy as np


# Show all columns (instead of cascading columns in the middle)
pd.set_option("display.max_columns", None)
# Don't show numbers in scientific notation
pd.set_option("display.float_format", "{:.2f}".format)

df_list = pd.read_pickle("listings_project.pkl")
df_cal = pd.read_parquet("calendar_project.parquet", engine="pyarrow")

# print(df_list.discount_per_5_days_booked)

df_list["discount_per_5_days_booked"] = (
    df_list["discount_per_5_days_booked"]
    .str.replace("%", "", regex=True)
    .str.replace(",", "")
    .astype(float)
) * 0.01
df_list["discount_per_10_days_booked"] = (
    df_list["discount_per_10_days_booked"]
    .str.replace("%", "", regex=True)
    .str.replace(",", "")
    .astype(float)
) * 0.01
df_list["discount_per_30_and_more_days_booked"] = (
    df_list["discount_per_30_and_more_days_booked"]
    .str.replace("%", "", regex=True)
    .str.replace(",", "")
    .astype(float)
) * 0.01

# testing
# test = df_list.host_is_superhost.info()
# print(test)


df_list["has_availability"] = (
    df_list["has_availability"]
    .str.replace("t", "True")
    .str.replace("f", "False")
    .astype(bool)
)
df_list["instant_bookable"] = (
    df_list["instant_bookable"]
    .str.replace("t", "True")
    .str.replace("f", "False")
    .astype(bool)
)
df_list["host_is_superhost"] = (
    df_list["host_is_superhost"]
    .str.replace("t", "True")
    .str.replace("f", "False")
    .astype(bool)
)

# print(df_list[["host_is_superhost", "instant_bookable", "has_availability"]].head(5))


df_list["price"] = (
    df_list["price"]
    .str.replace(r"\$", "", regex=True)
    .str.replace(",", "", regex=True)
    .astype(float)
)
df_list["price_per_person"] = (
    df_list["price_per_person"]
    .str.replace(r"\$", "", regex=True)
    .str.replace(",", "", regex=True)
    .astype(float)
)
df_list["minimum_price"] = (
    df_list["minimum_price"]
    .str.replace(r"\$", "", regex=True)
    .str.replace(",", "", regex=True)
    .astype(float)
)
df_list["service_cost"] = (
    df_list["service_cost"]
    .str.replace(r"\$", "", regex=True)
    .str.replace(",", "", regex=True)
    .astype(float)
)
temp_price = df_list[
    ["price", "price_per_person", "minimum_price", "service_cost"]
].head(5)

# print(temp_price.head(5))

df_list = df_list.rename(
    columns={"price": "price_in_dollar", "neighbourhood_cleansed": "neighbourhood"}
)

df_list = df_list.astype({"neighbourhood": "category", "room_type": "category"})

# for col in ["neighbourhood", "room_type"]:
#     df_list[col] = df_list[col].astype("category")

df_list = df_list.drop(
    columns=[
        "host_listings_count",
        "host_total_listings_count",
        "availability_60",
        "availability_90",
        "availability_365",
        "number_of_reviews",
        "number_of_reviews_ltm",
        "reviews_per_month",
    ]
)

df_list = df_list.drop(columns=["price_in_euros"])

df_list = df_list.dropna(subset=["review_scores_rating", "host_acceptance_rate"])

# print(df_list.info(verbose=True, show_counts=True))
# print(df_list.info(verbose=True, show_counts=True))

# print(df_list.room_type.unique())


def fill_empty_bedrooms(accommodations: int, bedrooms: int, room_type: str) -> int:
    if (room_type == "Shared room") or (room_type == "Private room"):
        return 1
    elif (room_type == "Entire home/apt") or (room_type == "Hotel room"):
        return np.ceil(accommodations / 2)
    else:
        return bedrooms


# deep copy the df

temp_df = df_list.copy()
temp_df["rooms"] = df_list[["accommodates", "bedrooms", "room_type"]].apply(
    lambda x: fill_empty_bedrooms(x["accommodates"], x["bedrooms"], x["room_type"]),
    axis=1,
)

df_list["bedrooms"] = df_list[["accommodates", "bedrooms", "room_type"]].apply(
    lambda x: fill_empty_bedrooms(x["accommodates"], x["bedrooms"], x["room_type"]),
    axis=1,
)
print(df_list.info(verbose=True, show_counts=True))
