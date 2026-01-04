import plotly.graph_objects as go

def generate_ts_chart(states):
    """
    Generate T-s chart from the Rankine cycle states.
    Returns Plotly figure JSON.
    """
    # Extract s and T values
    s_vals = [pt['s'] for pt in states] + [states[0]['s']]  # close the cycle
    T_vals = [pt['T'] for pt in states] + [states[0]['T']]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=s_vals,
        y=T_vals,
        mode='lines+markers',
        name='T-s Cycle',
        line=dict(color='firebrick', width=3)
    ))
    fig.update_layout(
        title='Rankine Cycle T-s Diagram',
        xaxis_title='Entropy s (J/kg·K)',
        yaxis_title='Temperature T (K)',
        template='plotly_white'
    )
    return fig.to_json()


def generate_pv_chart(states):
    """
    Generate P-v chart from the Rankine cycle states.
    Returns Plotly figure JSON.
    """
    # Extract P and v values
    v_vals = [pt['v'] for pt in states] + [states[0]['v']]  # close the cycle
    P_vals = [pt['P'] for pt in states] + [states[0]['P']]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=v_vals,
        y=P_vals,
        mode='lines+markers',
        name='P-v Cycle',
        line=dict(color='royalblue', width=3)
    ))
    fig.update_layout(
        title='Rankine Cycle P-v Diagram',
        xaxis_title='Specific Volume v (m³/kg)',
        yaxis_title='Pressure P (Pa)',
        template='plotly_white'
    )
    return fig.to_json()
