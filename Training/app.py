

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='D:/Education/PYTHON/ML-v2/Frontend/', static_folder='D:/Education/PYTHON/ML-v2/Frontend/static')


# Route for rendering the form
@app.route('/')
def index():
    return render_template('homepage.html')

# Route for handling form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get the URL input from the form
    url = request.form['url']

    # Preprocess and extract features from the URL
    url_features = extract_features(url)

    # Transform features into the same format as the training data
    url_features_array = np.array(url_features).reshape(1, -1)

    # Predict anomaly
    is_anomaly = isolation_forest.predict(url_features_array)

    if is_anomaly == -1:
        result = "The URL is detected as malicious."
    else:
        result = "The URL is detected as safe."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)



