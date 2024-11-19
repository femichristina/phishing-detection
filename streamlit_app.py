import streamlit as st
import joblib  # For loading your ML model
from feature import extract_features  # Assuming this is in feature.py
# Load the trained model
model = joblib.load('pickle/phishing_model.pkl')  # Update path if needed
# Streamlit app title and description
st.title("Phishing URL Detection")
st.markdown("**Enter a URL to check its legitimacy.**")
# Input field
url = st.text_input("Enter URL:", placeholder="e.g., http://example.com")
if st.button("Check URL"):
    try:
        # Extract features from the URL
        features = extract_features(url)
        
        # Predict using the model
        prediction = model.predict([features])[0]
        confidence = model.predict_proba([features]).max()

        # Display results
        if prediction == 1:
            st.error(f"The URL is likely **Phishing** (Confidence: {confidence:.2f})")
        else:
            st.success(f"The URL is likely **Legitimate** (Confidence: {confidence:.2f})")
    except Exception as e:
        st.error(f"An error occurred: {e}")
