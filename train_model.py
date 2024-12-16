import pandas as pd
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from URLFeatureExtraction import featureExtraction
from urllib.parse import urlparse

# Load and process the dataset
df = pd.read_csv("DataFiles/5.urldata.csv")

# Extract features for each URL in the dataset
features_list = []
labels = []

print("Processing URLs...")
for index, row in df.iterrows():
    url = f"http://{row['Domain']}"  # Add protocol to make it a valid URL
    label = row["Label"]
    features = featureExtraction(url)
    if features is not None:  # Only add if feature extraction was successful
        features_list.append(features)
        labels.append(label)
    if (index + 1) % 100 == 0:
        print(f"Processed {index + 1} URLs")

# Convert to DataFrame
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

X = pd.DataFrame(features_list, columns=feature_names)
y = pd.Series(labels)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining model...")
# Train XGBoost model
model = xgb.XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
print("Saving model...")
with open("XGBoostClassifier.pickle.dat", "wb") as f:
    pickle.dump(model, f)

# Print accuracy
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"\nTraining accuracy: {train_accuracy:.4f}")
print(f"Testing accuracy: {test_accuracy:.4f}")
