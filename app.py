
import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Nail Polish Recommender",
    page_icon="💅",
    layout="centered"
)

st.title("💅 Dress Color to Nail Polish Recommender")
st.write(
    "Select your dress color, dress style, and occasion "
    "to discover matching nail polish shades."
)

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "nail_polish_decision_tree.pkl"
)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

try:
    saved_data = load_model()
    model = saved_data["model"]
    encoders = saved_data["feature_encoders"]
    target_encoder = saved_data["target_encoder"]

except FileNotFoundError:
    st.error(
        "Model file not found. Please upload "
        "nail_polish_decision_tree.pkl to your repository."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()

# -----------------------------------
# NAIL POLISH SHADE SUGGESTIONS
# -----------------------------------

nail_polish = {
    "Black": ["Nude", "Red", "Silver", "Burgundy", "Gold"],
    "White": ["Baby Pink", "Red", "Nude", "Lavender", "French Manicure"],
    "Pink": ["White", "Nude", "Rose Gold", "Mauve", "Burgundy"],
    "Red": ["Nude", "Black", "Gold", "Burgundy", "Milky White"],
    "Blue": ["Nude", "Silver", "Baby Pink", "White", "Lavender"],
    "Purple": ["Nude", "Pink", "Silver", "Mauve", "White"],
    "Green": ["Nude", "Gold", "Cream", "Brown", "Burgundy"],
    "Yellow": ["White", "Nude", "Coral", "Brown", "Baby Pink"],
    "Brown": ["Beige", "Nude", "Gold", "Cream", "Terracotta"],
    "Beige": ["Brown", "White", "Rose Gold", "Mauve", "Red"],
    "Maroon": ["Nude", "Gold", "Cream", "Pink", "Burgundy"],
    "Navy Blue": ["Silver", "Nude", "White", "Gold", "Baby Pink"],
    "Lavender": ["White", "Nude", "Lilac", "Baby Pink", "Silver"],
    "Peach": ["White", "Coral", "Nude", "Rose Gold", "Pink"],
    "Grey": ["Pink", "Red", "Silver", "Nude", "Burgundy"]
}

# -----------------------------------
# USER INPUT
# -----------------------------------

st.subheader("Choose Your Dress Details")

dress_color = st.selectbox(
    "Select Dress Color",
    options=list(encoders["Dress_Color"].classes_)
)

dress_style = st.selectbox(
    "Select Dress Style",
    options=list(encoders["Dress_Style"].classes_)
)

occasion = st.selectbox(
    "Select Occasion",
    options=list(encoders["Occasion"].classes_)
)

# -----------------------------------
# PREDICT NAIL POLISH SHADE
# -----------------------------------

if st.button("Recommend Nail Polish 💅", type="primary"):

    try:
        color_encoded = encoders["Dress_Color"].transform(
            [dress_color]
        )[0]

        style_encoded = encoders["Dress_Style"].transform(
            [dress_style]
        )[0]

        occasion_encoded = encoders["Occasion"].transform(
            [occasion]
        )[0]

        input_data = pd.DataFrame(
            [[color_encoded, style_encoded, occasion_encoded]],
            columns=["Dress_Color", "Dress_Style", "Occasion"]
        )

        prediction = model.predict(input_data)
        predicted_shade = target_encoder.inverse_transform(
            prediction
        )[0]

        st.success("Your nail polish recommendation is ready!")

        st.subheader("🤖 Decision Tree Prediction")
        st.write(f"**Recommended Shade:** {predicted_shade}")

        st.divider()

        st.subheader("💖 More Matching Shades")

        matching_shades = nail_polish.get(
            dress_color,
            [predicted_shade]
        )

        # Show the model prediction first
        all_shades = list(
            dict.fromkeys([predicted_shade] + matching_shades)
        )

        for index, shade in enumerate(all_shades, start=1):
            st.write(f"{index}. 💅 {shade}")

        st.caption(
            "The Decision Tree predicts one shade. "
            "The additional shades come from predefined color-matching rules."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()
st.caption("Dress Color to Nail Polish Recommendation System")
st.caption("Built with Python, Scikit-learn and Streamlit.")

import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Nail Polish Recommender",
    page_icon="💅",
    layout="centered"
)

st.title("💅 Dress Color to Nail Polish Recommender")
st.write(
    "Select your dress color, dress style, and occasion "
    "to discover matching nail polish shades."
)

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "nail_polish_decision_tree.pkl"
)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

