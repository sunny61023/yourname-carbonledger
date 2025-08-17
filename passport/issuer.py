# passport/issuer.py
import json
import uuid
import datetime

def issue_passport(model_name: str, energy_kwh: float, carbon_intensity: float):
    """
    Issues a verifiable 'Carbon Passport' for an AI query/job.
    - model_name: which AI/ML model
    - energy_kwh: energy consumed (kWh)
    - carbon_intensity: gCO2 per kWh
    """
    passport = {
        "@context": "https://schema.org/",
        "@type": "CarbonPassport",
        "id": str(uuid.uuid4()),
        "model": model_name,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "energy_kwh": energy_kwh,
        "carbon_intensity": carbon_intensity,
        "emissions_gCO2": round(energy_kwh * carbon_intensity, 2)
    }
    return passport


if __name__ == "__main__":
    sample = issue_passport("gpt-simulated", 0.25, 420)  # 0.25 kWh, 420 gCO2/kWh
    print(json.dumps(sample, indent=2))

