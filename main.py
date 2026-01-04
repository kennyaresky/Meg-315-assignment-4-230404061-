from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from CoolProp.CoolProp import PropsSI

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set the templates folder
templates = Jinja2Templates(directory="templates")

# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Calculate route
@app.post("/calculate")
async def calculate(data: dict):
    P_boiler = data.get("P_boiler") * 1e5  # bar -> Pa
    P_condenser = data.get("P_condenser") * 1e5
    T_turbine_inlet = data.get("T_turbine_inlet") + 273.15  # °C -> K
    pump_eff = data.get("pump_efficiency")
    turbine_eff = data.get("turbine_efficiency")
    
    # --- Point 1: Condenser exit ---
    T1 = PropsSI("T", "P", P_condenser, "Q", 0, "Water")
    h1 = PropsSI("H", "P", P_condenser, "Q", 0, "Water")
    s1 = PropsSI("S", "P", P_condenser, "Q", 0, "Water")
    v1 = 1 / PropsSI("D", "P", P_condenser, "Q", 0, "Water")
    
    # --- Point 2: Pump exit ---
    h2s = h1 + v1 * (P_boiler - P_condenser)
    h2 = h1 + (h2s - h1) / pump_eff
    T2 = PropsSI("T", "P", P_boiler, "H", h2, "Water")
    s2 = PropsSI("S", "P", P_boiler, "H", h2, "Water")
    v2 = 1 / PropsSI("D", "P", P_boiler, "H", h2, "Water")
    
    # --- Point 3: Boiler exit / Turbine inlet ---
    T3 = T_turbine_inlet
    P3 = P_boiler
    h3 = PropsSI("H", "P", P3, "T", T3, "Water")
    s3 = PropsSI("S", "P", P3, "T", T3, "Water")
    v3 = 1 / PropsSI("D", "P", P3, "T", T3, "Water")
    
    # --- Point 4: Turbine exit ---
    s4s = s3  # isentropic
    h4s = PropsSI("H", "P", P_condenser, "S", s4s, "Water")
    h4 = h3 - turbine_eff * (h3 - h4s)
    T4 = PropsSI("T", "P", P_condenser, "H", h4, "Water")
    s4 = PropsSI("S", "P", P_condenser, "H", h4, "Water")
    v4 = 1 / PropsSI("D", "P", P_condenser, "H", h4, "Water")
    
    states = [
        {"point": 1, "T": T1, "P": P_condenser, "h": h1, "s": s1, "v": v1},
        {"point": 2, "T": T2, "P": P_boiler, "h": h2, "s": s2, "v": v2},
        {"point": 3, "T": T3, "P": P_boiler, "h": h3, "s": s3, "v": v3},
        {"point": 4, "T": T4, "P": P_condenser, "h": h4, "s": s4, "v": v4}
    ]
    
    ts_chart = {"data":[{"x":[s["s"] for s in states], "y":[s["T"] for s in states], "mode":"lines+markers", "type":"scatter"}]}
    pv_chart = {"data":[{"x":[s["v"] for s in states], "y":[s["P"] for s in states], "mode":"lines+markers", "type":"scatter"}]}
    
    return JSONResponse({"states": states, "ts_chart": ts_chart, "pv_chart": pv_chart})
