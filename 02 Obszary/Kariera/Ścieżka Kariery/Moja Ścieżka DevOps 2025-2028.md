---
typ: roadmapa-osobista
kategoria: kariera
status: aktywny
data_aktualizacji: 2026-03-15
cel: Platform Engineer w scale-upie
---

# Moja Ścieżka: Platform Engineer 2025–2028

> [!abstract] Cel
> Mid/Senior DevOps/Platform Eng w scale-upie (200–1000 osób, SaaS). Pensja napędzająca maszynę inwestycyjną. Saving Rate >50%.

---

## Gdzie jestem vs gdzie muszę być

| Umiejętność          | Teraz     | Target Mid DevOps     | Priorytet   |
|----------------------|-----------|-----------------------|-------------|
| Docker               | ✅        | ✅ wystarczy          | —           |
| Kubernetes           | 🟡 teoria | 🎯 core skill         | ⭐⭐⭐⭐⭐   |
| Terraform / IaC      | ❌        | 🎯 must-have          | ⭐⭐⭐⭐⭐   |
| GitHub Actions CI/CD | 🟡 basics | 🎯 pełny pipeline     | ⭐⭐⭐⭐    |
| Python (narzędzia)   | 🟡 basics | 🎯 piszę samodzielnie | ⭐⭐⭐⭐    |
| AWS / Cloud          | ❌        | 🎯 jeden cloud        | ⭐⭐⭐      |
| Linux / Bash         | ✅        | ✅ wystarczy          | ⭐⭐⭐      |
| Observability (PLT)  | 🟡 teoria | 🟡 nice to have       | ⭐⭐        |

---

## Harmonogram nauki

### Miesiące 1–2: Kubernetes w praktyce
- [x] Kurs: "Kubernetes for Absolute Beginners" — Mumshad Mannambeth (Udemy)
- [ ] Postawić k3s na mini PC (HomeLab)
- [ ] Wdrożyć prawdziwą aplikację (SOTP lub ChronoBook)
- [ ] Opanować: Pod, Deployment, Service, Ingress, ConfigMap, PV, RBAC
- **Cel:** kubectl z zamkniętymi oczami, troubleshooting z głowy

### Miesiące 2–3: Terraform + IaC
- [ ] Kurs: "HashiCorp Terraform Associate" — Zeal Vora (Udemy)
- [ ] Darmowy tier AWS do ćwiczeń
- [ ] Napisać IaC dla całego HomeLab (Proxmox + k3s + sieć)
- [ ] Opanować: state, moduły, remote backend, workspace
- **Cel:** cały HomeLab postawiony jedną komendą

### Miesiące 3–4: CI/CD pipeline end-to-end
- [ ] GitHub Actions: lint → test → build Docker → push → deploy k3s
- [ ] ArgoCD: GitOps dla własnych projektów
- [ ] Napisać pipeline dla SOTP lub własnej apki
- **Cel:** push do GitHub = automatyczny deploy na k3s

### Miesiące 4–6: Python narzędziowy
- [ ] Skupienie: os, subprocess, requests, argparse, logging, FastAPI
- [ ] Projekt: narzędzie CLI do automatyzacji czegoś w pracy/IBM
- **Cel:** samodzielne pisanie tools bez Stack Overflow co 5 min

### Miesiące 6–9: AWS basics
- [ ] AWS Solutions Architect Associate — to już otwiera drzwi
- [ ] Skupienie: EC2, S3, VPC, IAM, EKS

---

## Certyfikaty — kolejność

| Cert                           | Kiedy    | Koszt   | Wartość    |
|--------------------------------|----------|---------|------------|
| HashiCorp Terraform Associate  | Q3 2026  | ~600 PLN | ⭐⭐⭐⭐   |
| **CKA** (Kubernetes Admin)     | Q4 2026  | ~1600 PLN | ⭐⭐⭐⭐⭐ |
| AWS Solutions Architect Assoc. | Q1 2027  | ~600 PLN | ⭐⭐⭐⭐   |
| RHCSA                          | Q2 2027  | ~1600 PLN | ⭐⭐⭐ (IBM-specific) |

---

## 3 Projekty do CV 

### 1. HomeLab as Code
Cały Proxmox/k3s przez Terraform + Ansible. Zero klikania w GUI. README z architekturą.
**Pokazuje:** IaC, GitOps mindset, reproducibility.

### 2. CI/CD Pipeline end-to-end
FastAPI app → GitHub Actions → Docker → k3s → Prometheus/Grafana.
**Pokazuje:** pełny DevOps workflow od kodu do produkcji.

### 3. SOTP 


---

## Strategia zmiany pracy

> Zmiana co 2–3 lata = jedyna skuteczna metoda podwyżek w IT.
> Lojalność przez 5 lat w jednej firmie = strata 30–40% pensji.

| Wiek | Rok  | Rola               | Pensja netto pesym. |
|------|------|--------------------|---------------------|
| 21   | 2026 | Junior DevOps      | 5 500 PLN           |
| 22–23 | 2027–28 | Junior+/Regular | 7 500 PLN          |
| 24–25 | 2029–30 | Mid DevOps      | 10 000 PLN          |
| 26–27 | 2031–32 | Mid/Senior      | 13 000 PLN          |
| 28–30 | 2033–35 | Senior/Lead     | 16 000+ PLN         |

> [!warning] Ważna data
> **Listopad 2026** — aktywnie  poszukać pracy PRZED końcem stażu w IBM (grudzień 2026).


### Firmy na celowniku (Kraków)
- Allegro, Sabre, EPAM, Hitachi Energy, Motorola Solutions, UBS
- Remote EU: scale-upy DE/NL/UK (ekwiwalent 20–28k PLN netto)

---

## Powiązane
- [[Master Hub - DevOps & Kariera]]
- [[Checklist]]
- [[Firmy]]
- [[Nauka - Harmonogram Tygodniowy]]
