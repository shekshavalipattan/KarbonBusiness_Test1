import json
import requests

# Define the Flask API endpoint
API_URL = "http://127.0.0.1:5000/analyze-sentiment"

# Load the JSON data from the uploaded file
with open('Q3.Input_data_set.json', 'r') as file:
    reviews = json.load(file)

# Iterate through each review and send a POST request to the API
for review in reviews:
    # Prepare the payload
    payload = {"review_text": review["review_text"]}

    # Send POST request to the API
    response = requests.post(API_URL, json=payload)

    # Print the full API response to check for errors
    print("Full API Response:", response.json())  # Added this line

    # Get the API response
    result = response.json()

    # Print the original review and the predicted sentiment
    print(f"Review ID: {review['review_id']}")
    print(f"Product ID: {review['product_id']}")
    print(f"Original Review: {review['review_text']}")
    print(f"Expected Sentiment: {review['expected_sentiment']}")

    # Check if 'sentiment' key exists in the response
    if 'sentiment' in result:
        print(f"Predicted Sentiment: {result['sentiment']}")
        print(f"Confidence Score: {result['confidence']:.2f}")
    else:
        print("Error: 'sentiment' key not found in the response")

    print("-" * 50)
