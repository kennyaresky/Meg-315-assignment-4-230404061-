from CoolProp.CoolProp import PropsSI

def calculate_rankine_cycle(inputs):
    """
    Calculate the Rankine cycle states (4 points) for given inputs.
    inputs: dict with keys
        P_boiler (bar), P_condenser (bar), T_turbine_inlet (°C)
        pump_efficiency (0-1), turbine_efficiency (0-1)
    Returns: list of states with T, P, h, s, v
    """
    try:
        # Convert pressures to Pa and temperature to K
        P_boiler = inputs['P_boiler'] * 1e5
        P_condenser = inputs['P_condenser'] * 1e5
        T_turbine_inlet = inputs['T_turbine_inlet'] + 273.15
        pump_eff = inputs.get('pump_efficiency', 0.85)
        turbine_eff = inputs.get('turbine_efficiency', 0.85)

        states = []

        # -------------------
        # Point 1: Condenser exit / Pump inlet (saturated liquid)
        # -------------------
        T1 = PropsSI('T', 'P', P_condenser, 'Q', 0, 'Water')
        h1 = PropsSI('H', 'P', P_condenser, 'Q', 0, 'Water')
        s1 = PropsSI('S', 'P', P_condenser, 'Q', 0, 'Water')
        v1 = 1 / PropsSI('D', 'P', P_condenser, 'Q', 0, 'Water')
        states.append({'point': 1, 'T': T1, 'P': P_condenser, 'h': h1, 's': s1, 'v': v1})

        # -------------------
        # Point 2: Pump exit / Boiler inlet (compressed liquid)
        # -------------------
        # Isentropic pump work
        v1_specific = v1
        h2s = h1 + v1_specific * (P_boiler - P_condenser)  # ideal pump work
        # Actual pump considering efficiency
        h2 = h1 + (h2s - h1) / pump_eff
        # Estimate temperature from h2 and P_boiler
        T2 = PropsSI('T', 'P', P_boiler, 'H', h2, 'Water')
        s2 = PropsSI('S', 'P', P_boiler, 'H', h2, 'Water')
        v2 = 1 / PropsSI('D', 'P', P_boiler, 'H', h2, 'Water')
        states.append({'point': 2, 'T': T2, 'P': P_boiler, 'h': h2, 's': s2, 'v': v2})

        # -------------------
        # Point 3: Boiler exit / Turbine inlet (superheated steam)
        # -------------------
        h3 = PropsSI('H', 'P', P_boiler, 'T', T_turbine_inlet, 'Water')
        s3 = PropsSI('S', 'P', P_boiler, 'T', T_turbine_inlet, 'Water')
        v3 = 1 / PropsSI('D', 'P', P_boiler, 'T', T_turbine_inlet, 'Water')
        states.append({'point': 3, 'T': T_turbine_inlet, 'P': P_boiler, 'h': h3, 's': s3, 'v': v3})

        # -------------------
        # Point 4: Turbine exit / Condenser inlet (expanded steam)
        # -------------------
        # Isentropic turbine work
        h4s = PropsSI('H', 'P', P_condenser, 'S', s3, 'Water')  # ideal turbine outlet
        # Actual turbine considering efficiency
        h4 = h3 - turbine_eff * (h3 - h4s)
        # Estimate T4 and v4 from P_condenser and h4
        T4 = PropsSI('T', 'P', P_condenser, 'H', h4, 'Water')
        s4 = PropsSI('S', 'P', P_condenser, 'H', h4, 'Water')
        v4 = 1 / PropsSI('D', 'P', P_condenser, 'H', h4, 'Water')
        states.append({'point': 4, 'T': T4, 'P': P_condenser, 'h': h4, 's': s4, 'v': v4})

        return states

    except Exception as e:
        return {"error": str(e)}
