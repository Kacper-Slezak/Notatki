---
typ: architektura
projekt: 00 SOTP Dashboard
---

#  Struktura Repozytorium i Plików

Projekt podzielony jest na dwa główne repozytoria zgodnie z filozofią [[GitOps]]:
1. **sotp-backend** (Kod źródłowy aplikacji).
2. **sotp-k8s-config** (Manifesty wdrożeniowe dla [[ArgoCD]]).

## Drzewo Katalogów (sotp-backend)

```text
sotp/
├── backend/                        # Logika biznesowa ([[Python]]/[[FastAPI]])
│   ├── app/
│   │   ├── api/                    # Endpointy REST API
│   │   ├── core/                   # Konfiguracja, [[Security]], [[Observability]]
│   │   ├── models/                 # Modele ORM ([[SQLAlchemy]])
│   │   ├── schemas/                # Schematy walidacji ([[Pydantic]])
│   │   ├── services/               # Logika biznesowa (Service Layer)
│   │   ├── collectors/             # Logika zbierania danych ([[ICMP]], [[SNMP]])
│   │   ├── tasks/                  # Zadania w tle ([[Celery]])
│   │   └── utils/
│   ├── alembic/                    # Migracje bazy danych
│   ├── tests/                      # Testy jednostkowe i integracyjne ([[Pytest]])
│   ├── Dockerfile                  # Multi-stage build
│   └── pyproject.toml              # Zarządzanie zależnościami ([[Poetry]])
│
├── frontend/                       # Interfejs użytkownika
│   ├── src/
│   │   ├── app/                    # Routing ([[Next.js]] App Router)
│   │   ├── components/             # Komponenty UI ([[React]]/shadcn)
│   │   ├── lib/                    # Klient API, utils
│   │   └── types/                  # Definicje typów [[TypeScript]]
│   └── Dockerfile
│
├── infrastructure/                 # Kod infrastruktury
│   ├── docker/                     # Środowisko lokalne ([[Docker Compose]])
│   ├── helm/                       # Szablony wdrożeniowe ([[Helm]])
│   │   └── sotp/
│   │       ├── templates/          # Pliki YAML K8s
│   │       └── values.yaml         # Konfiguracja domyślna
│   ├── argocd/                     # Definicje aplikacji [[ArgoCD]]
│   ├── prometheus/                 # Reguły alertów
│   ├── grafana/                    # Dashboardy jako kod (JSON)
│   └── vault/                      # Polityki bezpieczeństwa [[HashiCorp Vault]]
│
├── docs/                           # Dokumentacja projektowa (ADR, API)
├── scripts/                        # Skrypty pomocnicze (setup, backup)
└── .github/workflows/              # Potoki CI/CD ([[GitHub Actions]])