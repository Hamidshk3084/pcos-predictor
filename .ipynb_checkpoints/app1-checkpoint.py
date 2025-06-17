from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("rf_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Set the optimal threshold from ROC analysis
OPTIMAL_THRESHOLD = 0.41  

@app.route("/")
def home():
    return render_template("front.html")

@app.route('/input')
def input_page():
    return render_template('index1.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract user input values
        age = float(request.form["Age"])
        height = float(request.form["Height"])
        weight = float(request.form["Weight"])
        waist = float(request.form["Waist"])
        hip = float(request.form["Hip"])
        pulse_rate = float(request.form["Pulse_rate"])
        cycle_length = float(request.form["Cycle_length"])
        cycle_ri = int(request.form["Cycle_RI"])
        marriage_status = float(request.form["Marraige_Status"])
        skin_darkening = int(request.form["Skin_darkening"])
        hair_growth = int(request.form["Hair_growth"])
        weight_gain = int(request.form["Weight_gain"])
        pimples = int(request.form["Pimples"])
        fast_food = int(request.form["Fast_food"])
        reg_exercise = int(request.form["Reg_Exercise"])
        hair_loss = int(request.form["Hair_loss"])

        # Auto-computed values
        bmi = weight / ((height / 100) ** 2)
        waist_to_weight = waist / weight
        cycle_score = 1.5 if cycle_length > 35 or cycle_length < 21 else 1.2 if cycle_ri == 0 else 1
        androgen_indicator = 1 if (pimples == 1 or hair_growth == 1) else 0
        fastfood_weightgain = 1 if (fast_food == 1 and weight_gain == 1) else 0
        symptom_severity = skin_darkening + hair_growth + weight_gain + pimples + fast_food

        # Prepare input array for model
        input_features = np.array([
            symptom_severity, skin_darkening, cycle_length, hair_growth, cycle_ri, age, height,
            bmi, marriage_status, hip, weight, waist, androgen_indicator, weight_gain, fast_food,
            pulse_rate, fastfood_weightgain, pimples, reg_exercise, hair_loss
        ]).reshape(1, -1)

        # Make prediction (probability of PCOS)
        prediction_prob = model.predict_proba(input_features)[0][1] * 100  # Convert to percentage

        # Classify based on threshold
        diagnosis = "PCOS Detected" if prediction_prob >= (OPTIMAL_THRESHOLD * 100) else "No PCOS Detected"

        # Pass prediction and health advice to result.html
        return render_template(
            "result.html", 
            prediction_text=f"{diagnosis} (Risk: {prediction_prob:.2f}%)",
            risk_percentage=f"{prediction_prob:.2f}%"
        )

    except Exception as e:
        return render_template("result.html", prediction_text=f"Error: {str(e)}", risk_percentage="N/A")

if __name__ == "__main__":
    app.run(debug=True)
