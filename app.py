import streamlit as st
import pandas as pd
import pickle

# Load files
model = pickle.load(open("xg_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))
default_house = pickle.load(open("default_house.pkl", "rb"))
col1, col2 = st.columns([4, 1])

with col1:
    st.title("House Price Prediction")

with col2:
    st.image("https://images.pexels.com/photos/20296321/pexels-photo-20296321.jpeg", width=180)

st.divider()

st.link_button(
    "📂 GitHub Repository",
    "https://github.com/your-username/your-repo"
)

st.markdown("### How Does the Model Work?")
st.markdown("**This app uses a supervised machine learning regression model trained on historical housing data. The model learns patterns between property features and their sold prices, then generalizes that learning to predict prices for new inputs.**")
tab1, tab2 = st.tabs(
    ["Basic Mode", "Advanced Mode"]
)


with tab1:
    st.subheader("Basic House Predictor")
    overall_qual_basic=st.slider("Overall Quality", 1, 10,key="overall_qual_basic")
    gr_liv_area_basic=st.number_input("Living Area (sq ft)",value=1500,key="gr_liv_area_basic")
    garage_cars_basic=st.number_input("Garage Capacity",value=2,key="garage_cars_basic")
    total_bsmt_basic=st.number_input("Basement Area (sq ft)",value=800,key="total_bsmt_basic")
    year_built_basic=st.number_input("Year Built",value=2000,key="year_built_basic")
    lot_area_basic=st.number_input("Lot Area (sq ft)",value=8000,key="lot_area_basic")

    predict_basic=st.button("Predict Price",key="predict_basic")

with tab2:
    st.subheader("Advanced House Predictor")
    col1, col2= st.columns([1,1])


    with col1:

        overall_qual_adv = st.slider("Overall Quality", 1, 10, 5,key="overall_qual_adv")

        overall_cond_adv = st.slider("Overall Condition", 1, 10, 5,key="overall_cond_adv")

        gr_liv_area_adv = st.number_input("Living Area", value=1500,key="gr_liv_area_adv")

        first_floor_adv = st.number_input("1st Floor Area", value=1000,key="first_floor_adv")

        second_floor_adv = st.number_input("2nd Floor Area", value=500,key="second_floor_adv")

        total_bsmt_adv = st.number_input("Basement Area", value=800,key="total_bsmt_adv")

        lot_area_adv = st.number_input("Lot Area", value=8000,key="lot_area_adv")

        year_built_adv = st.number_input("Year Built", value=2000,key="year_built_adv")


    with col2:
        year_remod_adv = st.number_input("Year Remodeled", value=2005,key="year_remod_adv")

        garage_cars_adv = st.number_input("Garage Cars", value=2,key="garage_cars_adv")

        garage_area_adv = st.number_input("Garage Area", value=500,key="garage_area_adv")

        fireplaces_adv = st.number_input("Fireplaces", value=1,key="fireplaces_adv")

        full_bath_adv = st.number_input("Full Bathrooms", value=2,key="full_bath_adv")

        bedrooms_adv = st.number_input("Bedrooms", value=3,key="bedrooms_adv")

        neighbourhood_adv=st.selectbox("Neighbourhood",["NAmes",
                "CollgCr",
                "OldTown",
                "NridgHt",
                "Somerst"
        ])
        kitchen_qual_adv = st.selectbox("Kitchen Quality",["TA", "Gd", "Fa"])

    st.write("")
    predict_advanced=st.button("Predict Price",key="predict_adv")

house = pd.DataFrame(
    0,
    index=[0],
    columns=columns
)

for col in default_house.index:
    if col in house.columns:
        house[col] = default_house[col]

if predict_basic:

    house["OverallQual"] = overall_qual_basic
    house["GrLivArea"] = gr_liv_area_basic
    house["GarageCars"] = garage_cars_basic
    house["TotalBsmtSF"] = total_bsmt_basic
    house["YearBuilt"] = year_built_basic
    house["LotArea"] = lot_area_basic

    prediction = model.predict(house)

    st.success(
    f"🏠 Estimated House Price: ${prediction[0]:,.0f}")


if predict_advanced:

    house["OverallQual"] = overall_qual_adv
    house["OverallCond"] = overall_cond_adv
    house["GrLivArea"] = gr_liv_area_adv
    house["1stFlrSF"] = first_floor_adv
    house["2ndFlrSF"] = second_floor_adv
    house["TotalBsmtSF"] = total_bsmt_adv
    house["LotArea"] = lot_area_adv
    house["YearBuilt"] = year_built_adv
    house["YearRemodAdd"] = year_remod_adv
    house["GarageCars"] = garage_cars_adv
    house["GarageArea"] = garage_area_adv
    house["Fireplaces"] = fireplaces_adv
    house["FullBath"] = full_bath_adv
    house["BedroomAbvGr"] = bedrooms_adv

    # Neighborhood
    neigh_col = f"Neighborhood_{neighbourhood_adv}"
    if neigh_col in house.columns:
        house[neigh_col] = 1

    # Kitchen Quality
    kitchen_col = f"KitchenQual_{kitchen_qual_adv}"
    if kitchen_col in house.columns:
        house[kitchen_col] = 1

    prediction = model.predict(house)

    st.success(
    f"🏠 Estimated House Price: ${prediction[0]:,.0f}")