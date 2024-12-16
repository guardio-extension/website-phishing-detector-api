# Phishing Website Detection by Machine Learning Techniques

This project aims to detect phishing websites using machine learning techniques. It extracts various features from URLs and uses them to train a machine learning model to classify URLs as either legitimate or phishing.

## Features Extracted

The project extracts the following features from URLs:

- Domain of URL
- IP Address in URL
- "@" Symbol in URL
- Length of URL
- Depth of URL
- Redirection "//" in URL
- "http/https" in Domain name
- Using URL Shortening Services (e.g., TinyURL)
- Prefix or Suffix "-" in Domain
- Age of Domain
- End Period of Domain

## Installation

### Prerequisites

- Python 3.6 or higher
- `virtualenv` package

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Phishing-Website-Detection-by-Machine-Learning-Techniques.git
   cd Phishing-Website-Detection-by-Machine-Learning-Techniques
   ```

2. **Create a virtual environment:**

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

4. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the project:**
   - You can run the feature extraction script using:
     ```sh
     python URLFeatureExtraction.py
     ```

## Project Structure

-

app.py

: Main application file.

-

DataFiles

: Directory containing data files used in the project.

-

requirements.txt

: List of dependencies required for the project.

-

test_url.py

: Script for testing URLs.

-

train_model.py

: Script for training the machine learning model.

- `URL Feature Extraction.ipynb`: Jupyter notebook for URL feature extraction.
-

URLFeatureExtraction.py

: Script for extracting features from URLs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- The dataset used in this project is sourced from [PhishTank](https://www.phishtank.com/developer_info.php) and the University of New Brunswick's [URL dataset](https://www.unb.ca/cic/datasets/url-2016.html).

Feel free to contribute to this project by submitting issues or pull requests.
