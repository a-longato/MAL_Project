import streamlit as st
from api import get_predictions

st.title("Temperature Predictions")

data = get_predictions()
st.line_chart({"Real": data["real"], "Predicted": data["predicted"]})
