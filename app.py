from flask import Flask, request, jsonify
from flask_cors import CORS
from test_url import test_url

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/api/check-url", methods=["POST"])
def check_url():
    print("Received POST request")
    try:
        data = request.get_json()
        if not data or "url" not in data:
            return jsonify({"error": "No URL provided", "status": "error"}), 400

        url = data["url"]
        result = test_url(url)
        if result is None:
            return jsonify({"error": "Error processing URL", "status": "error"}), 500

        message, confidence = result.split("(Confidence:")
        message = message.strip()
        confidence = confidence.strip().rstrip(")")

        # Determine if phishing based on the message content
        is_phishing = "phishing" in message.lower()

        response = jsonify(
            {
                "message": message,
                "confidence": confidence,
                "status": "success",
                "is_phishing": is_phishing,
            }
        )

        print("Response:", response.json)

        return response

    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500


@app.route("/", methods=["GET"])
def home():
    return """
    <html>
        <head>
            <title>Phishing URL Detection API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .container {
                    background-color: #f5f5f5;
                    padding: 20px;
                    border-radius: 5px;
                }
                pre {
                    background-color: #eee;
                    padding: 10px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Phishing URL Detection API</h1>
                <p>This API provides URL phishing detection capabilities.</p>
                
                <h2>API Usage</h2>
                <p>Send a POST request to <code>/api/check-url</code> with the following JSON body:</p>
                <pre>
{
    "url": "https://example.com"
}
                </pre>
                
                <h2>Example Response</h2>
                <pre>
{
    'confidence': '61.3%', 
    'is_phishing': False, 
    'message': 'This website appears to be legitimate.', 
    'status': 'success'
}
                </pre>
            </div>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