try:
    saved_data = load_model()
    model = saved_data["model"]
    encoders = saved_data["feature_encoders"]
    target_encoder = saved_data["target_encoder"]

except FileNotFoundError:
    st.error(
        "Model file not found. Please upload "
        "nail_polish_decision_tree.pkl to your repository."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()

# -----------------------------------
# NAIL POLISH SHADE SUGGESTIONS
# -----------------------------------

nail_polish = {
    "Black": ["Nude", "Red", "Silver", "Burgundy", "Gold"],
    "White": ["Baby Pink", "Red", "Nude", "Lavender", "French Manicure"],
    "Pink": ["White", "Nude", "Rose Gold", "Mauve", "Burgundy"],
    "Red": ["Nude", "Black", "Gold", "Burgundy", "Milky White"],
    "Blue": ["Nude", "Silver", "Baby Pink", "White", "Lavender"],
    "Purple": ["Nude", "Pink", "Silver", "Mauve", "White"],
    "Green": ["Nude", "Gold", "Cream", "Brown", "Burgundy"],
    "Yellow": ["White", "Nude", "Coral", "Brown", "Baby Pink"],
    "Brown": ["Beige", "Nude", "Gold", "Cream", "Terracotta"],
    "Beige": ["Brown", "White", "Rose Gold", "Mauve", "Red"],
    "Maroon": ["Nude", "Gold", "Cream", "Pink", "Burgundy"],
    "Navy Blue": ["Silver", "Nude", "White", "Gold", "Baby Pink"],
    "Lavender": ["White", "Nude", "Lilac", "Baby Pink", "Silver"],
    "Peach": ["White", "Coral", "Nude", "Rose Gold", "Pink"],
    "Grey": ["Pink", "Red", "Silver", "Nude", "Burgundy"]
}

# -----------------------------------
# USER INPUT
# -----------------------------------

st.subheader("Choose Your Dress Details")

dress_color = st.selectbox(
    "Select Dress Color",
    options=list(encoders["Dress_Color"].classes_)
)

dress_style = st.selectbox(
    "Select Dress Style",
    options=list(encoders["Dress_Style"].classes_)
)

occasion = st.selectbox(
    "Select Occasion",
    options=list(encoders["Occasion"].classes_)
)

# -----------------------------------
# PREDICT NAIL POLISH SHADE
# -----------------------------------

if st.button("Recommend Nail Polish 💅", type="primary"):

    try:
        color_encoded = encoders["Dress_Color"].transform(
            [dress_color]
        )[0]

        style_encoded = encoders["Dress_Style"].transform(
            [dress_style]
        )[0]

        occasion_encoded = encoders["Occasion"].transform(
            [occasion]
        )[0]

        input_data = pd.DataFrame(
            [[color_encoded, style_encoded, occasion_encoded]],
            columns=["Dress_Color", "Dress_Style", "Occasion"]
        )

        prediction = model.predict(input_data)
        predicted_shade = target_encoder.inverse_transform(
            prediction
        )[0]

        st.success("Your nail polish recommendation is ready!")

        st.subheader("🤖 Decision Tree Prediction")
        st.write(f"**Recommended Shade:** {predicted_shade}")

        st.divider()

        st.subheader("💖 More Matching Shades")

        matching_shades = nail_polish.get(
            dress_color,
            [predicted_shade]
        )

        # Show the model prediction first
        all_shades = list(
            dict.fromkeys([predicted_shade] + matching_shades)
        )

        for index, shade in enumerate(all_shades, start=1):
            st.write(f"{index}. 💅 {shade}")

        st.caption(
            "The Decision Tree predicts one shade. "
            "The additional shades come from predefined color-matching rules."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()
st.caption("Dress Color to Nail Polish Recommendation System")
st.caption("Built with Python, Scikit-learn and Streamlit.")

import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Nail Polish Recommender",
    page_icon="💅",
    layout="centered"
)

st.title("💅 Dress Color to Nail Polish Recommender")
st.write(
    "Select your dress color, dress style, and occasion "
    "to discover matching nail polish shades."
)

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "nail_polish_decision_tree.pkl"
)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

