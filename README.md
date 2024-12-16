# Phishing Website Detection by Machine Learning Techniques

This project is designed to detect phishing websites using a combination of URL-based feature extraction and machine learning classification. By examining various characteristics of a given URL—such as the presence of special characters, domain age, and URL length—the trained model distinguishes between legitimate and malicious (phishing) websites.

## Key Features

The following features are extracted from each URL to inform the classification model:

- **Domain of URL**: Extracts the domain name from the URL.
- **IP Address in URL**: Checks if the URL contains an IP address instead of a domain name.
- **"@" Symbol in URL**: Identifies the presence of the "@" symbol.
- **Length of URL**: Measures the total length of the URL.
- **Depth of URL**: Counts the number of subdirectories in the URL path.
- **Redirection "//" in URL**: Detects multiple occurrences of "//" which may indicate suspicious redirects.
- **"http/https" in Domain Name**: Checks if the domain name contains "http" or "https".
- **URL Shortening Services**: Identifies the use of known URL shorteners (e.g., TinyURL, bit.ly).
- **Prefix or Suffix "-" in Domain**: Detects suspicious hyphen usage in the domain.
- **Age of Domain**: Determines the domain’s age (older domains are often more trustworthy).
- **End Period of Domain**: Examines the domain’s expiration period.

## Getting Started

### Prerequisites

- **Python 3.6 or higher**
- **virtualenv** (optional but recommended for environment isolation)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/guardio-extension/website-phishing-detector-api.git
   cd website-phishing-detector-api
   ```

2. **Create a virtual environment (optional):**
   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Project

- **Feature Extraction:**
  ```sh
  python URLFeatureExtraction.py
  ```
  
- **Model Training:**
  ```sh
  python train_model.py
  ```

- **Testing URLs:**
  ```sh
  python test_url.py
  ```

- **Main Application to run API:**
  ```sh
  python app.py
  ```

## Project Structure

```
Phishing-Website-Detection-by-Machine-Learning-Techniques/
│
├─ app.py                         # Main application file
├─ train_model.py                 # Script to train the machine learning model
├─ test_url.py                    # Script to test URLs against the trained model
├─ URLFeatureExtraction.py        # Script for feature extraction from URLs
├─ URL Feature Extraction.ipynb   # Jupyter notebook for URL feature extraction analysis
│
├─ DataFiles/                     # Directory containing data files (datasets, etc.)
│   └─ ...
│
├─ requirements.txt               # Project dependencies
└─ LICENSE                        # License file
```

## Dataset and Sources

This project uses publicly available datasets:

- **PhishTank**: [PhishTank Developer Info](https://www.phishtank.com/developer_info.php)
- **URL Dataset (UNB)**: [University of New Brunswick’s URL dataset](https://www.unb.ca/cic/datasets/url-2016.html)

## Contributing

Contributions are welcome! If you find any issues or have ideas for enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
