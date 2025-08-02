from flask import Flask, request, jsonify
import google.generativeai as genai

# 👉 Directly set your API key here
API_KEY = "AIzaSyAFPFhppLy24xFolIyQNnTH8kahJM7kCfA"

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')


# Initialize Flask app
app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    try:
        response = model.generate_content(prompt)
        story = response.text
        return jsonify({"story": story})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
