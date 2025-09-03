# 🧠 OCD Patients Web Application

An interactive **OCD Patient Prediction Web App** built with **Flask**, **Scikit-learn**, and **Pandas**, deployed on **Render**, and version-controlled with **GitHub**.  
This project predicts OCD condition based on patient details and displays results in a simple web interface.

---

## 📊 About the Data
- Dataset: **OCD_Patient.csv**  
- Contains patient demographic and behavioral details.  
- Used to:
  - Train an ML model for OCD risk prediction  
  - Demonstrate data-driven healthcare applications  

---

## ⚙️ Why These Technologies?
- **Flask** → Lightweight backend framework for Python-based ML web apps.  
- **Pandas** → For data handling and preprocessing.  
- **Scikit-learn** → Trained OCD prediction model (`ocd_model.pkl`).  
- **Gunicorn** → Production-ready WSGI server.  
- **Render** → Cloud platform for deployment with GitHub integration.  

---

## 🚀 Complete Process (From Start to Finish)

### 1. Create Project Folder
D:\ocd_patients_web

### 2. Create & Activate Virtual Environment
- Windows:
  - `python -m venv venv`
  - `venv\Scripts\activate`
- macOS/Linux:
  - `python3 -m venv venv`
  - `source venv/bin/activate`

### 3. Install Dependencies
- Install required libraries:
  - `pip install flask pandas scikit-learn gunicorn`
- Export dependencies:
  - `pip freeze > requirements.txt`

### 4. Build Flask Application
- Created `app.py` with routes:
  - `/` → Home page with patient form  
  - `/result` → Display prediction results  
  - `/patient_detail` → Show individual patient details  
- Used:
  - Flask → Web framework  
  - Scikit-learn → ML prediction model  
  - Pandas → Handle input data  

### 5. Add Project Files
- `app.py` → Main Flask application  
- `templates/` → HTML templates (home, result, patient detail)  
- `requirements.txt` → Installed dependencies  
- `Procfile` → For Render deployment (`web: gunicorn app:app`)  
- `ocd_model.pkl` → Trained ML model  
- `label_encoder.pkl` → Label encoding for categorical features  
- `OCD_Patient.csv` → Dataset  

### 6. Initialize Git & Push to GitHub
- `git init`  
- `git remote add origin https://github.com/afridmd12/ocd_patients_web.git`  
- `git add .`  
- `git commit -m "Initial commit"`  
- `git push -u origin main`

### 7. Deploy on Render
1. Go to [Render](https://render.com)  
2. Create a new **Web Service**  
3. Connect GitHub repository  
4. Add:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Deploy 🚀  

---

## ✅ Features
- Patient form input for OCD prediction  
- Trained ML model for classification  
- Individual patient detail page  
- Hosted on Render  

---

## 💻 Run Locally
1. Clone repo:  
   `git clone https://github.com/afridmd12/ocd_patients_web.git`
2. Navigate:  
   `cd ocd_patients_web`
3. Create virtual environment & activate  
4. Install dependencies:  
   `pip install -r requirements.txt`
5. Run app:  
   `python app.py`
6. Open in browser:  
   `http://127.0.0.1:3001`

---

## 🌐 Deployment
- Hosted on **Render**  
- Live URL: [https://ocd-patients-web.onrender.com](https://ocd-patients-web.onrender.com)

---

## 📝 Author
👤 Mohammed Afrid  
📌 GitHub: [afridmd12](https://github.com/afridmd12/ocd_patients_web.git)  
