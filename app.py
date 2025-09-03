from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
CSV_FILE = "patients.csv"   # update to your actual file path
df = pd.read_csv(CSV_FILE)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    patients = None
    if request.method == "POST":
        patient_id = request.form.get("patient_id")
        age = request.form.get("age")
        gender = request.form.get("gender")

        filtered = df.copy()

        if patient_id:
            filtered = filtered[filtered["PatientID"].astype(str) == patient_id]
        if age:
            filtered = filtered[filtered["Age"] == int(age)]
        if gender:
            filtered = filtered[filtered["Gender"].str.lower() == gender.lower()]

        patients = filtered.to_dict(orient="records")
        return render_template("result.html", patients=patients)

    return render_template("search.html")

@app.route("/patient/<patient_id>")
def patient_detail(patient_id):
    patient = df[df["PatientID"].astype(str) == str(patient_id)]
    if patient.empty:
        return render_template("result.html", patients=[])
    return render_template("patient_details.html", patient=patient.iloc[0].to_dict())

if __name__ == "__main__":
    app.run(debug=True)
