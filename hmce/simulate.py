# hmce/simulate.py
import random
import datetime

def simulate_hourly_intensity():
    """
    Simulates hourly marginal carbon intensity (gCO2/kWh).
    Renewable-heavy hours have lower intensity.
    """
    now = datetime.datetime.now()
    hour = now.hour

    # simple model: cleaner energy between 10am - 4pm
    if 10 <= hour <= 16:
        intensity = random.randint(150, 300)  # low carbon
    else:
        intensity = random.randint(400, 600)  # high carbon

    return {
        "hour": hour,
        "carbon_intensity": intensity,
        "timestamp": now.isoformat()
    }

if __name__ == "__main__":
    print(simulate_hourly_intensity())

