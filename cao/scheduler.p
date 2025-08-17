# cao/scheduler.py
import datetime
from hmce.simulate import simulate_hourly_intensity
from passport.issuer import issue_passport

def schedule_job(job_id, model_name="demo-model", energy_kwh=0.2):
    """Schedules a job depending on carbon intensity & issues a passport."""
    data = simulate_hourly_intensity()
    carbon_intensity = data["carbon_intensity"]

    # Check if we are in "green hours"
    if carbon_intensity < 350:
        decision = "✅ Scheduled in green energy window"
    else:
        decision = "⚠️ Deferred - carbon intensity too high"

    passport = issue_passport(model_name, energy_kwh, carbon_intensity)

    print(f"[{job_id}] {decision}")
    print(passport)

    return passport

if __name__ == "__main__":
    for i in range(3):
        schedule_job(f"job-{i+1}")