try:
    saved_data = load_model()
    model = saved_data["model"]
    encoders = saved_data["feature_encoders"]
    target_encoder = saved_data["target_encoder"]

except FileNotFoundError:
    st.error(
        "Model file not found. Please upload "
        "nail_polish_decision_tree.pkl to your repository."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()

# -----------------------------------
# NAIL POLISH SHADE SUGGESTIONS
# -----------------------------------

nail_polish = {
    "Black": ["Nude", "Red", "Silver", "Burgundy", "Gold"],
    "White": ["Baby Pink", "Red", "Nude", "Lavender", "French Manicure"],
    "Pink": ["White", "Nude", "Rose Gold", "Mauve", "Burgundy"],
    "Red": ["Nude", "Black", "Gold", "Burgundy", "Milky White"],
    "Blue": ["Nude", "Silver", "Baby Pink", "White", "Lavender"],
    "Purple": ["Nude", "Pink", "Silver", "Mauve", "White"],
    "Green": ["Nude", "Gold", "Cream", "Brown", "Burgundy"],
    "Yellow": ["White", "Nude", "Coral", "Brown", "Baby Pink"],
    "Brown": ["Beige", "Nude", "Gold", "Cream", "Terracotta"],
    "Beige": ["Brown", "White", "Rose Gold", "Mauve", "Red"],
    "Maroon": ["Nude", "Gold", "Cream", "Pink", "Burgundy"],
    "Navy Blue": ["Silver", "Nude", "White", "Gold", "Baby Pink"],
    "Lavender": ["White", "Nude", "Lilac", "Baby Pink", "Silver"],
    "Peach": ["White", "Coral", "Nude", "Rose Gold", "Pink"],
    "Grey": ["Pink", "Red", "Silver", "Nude", "Burgundy"]
}

# -----------------------------------
# USER INPUT
# -----------------------------------

st.subheader("Choose Your Dress Details")

dress_color = st.selectbox(
    "Select Dress Color",
    options=list(encoders["Dress_Color"].classes_)
)

dress_style = st.selectbox(
    "Select Dress Style",
    options=list(encoders["Dress_Style"].classes_)
)

occasion = st.selectbox(
    "Select Occasion",
    options=list(encoders["Occasion"].classes_)
)

# -----------------------------------
# PREDICT NAIL POLISH SHADE
# -----------------------------------

if st.button("Recommend Nail Polish 💅", type="primary"):

    try:
        color_encoded = encoders["Dress_Color"].transform(
            [dress_color]
        )[0]

        style_encoded = encoders["Dress_Style"].transform(
            [dress_style]
        )[0]

        occasion_encoded = encoders["Occasion"].transform(
            [occasion]
        )[0]

        input_data = pd.DataFrame(
            [[color_encoded, style_encoded, occasion_encoded]],
            columns=["Dress_Color", "Dress_Style", "Occasion"]
        )

        prediction = model.predict(input_data)
        predicted_shade = target_encoder.inverse_transform(
            prediction
        )[0]

        st.success("Your nail polish recommendation is ready!")

        st.subheader("🤖 Decision Tree Prediction")
        st.write(f"**Recommended Shade:** {predicted_shade}")

        st.divider()

        st.subheader("💖 More Matching Shades")

        matching_shades = nail_polish.get(
            dress_color,
            [predicted_shade]
        )

        # Show the model prediction first
        all_shades = list(
            dict.fromkeys([predicted_shade] + matching_shades)
        )

        for index, shade in enumerate(all_shades, start=1):
            st.write(f"{index}. 💅 {shade}")

        st.caption(
            "The Decision Tree predicts one shade. "
            "The additional shades come from predefined color-matching rules."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()
st.caption("Dress Color to Nail Polish Recommendation System")
st.caption("Built with Python, Scikit-learn and Streamlit.")

import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Nail Polish Recommender",
    page_icon="💅",
    layout="centered"
)

st.title("💅 Dress Color to Nail Polish Recommender")
st.write(
    "Select your dress color, dress style, and occasion "
    "to discover matching nail polish shades."
)

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "nail_polish_decision_tree.pkl"
)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

