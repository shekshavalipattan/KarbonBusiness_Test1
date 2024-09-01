from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained sentiment analysis model
try:
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except ImportError as e:
    sentiment_analyzer = None
    print(f"Error loading model: ImportError - {str(e)}")
except Exception as e:
    sentiment_analyzer = None
    print(f"Error loading model: {str(e)}")

# Define route for sentiment analysis
@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    if not sentiment_analyzer:
        return jsonify({"error": "Sentiment analysis model could not be loaded due to an ImportError or other error."}), 500

    try:
        # Get the review text from the request
        review_data = request.get_json()
        if not review_data or 'review_text' not in review_data:
            return jsonify({"error": "Invalid input, 'review_text' is required"}), 400

        review_text = review_data['review_text']

        # Perform sentiment analysis
        result = sentiment_analyzer(review_text)[0]

        # Prepare response
        response = {
            "review_text": review_text,
            "sentiment": result['label'].lower(),  # Convert to lowercase for consistency
            "confidence": result['score']
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
