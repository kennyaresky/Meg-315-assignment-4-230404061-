from pydantic import BaseModel

class CycleInput(BaseModel):
    P_boiler: float           # Boiler pressure in bar
    P_condenser: float        # Condenser pressure in bar
    T_turbine_inlet: float    # Turbine inlet temp in °C
    pump_efficiency: float = 0.85
    turbine_efficiency: float = 0.85
