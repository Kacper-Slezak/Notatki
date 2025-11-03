## SOTP Master Document v4.0 ULTIMATE

System Observability & Telemetry Platform

Wersja: 4.0 Ultimate Edition (zaktualizowany podział ról)

Ostatnia aktualizacja: 2024-11-03

Status: Gotowy Plan Produkcyjny

### Streszczenie Zarządcze

SOTP to flagowa platforma do monitoringu infrastruktury sieciowej, łącząca:

- Nowoczesną architekturę (Kubernetes, GitOps, Service Mesh)
    
- Pełną obserwowalność (Metryki, Logi, Ślady - Stos PLT)
    
- Bezpieczeństwo klasy enterprise (Vault, mTLS, RBAC)
    
- Automatyzację (Automatyczna naprawa, predykcje AI/ML)
    

Kluczowe cechy:

- Natywny dla Kubernetes (K3d lokalnie, gotowy na chmurę)
    
- Wdrożenia GitOps (ArgoCD)
    
- Pełny stos obserwowalności (Prometheus + Loki + Tempo)
    
- Bezpieczeństwo Zero-Trust (Service Mesh + Vault)
    
- Inteligentna automatyzacja (Predykcje ML, auto-remediacja)
    

### Architektura

#### Warstwa Logiczna (Architektura Aplikacji)

```
┌─────────────────────────────────────────────────────────────┐
│                 WARSTWA INTERFEJSU UŻYTKOWNIKA              │
│  Next.js 14 (React) + Tailwind CSS + shadcn/ui              │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTPS (Traefik Ingress)
┌────────────────────▼────────────────────────────────────────┐
│                   WARSTWA BRAMY API                         │
│  Traefik (Ingress) → Rate Limiting → Walidacja JWT          │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  WARSTWA APLIKACJI                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Device     │  │  Auth/RBAC   │  │   Alerting   │       │
│  │   Service    │  │   Service    │  │   Service    │       │
│  │  (FastAPI)   │  │  (FastAPI)   │  │  (FastAPI)   │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│             WARSTWA PAMIĘCI PODRĘCZNEJ I KOLEJEK            │
│  Redis Cluster (Cache + Sesje + Broker Celery)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  WORKERZY KOLEKTORÓW                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │   ICMP   │ │   SNMP   │ │   SSH    │ │  Syslog  │        │
│  │ Collector│ │ Collector│ │ Collector│ │ Collector│        │
│  │ (Celery) │ │ (Celery) │ │ (Celery) │ │ (Celery) │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                 WARSTWA DANYCH I SEKRETÓW                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │  PostgreSQL 16  │  │  TimescaleDB    │  │ HashiCorp    │ │
│  │  (Inwentarz)    │  │  (Szeregi czas.)│  │ Vault        │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│           WARSTWA OBSERWOWALNOŚCI (Stos PLT)                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │  Prometheus     │  │  Loki           │  │ Tempo        │ │
│  │  (Metryki)      │  │  (Logi)         │  │ (Ślady)      │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │           Grafana (Zunifikowany Dashboard)             │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

#### Warstwa Wdrożenia (Architektura Infrastruktury)

```
┌──────────────────────────────────────────────────────────────┐
│                  STACJA ROBOCZA DEWELOPERA                   │
│            (VS Code + DevContainer)                          │
└────────────────────┬─────────────────────────────────────────┘
                     │ git push
┌────────────────────▼─────────────────────────────────────────┐
│              Repozytorium GitHub (sotp-backend)              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Potok CI (.github/workflows/ci.yml)                  │    │
│  │  ✓ Lint (Black, isort, ESLint, Prettier)             │    │
│  │  ✓ Testy (Pytest >80% pokrycia, Vitest)              │    │
│  │  ✓ Skanowanie bezp. (Bandit, Safety, Trivy)          │    │
│  │  ✓ Budowanie obrazów Docker (Multi-stage)            │    │
│  └──────────────────────────────────────────────────────┘    │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Potok CD (.github/workflows/deploy.yml)              │    │
│  │  ✓ Push obrazów do GHCR                              │    │
│  │  ✓ Aktualizacja tagów obrazów w repo sotp-k8s-config │    │
└────────────────────┬─────────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────────┐
│            GitHub: sotp-k8s-config (Repozytorium GitOps)     │
│  infrastructure/helm/sotp/                                   │
│    ├── Chart.yaml                                            │
│    ├── values.yaml  ← image.tag aktualizowany przez CD       │
│    └── templates/                                            │
└────────────────────┬─────────────────────────────────────────┘
                     │ ArgoCD obserwuje to repozytorium