try:
    saved_data = load_model()
    model = saved_data["model"]
    encoders = saved_data["feature_encoders"]
    target_encoder = saved_data["target_encoder"]

except FileNotFoundError:
    st.error(
        "Model file not found. Please upload "
        "nail_polish_decision_tree.pkl to your repository."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()

# -----------------------------------
# NAIL POLISH SHADE SUGGESTIONS
# -----------------------------------

nail_polish = {
    "Black": ["Nude", "Red", "Silver", "Burgundy", "Gold"],
    "White": ["Baby Pink", "Red", "Nude", "Lavender", "French Manicure"],
    "Pink": ["White", "Nude", "Rose Gold", "Mauve", "Burgundy"],
    "Red": ["Nude", "Black", "Gold", "Burgundy", "Milky White"],
    "Blue": ["Nude", "Silver", "Baby Pink", "White", "Lavender"],
    "Purple": ["Nude", "Pink", "Silver", "Mauve", "White"],
    "Green": ["Nude", "Gold", "Cream", "Brown", "Burgundy"],
    "Yellow": ["White", "Nude", "Coral", "Brown", "Baby Pink"],
    "Brown": ["Beige", "Nude", "Gold", "Cream", "Terracotta"],
    "Beige": ["Brown", "White", "Rose Gold", "Mauve", "Red"],
    "Maroon": ["Nude", "Gold", "Cream", "Pink", "Burgundy"],
    "Navy Blue": ["Silver", "Nude", "White", "Gold", "Baby Pink"],
    "Lavender": ["White", "Nude", "Lilac", "Baby Pink", "Silver"],
    "Peach": ["White", "Coral", "Nude", "Rose Gold", "Pink"],
    "Grey": ["Pink", "Red", "Silver", "Nude", "Burgundy"]
}

# -----------------------------------
# USER INPUT
# -----------------------------------

st.subheader("Choose Your Dress Details")

dress_color = st.selectbox(
    "Select Dress Color",
    options=list(encoders["Dress_Color"].classes_)
)

dress_style = st.selectbox(
    "Select Dress Style",
    options=list(encoders["Dress_Style"].classes_)
)

occasion = st.selectbox(
    "Select Occasion",
    options=list(encoders["Occasion"].classes_)
)

# -----------------------------------
# PREDICT NAIL POLISH SHADE
# -----------------------------------

if st.button("Recommend Nail Polish 💅", type="primary"):

    try:
        color_encoded = encoders["Dress_Color"].transform(
            [dress_color]
        )[0]

        style_encoded = encoders["Dress_Style"].transform(
            [dress_style]
        )[0]

        occasion_encoded = encoders["Occasion"].transform(
            [occasion]
        )[0]

        input_data = pd.DataFrame(
            [[color_encoded, style_encoded, occasion_encoded]],
            columns=["Dress_Color", "Dress_Style", "Occasion"]
        )

        prediction = model.predict(input_data)
        predicted_shade = target_encoder.inverse_transform(
            prediction
        )[0]

        st.success("Your nail polish recommendation is ready!")

        st.subheader("🤖 Decision Tree Prediction")
        st.write(f"**Recommended Shade:** {predicted_shade}")

        st.divider()

        st.subheader("💖 More Matching Shades")

        matching_shades = nail_polish.get(
            dress_color,
            [predicted_shade]
        )

        # Show the model prediction first
        all_shades = list(
            dict.fromkeys([predicted_shade] + matching_shades)
        )

        for index, shade in enumerate(all_shades, start=1):
            st.write(f"{index}. 💅 {shade}")

        st.caption(
            "The Decision Tree predicts one shade. "
            "The additional shades come from predefined color-matching rules."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()
st.caption("Dress Color to Nail Polish Recommendation System")
st.caption("Built with Python, Scikit-learn and Streamlit.")
