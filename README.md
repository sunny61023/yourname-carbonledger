# 🌍 CarbonLedger — Verifiable Carbon-Passports & Negative-Emission Orchestration  

**Author:** [ SHIVARATRI SUNNY], SR University, Warangal  
**Contact:** [ 2305a41030@sru.edu.in] GitHub: https://github.com/sunny61023  

---

## 🚀 Overview  

CarbonLedger is a **reproducible framework for auditable AI carbon footprints**.  
It introduces **Carbon Passports** (per-model and per-query), a **carbon-aware orchestrator**, and a **waste-heat credit protocol** to turn AI compute into a **climate-positive system**.  

Instead of vague averages, every model and every query gets a **cryptographically verifiable passport** with real emissions data. Workloads can be scheduled when & where grid electricity is cleanest — and paired with verified **waste-heat reuse credits** to achieve **net-negative AI**.  

---

## ✨ Key Features  

✅ **Carbon Passports** — signed JSON-LD records with per-model, per-query emissions  
✅ **Hourly Marginal Carbon Estimator (HMCE)** — accurate gCO₂e per hour, per query  
✅ **Carbon-Aware Orchestrator (CAO)** — optimizes placement & timing of jobs for lowest emissions  
✅ **Waste-Heat Credit Protocol (WHCP)** — turns recovered data-centre heat into verifiable credits  
✅ **Auditor Module** — ensures transparency, no greenwashing, cryptographic provenance  

---

## 📂 Repository Structure  

```bash
carbonledger/
│
├── passport/        # JSON-LD schema + signing tool
├── hmce/            # Hourly marginal carbon estimator scripts
├── cao/             # Carbon-aware orchestrator (simulator / K8s operator)
├── whcp/            # Heat credit protocol mock service
├── notebooks/       # Colab demo notebooks
└── assets/images/   # Diagrams & JSON passport screenshots
