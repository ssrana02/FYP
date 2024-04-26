import re
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Loading the dataset
dataset = pd.read_csv('D:/Education/PYTHON/ML-v2/Datasets/malicious_phish.csv')

# Extracting domain-based features
dataset['domain_length'] = dataset['url'].apply(lambda x: len(re.findall('/.', x)))
dataset['subdomains'] = dataset['url'].apply(lambda x: x.count('.') - 1)
dataset['has_ip'] = dataset['url'].apply(lambda x: 1 if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', x) else 0)

# Extracting path-based features
dataset['path_length'] = dataset['url'].apply(lambda x: len(re.findall('/', x)))
dataset['path_depth'] = dataset['url'].apply(lambda x: x.count('/'))

# Extracting character-based features
special_characters = '@/%/$/=/./_/?/:/~/'
dataset['special_chars_count'] = dataset['url'].apply(lambda x: sum(x.count(char) for char in special_characters))

# Combine features
X = dataset[['domain_length', 'subdomains', 'has_ip', 'path_length', 'path_depth', 'special_chars_count']].values

# Splitting the dataset into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Initialize the Isolation Forest model
isolation_forest = IsolationForest(contamination=0.1, random_state=42)

# Fit the model
isolation_forest.fit(X_train)

# Predictions on the testing set
y_pred = isolation_forest.predict(X_test)

# Evaluation
print("Number of anomalies detected:", len(y_pred[y_pred == -1]))




# Function to preprocess and extract features from a URL
def extract_features(url):
    domain_length = len(re.findall('/.', url))
    subdomains = url.count('.') - 1
    has_ip = 1 if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', url) else 0
    path_length = len(re.findall('/', url))
    path_depth = url.count('/')
    special_characters = '@/%/$/=/./_/?/:/~/'
    special_chars_count = sum(url.count(char) for char in special_characters)
    
    return [domain_length, subdomains, has_ip, path_length, path_depth, special_chars_count]

# URL to test
new_url = "https://certificate.doenets.lk/"

# Extract features from the new URL
new_url_features = extract_features(new_url)

# Transform features into the same format as the training data
new_url_features_array = np.array(new_url_features).reshape(1, -1)
#new commnet
# Predict anomaly
is_anomaly = isolation_forest.predict(new_url_features_array)

if is_anomaly == -1:
    print("The URL is detected as an anomaly.")
else:
    print("The URL is not detected as an anomaly.")
