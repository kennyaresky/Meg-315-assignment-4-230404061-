
# Rankine Cycle Visualizer (FastAPI + Plotly)

## 📌 Project Overview

This project is a web-based thermodynamic visualization tool developed to analyze the ideal Rankine cycle used in steam power plants.

It computes the thermodynamic properties at key state points of the Rankine cycle and visualizes the process on:

T–s (Temperature–Entropy) diagram

P–v (Pressure–Specific Volume) diagram

The project aligns with the Applied Thermodynamics assignment, specifically:

“Review the provided Building APIs in Python and SQL Server Fundamental Tracks from Datacamp towards developing the frontend to visualize the T-s and P-v charts of the processes governed by the theoretical Rankine cycle for the different flow processes.”


It allows users to:

* Input key Rankine cycle parameters
* Compute thermodynamic state points (ideal Rankine cycle)
* Visualize the cycle on **T–s** and **P–v** diagrams
* View computed state properties in tabular form

This project was developed for **Applied Thermodynamics** to demonstrate:

* API development in Python
* Frontend–backend interaction
* Visualization of thermodynamic processes

---

## 🧠 Theory Background (Very Important)

The **ideal Rankine cycle** consists of four main processes:

1. **1 → 2 (Pump)**
   Isentropic compression of saturated liquid from condenser pressure to boiler pressure.

2. **2 → 3 (Boiler)**
   Constant pressure heat addition until superheated steam is produced.

3. **3 → 4 (Turbine)**
   Isentropic expansion of steam producing work.

4. **4 → 1 (Condenser)**
   Constant pressure heat rejection, condensing steam back to saturated liquid.

The project visualizes these processes on:

* **Temperature–Entropy (T–s) diagram**
* **Pressure–Specific Volume (P–v) diagram**

---

## 🏗️ Project Architecture


⚙️ Technologies Used

# Backend

Python 3.9+

FastAPI

CoolProp (thermodynamic property calculations)

Uvicorn (ASGI server)



# Frontend

HTML5

CSS3

JavaScript

Plotly.js (for T–s and P–v charts)



### 🔹 Backend (FastAPI)

* Handles API routing
* Accepts Rankine cycle inputs
* Performs (currently) **ideal/dummy thermodynamic calculations**
* Returns:

  * State properties
  * T–s chart data
  * P–v chart data

### 🔹 Frontend

* Responsive HTML UI
* JavaScript sends data to backend using `fetch`
* Plotly renders T–s and P–v diagrams
* Results displayed dynamically without page reload

---









📦 Required Installations
1️⃣ Python

Make sure Python 3.9 or later is installed:

python --version

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Required Libraries

Note: CoolProp is already used in this project.

pip install fastapi uvicorn jinja2 coolprop plotly


Or using requirements.txt:

pip install -r requirements.txt


## ▶️ How to Run the Project

### Step 1: Navigate to project folder

```bash
cd rankine_fastapi_assignment
```

### Step 2: Run the FastAPI server

```bash
uvicorn main:app --reload
```

If your file is inside a folder (e.g. `app/main.py`), use:

```bash
uvicorn app.main:app --reload
```

### Step 3: Open the browser

Go to:

```
http://127.0.0.1:8000
```

---

## 🖥️ How to Use the App

1. Enter:

   * Boiler Pressure (bar)
   * Condenser Pressure (bar)
   * Turbine Inlet Temperature (°C)
   * Pump Efficiency
   * Turbine Efficiency

2. Click **Calculate**

3. The app will:

   * Display state properties (Points 1–4)
   * Plot **T–s diagram**
   * Plot **P–v diagram**

---

Visualization

The charts produced are:

T–s Diagram → entropy vs temperature

P–v Diagram → pressure vs specific volume




## ✅ Academic Note

This project fulfills:

* API development using Python
* Frontend visualization of thermodynamic processes
* Application of Rankine cycle theory

