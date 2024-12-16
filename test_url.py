import pickle
from URLFeatureExtraction import featureExtraction
import pandas as pd
import requests


def is_url_accessible(url):
    try:
        response = requests.head(url, timeout=5)
        return True
    except:
        return False


def test_url(url):
    try:
        # First check if URL is accessible
        if not is_url_accessible(url):
            print(f"Warning: Could not access {url}")
            print("This might be due to:")
            print("1. The website is down")
            print("2. No internet connection")
            print("3. The URL is incorrect")
            print("\nProceeding with analysis based on URL structure only...")

        # Load the XGBoost model
        try:
            model = pickle.load(open("XGBoostClassifier.pickle.dat", "rb"))
        except Exception as e:
            print(
                "Error loading the model. Please ensure you have the correct model file."
            )
            print("Technical details:", str(e))
            return None

        try:
            # Extract features from the URL
            features = featureExtraction(url)

            # Convert features to DataFrame
            feature_names = [
                "Domain",
                "Have_IP",
                "Have_At",
                "URL_Length",
                "URL_Depth",
                "Redirection",
                "https_Domain",
                "TinyURL",
                "Prefix/Suffix",
            ]

            df = pd.DataFrame([features], columns=feature_names)

            # Get prediction and probability
            prediction = model.predict(df)[0]
            probability = model.predict_proba(df)[0]

            # Get the confidence percentage
            confidence = probability[1] if prediction == 1 else probability[0]
            confidence_pct = confidence * 100

            print("prediction:", prediction)

            if prediction == 1:
                return f"Warning: This website might be a phishing website! (Confidence: {confidence_pct:.1f}%)"
            else:
                return f"This website appears to be legitimate. (Confidence: {confidence_pct:.1f}%)"
        except Exception as e:
            print(f"Error processing URL: {str(e)}")
            return None

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None