┌────────────────────▼─────────────────────────────────────────┐
│           Klaster Kubernetes (K3d lokalnie / Chmura)         │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ ArgoCD (Kontroler GitOps)                            │    │
│  │  - Wykrywa zmiany w sotp-k8s-config                  │    │
│  │  - Auto-synchronizacja: helm upgrade sotp ...        │    │
│  │  - Sprawdzanie zdrowia i Auto-rollback               │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Linkerd Service Mesh (Opcjonalnie - Faza 5)          │    │
│  │  - Automatyczne mTLS między serwisami                │    │
│  │  - Metryki L7 (success rate, latency)                │    │
│  │  - Retries & Circuit breaking                        │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  Wdrożona Aplikacja (SOTP):                                  │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────────┐ ┌───────-──┐  │
│  │FastAPI │ │Celery  │ │Redis   │ │PostgreSQL│ │Prometheus│  │
│  │(3 pody)│ │Workers │ │Cluster │ │  + TS    │ │+ Loki +  │  │
│  │        │ │(5 pod) │ │        │ │          │ │  Tempo   │  │
│  └────────┘ └────────┘ └────────┘ └──────────┘ └────────-─┘  │
└──────────────────────────────────────────────────────────────┘
```

### Struktura Projektu

```
sotp/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── devices.py          # CRUD Urządzeń
│   │   │   │   ├── auth.py             # Autentykacja JWT
│   │   │   │   ├── metrics.py          # Zapytania do TimescaleDB
│   │   │   │   ├── logs.py             # Zapytania do Loki
│   │   │   │   ├── alerts.py           # Zarządzanie alertami
│   │   │   │   ├── commands.py         # Wykonywanie poleceń SSH
│   │   │   │   ├── reports.py          # Generowanie raportów
│   │   │   │   └── webhooks.py         # Webhooki Alertmanagera
│   │   │   └── dependencies.py         # Zależności FastAPI
│   │   ├── core/
│   │   │   ├── config.py               # Ustawienia Pydantic
│   │   │   ├── security.py             # JWT, hashowanie haseł
│   │   │   ├── database.py             # Konfiguracja SQLAlchemy
│   │   │   ├── observability.py        # Konfiguracja OpenTelemetry
│   │   │   └── exceptions.py           # Własne wyjątki
│   │   ├── models/
│   │   │   ├── base.py
│   │   │   ├── device.py               # Model ORM urządzenia
│   │   │   ├── user.py                 # Model ORM użytkownika
│   │   │   ├── audit_log.py            # Ślad audytowy
│   │   │   ├── alert.py                # Model alertu
│   │   │   └── alert_rule.py           # Konfiguracja reguł alertów
│   │   ├── schemas/
│   │   │   ├── device.py               # Schematy Pydantic
│   │   │   ├── user.py
│   │   │   ├── metric.py
│   │   │   ├── auth.py
│   │   │   └── alert.py
│   │   ├── services/
│   │   │   ├── device_service.py       # Logika biznesowa
│   │   │   ├── auth_service.py
│   │   │   ├── vault_service.py        # Integracja z Vault
│   │   │   ├── alert_service.py
│   │   │   ├── report_service.py
│   │   │   └── remediation_service.py  # Auto-remediacja
│   │   ├── collectors/
│   │   │   ├── base.py                 # Abstrakcyjny kolektor
│   │   │   ├── icmp_collector.py       # Kolektor Ping
│   │   │   ├── snmp_collector.py       # Kolektor SNMP
│   │   │   ├── ssh_collector.py        # Wykonywanie poleceń SSH
│   │   │   └── syslog_collector.py     # Odbiornik Syslog
│   │   ├── tasks/
│   │   │   ├── celery_app.py           # Konfiguracja Celery
│   │   │   ├── monitoring_tasks.py     # Zadania pollingu
│   │   │   ├── alert_tasks.py          # Ewaluacja alertów
│   │   │   ├── backup_tasks.py         # Backup konfiguracji
│   │   │   └── ml_tasks.py             # Predykcje ML
│   │   └── utils/
│   │       ├── parsers.py              # Parsery TextFSM
│   │       ├── validators.py
│   │       └── helpers.py
│   ├── tests/
│   │   ├── unit/
│   │   │   ├── test_collectors.py
│   │   │   ├── test_services.py
│   │   │   └── test_utils.py
│   │   ├── integration/
│   │   │   ├── test_api.py
│   │   │   └── test_tasks.py
│   │   └── e2e/
│   │       └── test_flows.py
│   ├── alembic/
│   │   ├── env.py                      # Wsparcie dla wielu baz danych
│   │   └── versions/
│   │       ├── 001_initial_postgres.py
│   │       └── 002_initial_timescale.py
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── Dockerfile                      # Budowanie wieloetapowe
│   └── pyproject.toml                  # Konfiguracja Poetry/Ruff
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/page.tsx
│   │   │   │   └── register/page.tsx
│   │   │   ├── (dashboard)/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── page.tsx            # Przegląd
│   │   │   │   ├── devices/
│   │   │   │   │   ├── page.tsx        # Lista urządzeń
│   │   │   │   │   ├── [id]/page.tsx   # Szczegóły urządzenia
│   │   │   │   │   └── [id]/console/page.tsx
│   │   │   │   ├── metrics/page.tsx
│   │   │   │   ├── logs/page.tsx
│   │   │   │   ├── alerts/page.tsx
│   │   │   │   └── reports/page.tsx
│   │   │   └── layout.tsx
│   │   ├── components/
│   │   │   ├── ui/                     # Komponenty shadcn/ui
│   │   │   ├── forms/
│   │   │   │   ├── DeviceForm.tsx
│   │   │   │   └── AlertRuleForm.tsx
│   │   │   ├── charts/
│   │   │   │   ├── LineChart.tsx
│   │   │   │   └── HeatMap.tsx
│   │   │   └── tables/
│   │   │       └── DeviceTable.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   ├── useDevices.ts
│   │   │   └── useMetrics.ts
│   │   ├── lib/
│   │   │   ├── api.ts                  # Instancja Axios
│   │   │   ├── auth.ts                 # Funkcje pomocnicze autentykacji
│   │   │   ├── tracing.ts              # OpenTelemetry
│   │   │   └── utils.ts
│   │   └── types/
│   │       ├── device.ts
│   │       └── metric.ts
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   └── Dockerfile
├── infrastructure/
│   ├── docker/                          # Tylko dla lokalnego DevContainera
│   │   ├── docker-compose.dev.yml
│   │   └── init-scripts/
│   │       ├── postgres-init.sql
│   │       └── timescale-init.sql
│   ├── kubernetes/                      # Surowe manifesty K8s (backup)
│   │   ├── namespace.yaml
│   │   ├── postgres.yaml
│   │   └── ...
│   ├── helm/                            # PODSTAWOWA metoda wdrożenia
│   │   └── sotp/
│   │       ├── Chart.yaml
│   │       ├── values.yaml
│   │       ├── values-dev.yaml
│   │       ├── values-prod.yaml
│   │       └── templates/
│   │           ├── _helpers.tpl
│   │           ├── backend-deployment.yaml
│   │           ├── backend-service.yaml
│   │           ├── celery-worker.yaml
│   │           ├── celery-beat.yaml
│   │           ├── frontend-deployment.yaml
│   │           ├── postgres.yaml
│   │           ├── timescale.yaml
│   │           ├── redis.yaml
│   │           ├── vault.yaml
│   │           ├── prometheus.yaml
│   │           ├── loki.yaml
│   │           ├── tempo.yaml
│   │           ├── grafana.yaml
│   │           ├── ingress.yaml
│   │           └── migrations-job.yaml
│   ├── argocd/
│   │   ├── application.yaml            # Definicja aplikacji ArgoCD
│   │   └── project.yaml
│   ├── prometheus/
│   │   ├── prometheus.yaml
│   │   └── rules/
│   │       ├── alerts.yaml
│   │       └── recording.yaml
│   ├── grafana/
│   │   ├── dashboards/
│   │   │   ├── network-overview.json
│   │   │   ├── device-details.json
│   │   │   ├── system-health.json
│   │   │   └── observability.json      # Zunifikowany PLT
│   │   └── datasources/
│   │       └── datasources.yaml
│   ├── loki/
│   │   └── config.yaml
│   ├── tempo/
│   │   └── config.yaml
│   ├── vault/
│   │   ├── config.json
│   │   └── policies/
│   │       ├── backend-policy.hcl
│   │       └── k8s-auth.hcl
│   └── linkerd/                         # Faza 5
│       └── service-profiles/
├── docs/
│   ├── 00-OVERVIEW.md                   # Przegląd projektu
│   ├── 01-REQUIREMENTS.md               # Pełne wymagania
│   ├── 02-USER_STORIES.md               # Wszystkie historyjki użytkownika
│   ├── 03-ARCHITECTURE.md               # Diagramy C4
│   ├── 04-API.md                        # Dokumentacja API
│   ├── 05-DATABASE.md                   # Schemat bazy danych
│   ├── 06-DEPLOYMENT.md                 # Przewodnik wdrożeniowy
│   ├── 07-OBSERVABILITY.md              # Przewodnik po stosie PLT
│   ├── 08-GITOPS.md                     # Przepływ pracy GitOps
│   ├── 09-SECURITY.md                   # Praktyki bezpieczeństwa
│   ├── 10-TESTING.md                    # Strategia testowania
│   ├── 11-DISASTER_RECOVERY.md          # Procedury DR
│   ├── 12-TROUBLESHOOTING.md            # Rozwiązywanie problemów
│   └── 99-ADR/                          # Decyzje architektoniczne
│       ├── 001-why-kubernetes.md
│       ├── 002-why-gitops.md
│       └── 003-why-service-mesh.md
├── scripts/
│   ├── setup.sh                         # Wstępna konfiguracja
│   ├── k3d-cluster.sh                   # Tworzenie klastra K3d
│   ├── install-argocd.sh                # Instalacja ArgoCD
│   ├── install-linkerd.sh               # Instalacja Linkerd
│   ├── backup.sh                        # Backup baz danych
│   ├── restore.sh                       # Odtwarzanie z backupu
│   ├── seed-demo-data.py                # Dane demonstracyjne
│   └── generate-secrets.sh              # Generowanie sekretów
├── .github/
│   └── workflows/
│       ├── ci.yml                       # Testowanie i Budowanie
│       ├── deploy-dev.yml               # Wdrożenie na dev
│       ├── deploy-prod.yml              # Wdrożenie na prod
│       └── security-scan.yml            # Cotygodniowe skanowanie bezp.
├── .gitignore
├── .env.example
├── Makefile                             # Polecenia pomocnicze
└── README.md
```

---

### Stos Technologiczny

|**Warstwa**|**Technologia**|**Uzasadnienie**|
|---|---|---|
|**Orkiestracja**|K3d (K3s) + Helm|Lekki K8s do lokalnego developmentu. Gotowy na produkcję. Helm standaryzuje wdrożenia.|
|**GitOps**|ArgoCD|Deklaratywne wdrożenia (pull-based CD). Standard branżowy. Auto-synchronizacja, rollback, wykrywanie dryfu.|
|**Service Mesh**|Linkerd (Faza 5)|Automatyczne mTLS, metryki L7, odporność. Lżejszy niż Istio.|
|**Frontend**|Next.js 14 + React + Tailwind|Nowoczesny, szybki, przyjazny SEO. shadcn/ui dla komponentów.|
|**Backend**|FastAPI + Python 3.11+|Asynchroniczne I/O, auto-dokumentacja OpenAPI, walidacja Pydantic, wsparcie OpenTelemetry.|
|**Kolejka Zadań**|Celery + Redis|Rozproszone wykonywanie zadań. Idealne do odpytywania tysięcy urządzeń.|
|**Bazy Danych**|PostgreSQL 16 + TimescaleDB 2.13|Postgres dla inwentarza, TimescaleDB dla szeregów czasowych. Jeden język zapytań.|
|**Sekrety**|HashiCorp Vault|Dynamiczne sekrety, szyfrowanie jako usługa, logowanie audytowe. Standard branżowy.|
|**Obserwowalność**|||
|- Metryki|Prometheus + Alertmanager|De-facto standard. Potężny PromQL. Natywna integracja z K8s.|
|- Logi|Loki + Promtail|"Prometheus dla logów". Niski koszt. Zapytania oparte na etykietach.|
|- Ślady|Tempo|Rozproszony tracing. Natywny dla OpenTelemetry. Widoczność pełnego cyklu życia żądania.|
|- Wizualizacja|Grafana|Zunifikowany dashboard dla metryk, logów i śladów. Standard branżowy.|
|**Kolektory**|icmplib, pysnmp, netmiko, textfsm|Biblioteki Python dla ICMP, SNMP, SSH, parsowania.|
|**CI/CD**|GitHub Actions|Natywna integracja z GitHub. Darmowe dla publicznych repozytoriów.|
|**Środ. Deweloperskie**|VS Code DevContainers|Spójne środowisko deweloperskie. Koniec z "u mnie działa".|
|**ML/AI (Faza 5)**|TimescaleDB Toolkit + Prophet|Wbudowane funkcje ML. Prognozowanie szeregów czasowych.|
|**Load Balancer**|Traefik (K8s Ingress Controller)|Dynamiczna konfiguracja. Automatyczne SSL (Let's Encrypt). Eksport metryk.|

---

### Kompletny Podział na Fazy (Zaktualizowane Role)

**Zespół:**

- **Osoba 1 (Lider DevOps):** Odpowiedzialny za platformę, infrastrukturę (K8s, Helm), CI/CD, GitOps (ArgoCD), stos obserwowalności (PLT), bezpieczeństwo (Vault, Linkerd).
    
- **Osoba 2 (Frontend Developer):** Odpowiedzialny za całe UI/UX (Next.js, React, Tailwind).
    
- **Osoba 3 (Specjalista ds. Kolektorów):** Odpowiedzialny za logikę zbierania danych (ICMP, SNMP, SSH - `pysnmp`, `netmiko`).
    
- **Osoba 4 (Backend Developer):** Odpowiedzialny za aplikację (FastAPI), API, logikę biznesową, modele baz danych (SQLAlchemy), schematy (Pydantic) i definicje zadań Celery.
    

#### FAZA 0: Fundamenty i Proof of Concept (1 Tydzień)

**Cel:** Walidacja kluczowych koncepcji przed dużą inwestycją czasową.

**0.1 Konfiguracja Środowiska (1 dzień)**

- **Odpowiedzialni:** Wszyscy
    
- **Zadania:** Instalacja narzędzi, inicjalizacja Git, konfiguracja DevContainer.
    
- **Rezultaty:** Działający DevContainer, `Makefile`, `README.md`.
    
- **Kryteria Sukcesu:** `make setup` działa; wszyscy mają identyczne środowisko.
    

**0.2 POC: Kolektor ICMP + Prometheus + Grafana (2 dni)**

- **Odpowiedzialny:** Osoba 3 (Specjalista ds. Kolektorów)
    
- **Cel:** Udowodnienie, że potrafimy zbierać metryki i je wizualizować (na prostym Docker Compose).
    
- **Zadania:** Skrypt Pythona (`icmplib`), `docker-compose.yml` (Prometheus, Grafana), dashboard.
    
- **Rezultaty:** Działający skrypt POC, pliki konfiguracyjne, dashboard.
    
- **Kryteria Sukcesu:** Metryki widoczne w Grafanie; dashboard reaguje na zmiany w sieci.
    

**0.3 Definicja Wymagań (2 dni)**

- **Odpowiedzialni:** Wszyscy (sesja warsztatowa)
    
- **Zadania:** Definicja Historyjek Użytkownika (30+), Wymagań Funkcjonalnych i Niefunkcjonalnych, Decyzji Architektonicznych (ADR).
    
- **Rezultaty:** `docs/01-REQUIREMENTS.md`, `docs/02-USER_STORIES.md`, `docs/99-ADR/`.
    
- **Kryteria Sukcesu:** Wymagania zatwierdzone; ADR dokumentują kluczowe decyzje.
    

---

#### FAZA 1: MVP - Fundamenty Kubernetes (3-4 Tygodnie)

**Cel:** Działająca aplikacja na Kubernetes z podstawowym CRUD i monitoringiem.

**1.1 Konfiguracja Lokalnego Klastra Kubernetes (2 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Skrypt `k3d-cluster.sh`, konfiguracja portów, instalacja `metrics-server`, lokalne repozytorium obrazów.
    
- **Rezultaty:** Skrypt do tworzenia klastra, wpisy w `Makefile`, dokumentacja wdrożenia.
    
- **Kryteria Sukcesu:** Klaster K3d działa; można wysyłać obrazy do lokalnego rejestru.
    

**1.2 Stworzenie Helm Chart (3 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Stworzenie struktury `helm create`, definicja `values.yaml`, stworzenie szablonów dla wszystkich komponentów (backend, frontend, bazy danych, obserwowalność).
    
- **Rezultaty:** Kompletny Helm chart w `infrastructure/helm/sotp/`.
    
- **Kryteria Sukcesu:** `helm lint .` przechodzi; `helm install ...` wdraża wszystkie pody.
    

**1.3 Schemat Bazy Danych i Migracje (2 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Definicja modeli SQLAlchemy; konfiguracja Alembic dla wielu baz (Postgres + Timescale); stworzenie początkowych migracji.
    
- **Zadanie (Lider DevOps):** Stworzenie K8s Job (`migrations-job.yaml`) w Helm charcie do automatycznego uruchamiania migracji.
    
- **Rezultaty:** `backend/app/models/*.py`, `backend/alembic/versions/*`, `docs/05-DATABASE.md`.
    
- **Kryteria Sukcesu:** Migracje są idempotentne; Job uruchamia się poprawnie przed startem aplikacji.
    

**1.4 Implementacja Rdzenia Backend API (4 dni)**

- **Odpowiedzialny:** Osoba 4 (Backend Developer)
    
- **Zadania:** Konfiguracja `main.py` (FastAPI), implementacja endpointów CRUD dla urządzeń, implementacja warstwy serwisowej (`device_service.py`) z logiką biznesową i walidacją.
    
- **Rezultaty:** `backend/app/main.py`, `.../api/v1/devices.py`, `.../services/device_service.py`, `.../schemas/device.py`.
    
- **Kryteria Sukcesu:** Endpointy CRUD działają; walidacja Pydantic działa; dokumentacja OpenAPI jest kompletna.
    

**1.5 Produkcyjna Implementacja Kolektora ICMP (3 dni)**

- **Odpowiedzialny:** Osoba 3 (Specjalista ds. Kolektorów)
    
- **Zadania:** Implementacja logiki `ICMPCollector` (z `icmplib` i `tenacity` for retries).
    
- **Zadanie (Osoba 4):** Definicja zadań Celery (`poll_device_icmp`, `poll_all_devices_icmp`) i logiki zapisu do TimescaleDB.
    
- **Rezultaty:** `.../collectors/icmp_collector.py`, `.../tasks/monitoring_tasks.py`.
    
- **Kryteria Sukcesu:** Metryki ICMP są poprawnie zbierane i zapisywane w TimescaleDB co 30 sekund.
    

**1.6 Podstawowy Interfejs Użytkownika (Frontend) (5 dni)**

- **Odpowiedzialny:** Osoba 2 (Frontend Developer)
    
- **Zadania:** Konfiguracja Next.js, layout (Sidebar/Navbar), strona listy urządzeń (`DeviceTable.tsx`), formularz (`DeviceForm.tsx`), klient API (`lib/api.ts`).
    
- **Rezultaty:** Działająca strona `/devices` pozwalająca na pełny CRUD.
    
- **Kryteria Sukcesu:** Można dodawać, edytować i usuwać urządzenia przez UI; stany ładowania/błędów są obsłużone.
    

**1.7 Testowanie i Potok CI (3 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps - Potoki) i Wszyscy (Pisanie Testów)
    
- **Zadania:** Pisanie testów jednostkowych i integracyjnych (Backend/Frontend); Stworzenie potoku `ci.yml` (Lint, Test, Build, Scan); Konfiguracja Codecov.
    
- **Rezultaty:** `backend/tests/`, `frontend/tests/`, `.github/workflows/ci.yml`.
    
- **Kryteria Sukcesu:** Pokrycie testami backendu > 80%; Potok CI automatycznie blokuje błędny kod.
    

---

#### FAZA 2: Bezpieczeństwo i Zaawansowany Monitoring (3 Tygodnie)

**Cel:** Zabezpieczenie aplikacji i rozbudowa możliwości zbierania danych.

**2.1 Autentykacja i Autoryzacja (RBAC) (4 dni)**

- **Odpowiedzialny:** Osoba 4 (Backend Developer)
    
- **Zadania:** Implementacja JWT (access/refresh), endpointy `/login`, `/register`, hashowanie haseł, zależności FastAPI do ochrony endpointów w oparciu o role.
    
- **Zadanie (Osoba 2):** Stworzenie stron logowania/rejestracji, implementacja "Protected Routes" i zarządzanie stanem sesji (Zustand).
    
- **Rezultaty:** `.../api/v1/auth.py`, `.../core/security.py`, `frontend/(auth)/login/page.tsx`.
    
- **Kryteria Sukcesu:** Endpointy są chronione; przepływ logowania działa; użytkownik jest wylogowywany po wygaśnięciu tokena.
    

**2.2 Pełna Integracja z HashiCorp Vault (3 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps - Infrastruktura) i Osoba 4 (Backend Developer - Aplikacja)
    
- **Zadania (DevOps):** Wdrożenie Vault i Vault Secrets Injector w K8s; konfiguracja ról i polityk.
    
- **Zadania (Backend):** Stworzenie `VaultService` (`hvac`); modyfikacja `config.py` do pobierania sekretów z Vault przy starcie (zamiast envars).
    
- **Rezultaty:** `.../services/vault_service.py`; adnotacje Vault w `backend-deployment.yaml`.
    
- **Kryteria Sukcesu:** Aplikacja nie przechowuje żadnych haseł w `values.yaml`; sekrety są wstrzykiwane dynamicznie.
    

**2.3 Implementacja Kolektora SNMP (5 dni)**

- **Odpowiedzialny:** Osoba 3 (Specjalista ds. Kolektorów)
    
- **Zadania:** Implementacja logiki `SNMPCollector` (`pysnmp`) wspierającej v2c i v3; pobieranie poświadczeń z Vault.
    
- **Zadanie (Osoba 4):** Definicja zadania `poll_device_snmp(device_id)` i logiki zapisu metryk (CPU, RAM, Interfejsy) do TimescaleDB.
    
- **Rezultaty:** `.../collectors/snmp_collector.py`.
    
- **Kryteria Sukcesu:** Dane SNMPv3 są poprawnie zbierane i zapisywane w TimescaleDB.
    

**2.4 Frontend - UI Metryk (4 dni)**

- **Odpowiedzialny:** Osoba 2 (Frontend Developer) i Osoba 4 (Backend Developer)
    
- **Zadania (Backend):** Stworzenie endpointu API `GET /api/v1/devices/{id}/metrics` do pobierania danych z TimescaleDB.
    
- **Zadania (Frontend):** Dodanie zakładki "Metryki" na stronie urządzenia; implementacja wykresów (`recharts`) dla ICMP, CPU, RAM, Ruchu Sieciowego; dodanie wyboru zakresu czasu.
    
- **Rezultaty:** `.../api/v1/metrics.py`; zaktualizowana strona `frontend/devices/[id]/page.tsx`.
    
- **Kryteria Sukcesu:** Wykresy na stronie urządzenia pokazują dane historyczne i aktualizują się po zmianie zakresu czasu.
    

**2.5 Dashboardy Grafana (2 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Wdrożenie Grafany (przez Helm); automatyczny provisioning źródeł danych (Prometheus, TimescaleDB); stworzenie dashboardów "as code" (`network-overview.json`, `device-details.json`, `system-health.json`).
    
- **Rezultaty:** `infrastructure/grafana/dashboards/*.json`.
    
- **Kryteria Sukcesu:** Dashboardy są automatycznie ładowane przy starcie Grafany; `device-details.json` poprawnie filtruje dane.
    

---

#### FAZA 3: Obserwowalność i Automatyzacja CD (GitOps) (3 Tygodnie)

**Cel:** Osiągnięcie pełnej obserwowalności (stos PLT) i wdrożenie wzorca GitOps.

**3.1 Filar Obserwowalności 1: Metryki (Prometheus) (2 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Wdrożenie `prometheus-operator`; konfiguracja `ServiceMonitor` do automatycznego scrapowania backendu; wdrożenie `Alertmanager`.
    
- **Rezultaty:** Działający stos Prometheus + Alertmanager.
    
- **Kryteria Sukcesu:** Metryki API są automatycznie zbierane.
    

**3.2 Filar Obserwowalności 2: Logi (Loki) (3 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Wdrożenie `Loki` i `Promtail`; konfiguracja `Promtail` (DaemonSet) do zbierania logów ze wszystkich podów w namespace.
    
- **Rezultaty:** Działający stos Loki; logi widoczne w Grafanie.
    
- **Kryteria Sukcesu:** Można przeszukiwać logi wszystkich podów z poziomu Grafany.
    

**3.3 Filar Obserwowalności 3: Ślady (Tempo) (4 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps - Infrastruktura) i Osoba 4 (Backend Developer - Aplikacja)
    
- **Zadania (DevOps):** Wdrożenie `Grafana Tempo` (Helm); konfiguracja źródeł danych w Grafanie (Tempo + powiązanie z Loki).
    
- **Zadania (Backend):** Instrumentacja kodu (`opentelemetry-distro`, `...-fastapi`, `...-celery`, `...-sqlalchemy`); konfiguracja `observability.py` do wysyłania śladów do Tempo.
    
- **Rezultaty:** `.../core/observability.py`; zaktualizowane `requirements.txt`.
    
- **Kryteria Sukcesu:** Można prześledzić pełny cykl życia żądania (API -> Celery -> Baza Danych) i przejść ze śladu do logów.
    

**3.4 Wdrożenie GitOps (ArgoCD) (5 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Stworzenie **drugiego** repozytorium `sotp-k8s-config`; przeniesienie tam Helm charta; instalacja ArgoCD; stworzenie manifestu `Application` ArgoCD.
    
- **Zadanie (Aktualizacja Potoku):** Modyfikacja `deploy-prod.yml`, aby po zbudowaniu obrazu aktualizował `image.tag` w `values.yaml` w repozytorium `sotp-k8s-config`.
    
- **Rezultaty:** Dwa repozytoria; działająca instancja ArgoCD; w pełni zautomatyzowany potok CD (GitOps).
    
- **Kryteria Sukcesu:** `git push` do `sotp-backend` powoduje automatyczne wdrożenie nowej wersji na klastrze przez ArgoCD.
    

---

#### FAZA 4: Funkcjonalność Produkcyjna (3-4 Tygodnie)

**Cel:** Ukończenie implementacji funkcji produktu.

**4.1 Kolektor SSH (Netmiko) (5 dni)**

- **Odpowiedzialny:** Osoba 3 (Logika Kolektora) i Osoba 4 (Endpoint API)
    
- **Zadania (Osoba 3):** Implementacja `SSHCollector` (`netmiko`) i parserów `TextFSM`.
    
- **Zadania (Osoba 4):** Stworzenie endpointu API `POST .../execute` (z białą listą poleceń), kolejkowanie przez Celery, zwracanie sparsowanego JSON.
    
- **Zadanie (Osoba 2):** Stworzenie zakładki "Konsola" w UI.
    
- **Rezultaty:** `.../collectors/ssh_collector.py`, `.../api/v1/commands.py`, `frontend/.../console/page.tsx`.
    
- **Kryteria Sukcesu:** Można wykonać `show version` z UI i zobaczyć sparsowany JSON; próba wykonania `config t` jest blokowana.
    

**4.2 Kolektor Syslog i Logi Audytowe (4 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps - Syslog) i Osoba 4 (Backend Developer - Audyt)
    
- **Zadania (DevOps):** Konfiguracja Promtail do odbierania Sysloga z urządzeń sieciowych i przesyłania do Loki.
    
- **Zadania (Backend):** Implementacja modelu `AuditLog` (Postgres); stworzenie middleware FastAPI do automatycznego logowania wszystkich żądań POST/PUT/DELETE.
    
- **Zadanie (Osoba 2):** Stworzenie UI (`/logs`) do przeglądania logów Syslog (Loki) i Audytowych (Postgres).
    
- **Rezultaty:** Zaktualizowany `promtail/config.yaml`; `.../models/audit_log.py`; `frontend/.../logs/page.tsx`.
    
- **Kryteria Sukcesu:** Logi z routera są widoczne w Loki; usunięcie urządzenia przez UI tworzy wpis w tabeli `audit_logs`.
    

**4.3 System Raportowania (3 dni)**

- **Odpowiedzialny:** Osoba 4 (Backend Developer) i Osoba 2 (Frontend Developer)
    
- **Zadania (Backend):** Stworzenie API (`.../reports/generate`), logiki agregacji danych z TimescaleDB, generowanie PDF (`WeasyPrint`) lub CSV.
    
- **Zadania (Frontend):** Stworzenie UI (`/reports`) do wyboru typu raportu, zakresu dat i pobierania pliku.
    
- **Rezultaty:** `.../services/report_service.py`; `frontend/.../reports/page.tsx`.
    
- **Kryteria Sukcesu:** Można wygenerować i pobrać raport dostępności PDF z ostatnich 7 dni.
    

**4.4 Backup i Disaster Recovery (3 dni)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Stworzenie `CronJob` K8s do codziennego backupu baz (`pg_dump`, `ts-dump`) do S3 (np. MinIO); spisanie i przetestowanie procedury odtwarzania.
    
- **Rezultaty:** `templates/backup-job.yaml`; `docs/11-DISASTER_RECOVERY.md`.
    
- **Kryteria Sukcesu:** Backup jest wykonywany automatycznie; procedura odtwarzania jest przetestowana i działa.
    

---

#### FAZA 5: Wizja i Dalszy Rozwój (Ongoing)

**Cel:** Wdrożenie flagowych funkcji, które wyróżniają projekt.

**5.1 Wdrożenie Service Mesh (Linkerd)**

- **Odpowiedzialny:** Osoba 1 (Lider DevOps)
    
- **Zadania:** Instalacja Linkerd; wstrzyknięcie proxy do podów aplikacji; konfiguracja `ServiceProfile`.
    
- **Rezultat (Flagowy):** Automatyczne mTLS między wszystkimi serwisami; "Golden Metrics" (RPS, latency, success rate) dla całego ruchu.
    

**5.2 Automatyzacja w Zamkniętej Pętli (Closed-Loop Automation)**

- **Odpowiedzialni:** Osoba 1 (DevOps), Osoba 4 (Backend), Osoba 3 (Kolektor)
    
- **Zadania:**
    
    1. (DevOps) Konfiguracja Alertmanager, by wysyłał webhooki do API.
        
    2. (Backend) Stworzenie endpointu `/api/v1/webhooks/remediate`, który waliduje alert i kolejkuje zadanie Celery.
        
    3. (Kolektor) Implementacja logiki zadania (`tasks.remediate_interface`) używając Netmiko.
        
- **Rezultat (Flagowy):** System, który nie tylko informuje o problemie, ale sam próbuje go naprawić (np. restartując interfejs).
    

**5.3 Anomalia i Predykcja (AI/ML)**

- **Odpowiedzialny:** Osoba 4 (Backend Developer)
    
- **Zadania:** Instalacja `TimescaleDB Toolkit`; stworzenie zadania Celery (`tasks.predict_trends()`) używającego wbudowanych funkcji (np. `Prophet`) do generowania predykcji i wykrywania anomalii.
    
- **Rezultat (Flagowy):** Przejście od monitoringu reaktywnego do proaktywnego ("coś się _zaraz_ zepsuje").
    

**5.4 Zarządzanie Konfiguracją Sieci (GitOps dla Sieci)**

- **Odpowiedzialny:** Osoba 3 (Kolektor) i Osoba 4 (Backend)
    
- **Zadania (Osoba 3):** Implementacja logiki `backup_config()` (używając Netmiko).
    
- **Zadania (Osoba 4):** Stworzenie zadania Celery, które uruchamia logikę i zapisuje konfigurację do repozytorium `sotp-k8s-config`.
    
- **Rezultat (Flagowy):** Możliwość wykonania `git diff` na konfiguracji urządzenia; alertowanie o "dryfie" konfiguracji.
    

---

### Kluczowe Metryki Sukcesu

|**Metryka**|**Cel**|
|---|---|
|System Uptime|99.5%+|
|Czas Odpowiedzi API|< 200ms (p95)|
|Wskaźnik Sukcesu Pollingu|> 99%|
|Wskaźnik Fałszywych Pozytywów (Alerty)|< 5%|
|Pokrycie Testami (Backend)|> 80%|
|Podatności Bezpieczeństwa|0 Krytycznych, 0 Wysokich|
|Częstotliwość Wdrożeń|Codziennie (dzięki GitOps)|
|MTTR (Mean Time To Recovery)|< 15 minut (automatyczne rollbacki)|


### Szacowany Timeline

|**Faza**|**Czas**|**Odpowiedzialni Główne**|
|---|---|---|
|Faza 0: POC|1 tydzień|Wszyscy|
|Faza 1: MVP & K8s|3-4 tygodnie|Wszyscy (podział: DevOps, Backend, Frontend, Kolektory)|
|Faza 2: Bezpieczeństwo i Monitoring|3 tygodnie|Wszyscy (podział j.w.)|
|Faza 3: Obserwowalność & GitOps|3 tygodnie|Lider DevOps (głównie), Backend (instrumentacja)|
|Faza 4: Funkcjonalność Produkcyjna|3-4 tygodnie|Wszyscy (podział j.w.)|
|Faza 5: Wizja (Funkcje Flagowe)|3-4 tygodnie|Wszyscy (podział j.w.)|
|**TOTAL**|**~16-19 tygodni**|**4-osobowy zespół**|