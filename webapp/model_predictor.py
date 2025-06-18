import joblib
import numpy as np

# Load the saved pipeline and threshold
pipeline = joblib.load('logistic_pipeline.pkl')  # includes scaler + model
threshold = joblib.load('threshold.pkl')         # e.g., 0.25 or 0.3

def get_asteroid_risk_prediction(diameter_km, velocity_kmph, distance_km):
    """
    Predicts asteroid risk based on input features using trained pipeline.
    """
    try:
        diameter_km = float(diameter_km)
        velocity_kmph = float(velocity_kmph)
        distance_km = float(distance_km)
    except ValueError:
        return "Error: Invalid input types. Please provide numbers."
    except TypeError:
        return "Error: Missing input values."

    if distance_km == 0:
        return "Error: Distance cannot be zero."

    # 1. Calculate risk_score
    risk_score = (diameter_km * (velocity_kmph**2)) / distance_km

    # 2. Prepare features in correct format (must match training format!)
    input_features = np.array([[diameter_km, velocity_kmph, distance_km, risk_score]])

    # 3. Predict probability using trained pipeline
    y_proba = pipeline.predict_proba(input_features)[:, 1]  # Probability of being hazardous

    # 4. Apply custom threshold
    prediction = int(y_proba >= threshold)

    # 5. Return human-readable result
    return "High Risk" if prediction == 1 else "Low Risk"

# Example usage
if __name__ == '__main__':
    print(get_asteroid_risk_prediction(1, 60000, 1000000))       # High Risk
    print(get_asteroid_risk_prediction(0.01, 20000, 50000000))   # Low Risk
    print(get_asteroid_risk_prediction(0.5, 50000, 4000000))     # High Risk
    print(get_asteroid_risk_prediction("test", 50000, 4000000))  # Error
    print(get_asteroid_risk_prediction(0.5, 50000, 0))           # Error
