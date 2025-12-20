---
typ: plan
projekt: 00 SOTP Dashboard
---
#  Roadmapa i Fazy Wdrożenia

## Szacowany Czas: 16-19 Tygodni

### [[Roadmapa i Fazy#FAZA 0 Fundamenty i Proof of Concept|FAZA 0: Fundamenty i POC]] (1 Tydzień)
Walidacja koncepcji.
- [x] 0.1 Konfiguracja środowiska ([[DevContainer]], [[Makefile]]).
- [x] 0.2 POC: Kolektor [[ICMP]] + [[Prometheus]] + [[Grafana]].
- [x] 0.3 Definicja [[User Stories]] i wymagań.

### [[Roadmapa i Fazy#FAZA 1 MVP - Fundamenty Kubernetes|FAZA 1: MVP - Fundamenty Kubernetes]] (3-4 Tygodnie)
Działająca aplikacja CRUD na klastrze.
- [ ] 1.1 Lokalny klaster [[K3d]] (K3s).
- [ ] 1.2 Stworzenie [[Helm Chart]] dla SOTP.
- [x] 1.3 Baza danych: Migracje [[Alembic]] dla [[PostgreSQL]] i [[TimescaleDB]].
- [x] 1.4 Backend API: [[FastAPI]] Core i CRUD urządzeń.
- [x] 1.5 Kolektor [[ICMP]] (produkcyjny) z użyciem biblioteki `icmplib`.
- [ ] 1.6 Frontend: [[Next.js]] + [[Tailwind CSS]].

### [[Roadmapa i Fazy#FAZA 2 Bezpieczeństwo i Monitoring|FAZA 2: Bezpieczeństwo i Monitoring]] (3 Tygodnie)
- [ ] 2.1 Autentykacja [[JWT]] i [[RBAC]].
- [ ] 2.2 Integracja z [[HashiCorp Vault]] (wstrzykiwanie sekretów).
- [ ] 2.3 Kolektor [[SNMP]] (wersje v2c i v3).

### [[Roadmapa i Fazy#FAZA 3 Obserwowalność i GitOps|FAZA 3: Obserwowalność i GitOps]] (3 Tygodnie)
Wdrożenie pełnego stosu PLT.
- [ ] 3.1 Metryki: [[Prometheus Operator]] i [[Alertmanager]].
- [ ] 3.2 Logi: [[Loki]] i [[Promtail]].
- [ ] 3.3 Ślady (Tracing): [[Grafana Tempo]] i instrumentacja [[OpenTelemetry]].
- [ ] 3.4 Wdrożenie [[GitOps]] z [[ArgoCD]].

### [[Roadmapa i Fazy#FAZA 4 Funkcjonalność Produkcyjna|FAZA 4: Funkcjonalność Produkcyjna]] (3-4 Tygodnie)
- [ ] 4.1 Kolektor [[SSH]] ([[Netmiko]]) i parsowanie komend.
- [ ] 4.2 Obsługa [[Syslog]] i logi audytowe.
- [ ] 4.3 Raportowanie ([[PDF]], [[CSV]]).
- [ ] 4.4 Backup i [[Disaster Recovery]] (S3/MinIO).

### [[Roadmapa i Fazy#FAZA 5 Wizja|FAZA 5: Wizja i AI]] (Ongoing)
- [ ] 5.1 [[Service Mesh]] ([[Linkerd]]) - mTLS.
- [ ] 5.2 Auto-remediacja (Self-healing).
- [ ] 5.3 Anomalia i AI: [[TimescaleDB Toolkit]] + Prophet.