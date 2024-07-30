import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://user:password@localhost:5432/seismic_data')

# Load data from PostgreSQL
seismic_data = pd.read_sql('seismic_data', engine)

# Feature extraction
X = seismic_data[['latitude', 'longitude', 'depth', 'mag']]
y = (seismic_data['mag'] >= 5).astype(int)  # Binary classification: significant earthquake or not

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/seismic_activity_prediction_model.pkl')
