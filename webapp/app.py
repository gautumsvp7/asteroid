from flask import Flask, request, render_template
from model_predictor import get_asteroid_risk_prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    error_text = None
    if request.method == 'POST':
        try:
            diameter = request.form.get('diameter')
            velocity = request.form.get('velocity')
            distance = request.form.get('distance')

            # Basic validation to ensure inputs are provided
            if diameter is None or velocity is None or distance is None or \
               diameter == '' or velocity == '' or distance == '':
                error_text = "Error: All input fields are required."
            else:
                # The get_asteroid_risk_prediction function already handles float conversion and specific errors
                result = get_asteroid_risk_prediction(diameter, velocity, distance)
                if "Error:" in result:
                    error_text = result
                else:
                    prediction_text = result
        except Exception as e:
            # Catch any other unexpected errors
            error_text = f"An unexpected error occurred: {str(e)}"

    # Pass None for values if it's a GET request or if there was an error preventing their display
    return render_template('index.html',
                           prediction_text=prediction_text,
                           error_text=error_text,
                           diameter=request.form.get('diameter', '') if request.method == 'POST' else '',
                           velocity=request.form.get('velocity', '') if request.method == 'POST' else '',
                           distance=request.form.get('distance', '') if request.method == 'POST' else '')

if __name__ == '__main__':
    app.run(debug=True)
