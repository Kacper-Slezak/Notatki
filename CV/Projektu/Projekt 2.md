#  SOTP - System Observability & Telemetry Platform

## Kompletny Plan Wykonawczy - Master Document v2.0

---

##  Architektura Wysokopoziomowa

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                      │
│  React/Next.js Frontend + Grafana Dashboards                │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   API GATEWAY LAYER                          │
│  Traefik (Load Balancer + SSL) → FastAPI (REST + WebSocket) │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  APPLICATION LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Inventory  │  │  Auth/RBAC   │  │   Alerting   │      │
│  │   Service    │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   CACHE & QUEUE LAYER                        │
│  Redis (Cache + Session) + Celery (Task Queue)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  COLLECTOR WORKERS                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │   SNMP   │ │   ICMP   │ │   SSH    │ │  Syslog  │       │
│  │ Collector│ │ Collector│ │ Collector│ │ Collector│       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   DATA LAYER                                 │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │  PostgreSQL     │  │  TimescaleDB    │                  │
│  │  (Inventory)    │  │  (Time-Series)  │                  │
│  └─────────────────┘  └─────────────────┘                  │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │  Loki           │  │  Vault          │                  │
│  │  (Logs)         │  │  (Secrets)      │                  │
│  └─────────────────┘  └─────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

---

##  Struktura Projektu

```
sotp/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── devices.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── metrics.py
│   │   │   │   ├── logs.py
│   │   │   │   └── users.py
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── database.py
│   │   │   └── exceptions.py
│   │   ├── models/
│   │   │   ├── device.py
│   │   │   ├── user.py
│   │   │   ├── audit_log.py
│   │   │   └── alert.py
│   │   ├── schemas/
│   │   │   ├── device.py
│   │   │   ├── user.py
│   │   │   ├── metric.py
│   │   │   └── auth.py
│   │   ├── services/
│   │   │   ├── device_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── audit_service.py
│   │   │   └── vault_service.py
│   │   ├── collectors/
│   │   │   ├── base.py
│   │   │   ├── icmp_collector.py
│   │   │   ├── snmp_collector.py
│   │   │   ├── ssh_collector.py
│   │   │   └── syslog_collector.py
│   │   ├── tasks/
│   │   │   ├── celery_app.py
│   │   │   ├── monitoring_tasks.py
│   │   │   └── alert_tasks.py
│   │   └── utils/
│   │       ├── parsers.py
│   │       ├── validators.py
│   │       └── helpers.py
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── alembic/
│   │   └── versions/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── Dockerfile
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   ├── (dashboard)/
│   │   │   │   ├── devices/
│   │   │   │   ├── metrics/
│   │   │   │   ├── logs/
│   │   │   │   └── alerts/
│   │   │   └── layout.tsx
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   ├── forms/
│   │   │   ├── charts/
│   │   │   └── tables/
│   │   ├── hooks/
│   │   ├── lib/
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   └── utils.ts
│   │   └── types/
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
├── infrastructure/
│   ├── docker/
│   │   ├── docker-compose.yml
│   │   ├── docker-compose.dev.yml
│   │   ├── docker-compose.prod.yml
│   │   └── init-scripts/
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   ├── rules/
│   │   │   ├── alerts.yml
│   │   │   └── recording_rules.yml
│   │   └── alertmanager.yml
│   ├── grafana/
│   │   ├── dashboards/
│   │   │   ├── network-overview.json
│   │   │   ├── device-details.json
│   │   │   └── system-health.json
│   │   └── datasources/
│   ├── loki/
│   │   └── config.yml
│   ├── promtail/
│   │   └── config.yml
│   ├── nginx/
│   │   ├── nginx.conf
│   │   └── ssl/
│   └── terraform/ (opcjonalnie)
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── REQUIREMENTS.md
│   ├── USER_STORIES.md
│   └── CONTRIBUTING.md
├── scripts/
│   ├── setup.sh
│   ├── backup.sh
│   ├── restore.sh
│   └── generate-secrets.sh
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── build.yml
│       ├── deploy-dev.yml
│       └── deploy-prod.yml
├── .gitignore
├── .env.example
├── Makefile
└── README.md
```

---

##  FAZA 0: Przygotowanie i Proof of Concept

**Czas: 3-5 dni | Priorytet: KRYTYCZNY**

### 0.1 Setup Środowiska Deweloperskiego

**Wykonawca: Wszyscy | Czas: 1 dzień**

#### Zadania:

1. **Instalacja podstawowych narzędzi:**
    
    - Docker & Docker Compose (najnowsze wersje)
    - Python 3.11+ z venv
    - Node.js 20+ LTS z npm/pnpm
    - Git z konfiguracją
    - IDE/Editor (VSCode + rozszerzenia Python/TypeScript)
    - PostgreSQL client (psql, pgAdmin)
    - Redis client (redis-cli)
2. **Inicjalizacja repozytorium:**
    
    - Utworzenie struktury folderów zgodnie z diagramem
    - Konfiguracja .gitignore
    - Dodanie .env.example z wszystkimi wymaganymi zmiennymi
    - Utworzenie README.md z instrukcją quick start
3. **Pre-commit hooks:**
    
    - Black/isort dla Python
    - ESLint/Prettier dla TypeScript
    - Commit message linting
    - Security scanning
4. **Konfiguracja narzędzi deweloperskich:**
    
    - Makefile z podstawowymi komendami (up, down, test, migrate)
    - VSCode workspace settings
    - Debug configurations

#### Deliverables:

-  Działające środowisko deweloperskie na każdej maszynie
-  Zainicjalizowane repozytorium Git
-  Dokumentacja setup w README.md

---

### 0.2 Proof of Concept - Prosty Ping Collector

**Wykonawca: Osoba 3 (Collector) | Czas: 2 dni**

#### Cel:

Udowodnić, że można:

- Zbierać metryki ICMP ping asynchronicznie
- Wysyłać je do Prometheus
- Wyświetlić w Grafanie

#### Zadania:

1. **Implementacja:**
    
    - Stwórz prosty skrypt Python używający `icmplib` lub `aioping`
    - Dodaj listę 3-5 testowych IP (8.8.8.8, 1.1.1.1, etc.)
    - Implementuj async loop pingujący co 30s
    - Zapisuj metryki (latency, packet_loss) do Prometheus Pushgateway
2. **Infrastruktura:**
    
    - Uruchom Prometheus w Dockerze
    - Uruchom Pushgateway w Dockerze
    - Uruchom Grafanę w Dockerze
    - Połącz Grafanę z Prometheusem jako datasource
3. **Wizualizacja:**
    
    - Stwórz prosty dashboard w Grafanie
    - Dodaj panel z wykresem latency dla każdego urządzenia
    - Dodaj panel ze statusem UP/DOWN

#### Kryteria sukcesu:

-  Skrypt działa non-stop bez crashy
-  Metryki są widoczne w Prometheus UI
-  Dashboard w Grafanie pokazuje live dane
-  Możesz "zabić" jedno urządzenie i zobaczyć zmianę na dashboardzie

#### Deliverables:

- `poc/ping_collector.py` - działający skrypt
- `poc/docker-compose.yml` - minimal stack
- `poc/dashboard.json` - eksport dashboardu Grafana
- `poc/README.md` - instrukcja uruchomienia

---

### 0.3 Definicja Requirements

**Wykonawca: Cały zespół | Czas: 1-2 dni**

#### Zadania:

1. **User Stories:**
    
    - Zdefiniuj minimum 30 user stories pogrupowanych w Epics
    - Każda story musi mieć: As a [role], I want [feature], So that [benefit]
    - Dodaj Acceptance Criteria dla każdej story
    - Przypisz story points (1, 2, 3, 5, 8)
2. **Wymagania funkcjonalne:**
    
    - Device Management (CRUD)
    - Monitoring (ICMP, SNMP, SSH)
    - Alerting (Email, Slack, Webhook)
    - Authentication & Authorization (JWT, RBAC)
    - Audit Logging
    - Reporting (CSV export, PDF reports)
3. **Wymagania niefunkcjonalne:**
    
    - Performance: System musi obsłużyć 1000 urządzeń z polling co 30s
    - Availability: 99.5% uptime
    - Security: OWASP Top 10 compliance
    - Scalability: Horizontal scaling możliwy
    - Backup: Daily automated backups z 30-day retention
4. **Technology Stack Decision:**
    
    - Uzasadnij wybór każdej technologii
    - Porównaj alternatywy (np. FastAPI vs Django, React vs Vue)
    - Dokumentuj trade-offs

#### Deliverables:

- `docs/REQUIREMENTS.md` - pełna specyfikacja
- `docs/USER_STORIES.md` - wszystkie user stories z AC
- `docs/TECH_STACK.md` - uzasadnienie wyborów
- `docs/ARCHITECTURE.md` - diagramy C4 model (Context, Container, Component)

---

##  FAZA 1: MVP - Infrastruktura i CRUD

**Czas: 2-3 tygodnie | Priorytet: WYSOKI**

### 1.1 Docker Compose - Full Stack Setup

**Wykonawca: Ty (DevOps) | Czas: 3 dni**

#### Zadania:

1. **Stwórz docker-compose.yml z usługami:**
    
    - Traefik (reverse proxy + SSL)
    - FastAPI backend
    - Celery worker
    - Celery beat (scheduler)
    - PostgreSQL (inventory data)
    - TimescaleDB (time-series metrics)
    - Redis (cache + celery broker)
    - Vault (secrets management)
    - Prometheus + Alertmanager
    - Grafana
    - Loki + Promtail
    - Frontend (React/Next.js)
2. **Networking:**
    
    - Zdefiniuj bridge network
    - Skonfiguruj service discovery (Docker DNS)
    - Ustaw hostname dla każdego serwisu
3. **Volumes:**
    
    - Named volumes dla persistent data
    - Bind mounts dla config files
    - Backup strategy
4. **Health Checks:**
    
    - Każdy serwis musi mieć healthcheck
    - Zdefiniuj depends_on z condition: service_healthy
5. **Environment Variables:**
    
    - Stwórz .env.example z wszystkimi zmiennymi
    - Użyj ${VARIABLE:-default} syntax
    - Dokumentuj każdą zmienną
6. **Init Scripts:**
    
    - TimescaleDB: utworzenie hypertable dla metryk
    - PostgreSQL: utworzenie baz danych
    - Vault: inicjalizacja i unseal
    - Prometheus: import alerting rules
    - Grafana: provisioning datasources i dashboards

#### Deliverables:

- `infrastructure/docker/docker-compose.yml` - production-ready
- `infrastructure/docker/docker-compose.dev.yml` - development overrides
- `infrastructure/docker/init-scripts/*` - wszystkie init scripts
- `docs/DEPLOYMENT.md` - instrukcja wdrożenia

#### Kryteria sukcesu:

-  `docker-compose up -d` uruchamia cały stack bez błędów
-  Wszystkie serwisy są "healthy" po 2 minutach
-  Możesz zalogować się do każdego serwisu
-  Grafana ma skonfigurowane datasources

---

### 1.2 Database Schema Design

**Wykonawca: Ty (DevOps) | Czas: 2 dni**

#### Zadania:

1. **Projektowanie tabel:**
    
    - **users**: id, username, email, password_hash, role, is_active, created_at
    - **devices**: id, name, ip_address, device_type, vendor, model, location, snmp_config, ssh_config, is_active, created_by, created_at, updated_at, deleted_at
    - **credentials**: id, device_id, credential_type, vault_path (NIE PRZECHOWUJ HASEŁ W DB!)
    - **audit_logs**: id, user_id, action, resource_type, resource_id, details_json, ip_address, timestamp
    - **alerts**: id, device_id, alert_type, severity, message, acknowledged, created_at
    - **alert_rules**: id, name, condition, threshold, notification_channel
2. **TimescaleDB schema:**
    
    - **device_metrics**: time, device_id, metric_type, metric_name, value, labels_jsonb
    - Create hypertable z time dimension
    - Create indexes: (device_id, time), (metric_type, time)
    - Continuous aggregates dla pre-computed queries
3. **Relacje:**
    
    - users 1:N devices (created_by FK)
    - devices 1:N credentials
    - devices 1:N alerts
    - users 1:N audit_logs
4. **Indexes:**
    
    - Wszystkie FK
    - Często wyszukiwane pola (ip_address, username, email)
    - Composite indexes dla common queries
5. **Constraints:**
    
    - UNIQUE na ip_address, username, email
    - CHECK constraints (np. port 1-65535)
    - Foreign key constraints z ON DELETE CASCADE/SET NULL

#### Narzędzia:

- Alembic dla migracji
- dbdiagram.io dla wizualizacji schema
- SQLAlchemy ORM models

#### Deliverables:

- `backend/alembic/versions/001_initial_schema.py` - pierwsza migracja
- `backend/app/models/*.py` - SQLAlchemy models
- `docs/DATABASE_SCHEMA.md` - dokumentacja z diagramami
- `infrastructure/docker/init-scripts/timescale-init.sql`

---

### 1.3 Backend Core - FastAPI Setup

**Wykonawca: Ty (DevOps) | Czas: 3 dni**

#### Zadania:

1. **Struktura aplikacji:**
    
    - Stwórz main.py z FastAPI app
    - Skonfiguruj CORS middleware
    - Dodaj exception handlers
    - Skonfiguruj logging (structlog)
    - Dodaj Prometheus metrics middleware
2. **Configuration Management:**
    
    - Użyj Pydantic Settings
    - Załaduj konfigurację z .env
    - Waliduj wszystkie zmienne środowiskowe przy starcie
    - Stwórz różne profile (dev, staging, prod)
3. **Database Connection:**
    
    - Async SQLAlchemy engine
    - Connection pooling
    - Dependency injection dla session
    - Graceful shutdown
4. **Security Foundation:**
    
    - HTTPS only (w produkcji)
    - Security headers (helmet)
    - Request ID tracking
    - Rate limiting per IP
5. **Health & Readiness Endpoints:**
    
    - `/health` - czy aplikacja działa
    - `/ready` - czy może przyjmować ruch (DB connected?)
    - `/metrics` - Prometheus metrics
6. **OpenAPI Documentation:**
    
    - Automatyczna generacja z FastAPI
    - Dodaj descriptions do wszystkich endpoints
    - Dodaj examples do request/response
    - Skonfiguruj tags

#### Deliverables:

- `backend/app/main.py` - entry point
- `backend/app/core/config.py` - konfiguracja
- `backend/app/core/database.py` - DB setup
- `backend/Dockerfile` - multi-stage build
- `backend/requirements.txt` - dependencies

---

### 1.4 Backend API - Device CRUD

**Wykonawca: Ty (DevOps) | Czas: 3 dni**

#### Zadania:

1. **Implementacja endpointów:**
    
    - `POST /api/v1/devices` - dodaj urządzenie
    - `GET /api/v1/devices` - lista z pagination, filtering, sorting
    - `GET /api/v1/devices/{id}` - szczegóły
    - `PUT /api/v1/devices/{id}` - update
    - `PATCH /api/v1/devices/{id}` - partial update
    - `DELETE /api/v1/devices/{id}` - soft delete
2. **Pydantic Schemas:**
    
    - DeviceCreate - walidacja przy tworzeniu
    - DeviceUpdate - walidacja przy update
    - DeviceResponse - zwracany format
    - DeviceList - lista z metadata (total, page, etc.)
3. **Service Layer:**
    
    - DeviceService z business logic
    - Walidacja IP address (IPv4/IPv6)
    - Sprawdzanie duplikatów
    - Soft delete implementation
4. **Query Features:**
    
    - Pagination (limit, offset)
    - Filtering (is_active, device_type, vendor)
    - Searching (name, ip_address)
    - Sorting (asc/desc po dowolnym polu)
5. **Error Handling:**
    
    - 404 - not found
    - 400 - validation error
    - 409 - conflict (duplicate IP)
    - 500 - internal error

#### Deliverables:

- `backend/app/api/v1/devices.py` - routes
- `backend/app/schemas/device.py` - pydantic models
- `backend/app/services/device_service.py` - business logic
- `backend/tests/test_devices.py` - unit tests

#### Kryteria sukcesu:

-  Wszystkie endpointy działają
-  OpenAPI docs są kompletne
-  Testy jednostkowe przechodzą (min 80% coverage)
-  Możesz zarządzać urządzeniami przez Swagger UI

---

### 1.5 ICMP Collector - Basic Implementation

**Wykonawca: Osoba 3 (Collector) | Czas: 4 dni**

#### Zadania:

1. **Base Collector Class:**
    
    - Abstract base class dla wszystkich collectorów
    - Interfejs: collect(), store(), handle_error()
    - Async implementation
    - Retry logic z exponential backoff
2. **ICMP Collector Implementation:**
    
    - Użyj `icmplib` lub `aioping`
    - Zbieraj: RTT, packet_loss, jitter
    - Timeout handling
    - Concurrent pinging (max 50 równocześnie)
3. **Celery Task:**
    
    - Task: poll_device_icmp(device_id)
    - Periodic task w Celery Beat (co 30s)
    - Task routing (queue dla collectorów)
    - Result backend configuration
4. **Data Storage:**
    
    - Insert do TimescaleDB
    - Batch inserts dla performance
    - Compression po 7 dniach
    - Retention policy (90 dni)
5. **Error Handling:**
    
    - Network unreachable
    - Timeout exceeded
    - Permission denied (raw sockets)
    - Dead letter queue dla failed tasks
6. **Monitoring:**
    
    - Track collector performance
    - Count successful/failed pings
    - Measure collection duration
    - Export metrics do Prometheus

#### Deliverables:

- `backend/app/collectors/base.py` - abstract base
- `backend/app/collectors/icmp_collector.py` - implementacja
- `backend/app/tasks/monitoring_tasks.py` - Celery tasks
- `backend/tests/test_icmp_collector.py` - testy

#### Kryteria sukcesu:

-  Collector działa asynchronicznie
-  Metryki są zapisywane do TimescaleDB
-  Możesz zobaczyć dane w Grafanie
-  System survives 1000+ urządzeń

---

### 1.6 Frontend - Basic UI

**Wykonawca: Osoba 2 (Frontend) | Czas: 5 dni**

#### Zadania:

1. **Setup projektu:**
    
    - Next.js 14 z App Router
    - TypeScript strict mode
    - Tailwind CSS + shadcn/ui
    - React Query dla API calls
    - Zustand dla state management
2. **Layout & Navigation:**
    
    - Top navbar z logo i user menu
    - Sidebar z menu (Devices, Metrics, Logs, Alerts, Settings)
    - Breadcrumbs
    - Dark mode toggle
3. **Device List Page:**
    
    - Table z kolumnami: Name, IP, Type, Status, Actions
    - Pagination controls
    - Search bar (live search)
    - Filters (Type, Status, Vendor)
    - Sorting (klik na header)
    - Add Device button
4. **Device Form (Modal/Slide-over):**
    
    - Pola: Name, IP Address, Type, Vendor, Model, Location
    - Real-time validation
    - Error handling
    - Success/error notifications
5. **Device Details Page:**
    
    - Overview section (basic info)
    - Metrics section (placeholder dla Fazy 2)
    - Configuration section (SNMP/SSH settings)
    - Actions (Edit, Delete, Test Connectivity)
6. **API Integration:**
    
    - Axios/Fetch wrapper z interceptors
    - Error handling (network errors, 401, 403, 500)
    - Loading states
    - Optimistic updates

#### Deliverables:

- `frontend/src/app/(dashboard)/devices/*` - strony
- `frontend/src/components/devices/*` - komponenty
- `frontend/src/lib/api.ts` - API client
- `frontend/Dockerfile` - production build

#### Kryteria sukcesu:

-  Możesz dodać urządzenie przez UI
-  Lista urządzeń ładuje się z API
-  Możesz edytować i usuwać urządzenia
-  UI jest responsywne (mobile-first)
-  Dark mode działa

---

### 1.7 Testing & Quality Assurance

**Wykonawca: Wszyscy | Czas: 2 dni**

#### Zadania:

1. **Backend Tests:**
    
    - Unit tests (pytest) - min 80% coverage
    - Integration tests (testcontainers)
    - API tests (httpx async client)
    - Load tests (locust) - 100 concurrent users
2. **Frontend Tests:**
    
    - Unit tests (Vitest)
    - Component tests (React Testing Library)
    - E2E tests (Playwright) - critical paths
    - Visual regression (Chromatic opcjonalnie)
3. **CI/CD Pipeline:**
    
    - GitHub Actions workflow
    - Lint → Test → Build → Deploy
    - Security scanning (Bandit, Safety, Trivy)
    - Code quality (SonarCloud)
4. **Manual Testing:**
    
    - Test all user flows
    - Cross-browser testing
    - Mobile testing
    - Accessibility testing (WCAG AA)

#### Deliverables:

- `backend/tests/*` - wszystkie testy
- `frontend/tests/*` - wszystkie testy
- `.github/workflows/test.yml` - CI pipeline
- `docs/TESTING.md` - test strategy

---

### 1.8 Documentation & Demo

**Wykonawca: Wszyscy | Czas: 2 dni**

#### Zadania:

1. **API Documentation:**
    
    - OpenAPI spec kompletny
    - Przykłady dla każdego endpointa
    - Authentication guide
    - Rate limiting info
2. **User Documentation:**
    
    - Quick start guide
    - Feature walkthrough z screenshots
    - FAQ
    - Troubleshooting guide
3. **Developer Documentation:**
    
    - Architecture decision records (ADR)
    - Code style guide
    - Contributing guide
    - Local development setup
4. **Demo Preparation:**
    
    - Seed database z testowymi danymi
    - Przygotuj demo scenario
    - Nagraj video walkthrough (opcjonalnie)

#### Deliverables:

- `docs/*` - pełna dokumentacja
- `scripts/seed-demo-data.py` - demo data
- `README.md` - zaktualizowany
- Demo environment gotowy

---

## FAZA 2: Security & Advanced Monitoring

**Czas: 2-3 tygodnie | Priorytet: WYSOKI**

### 2.1 Authentication & Authorization

**Wykonawca: Ty (DevOps) | Czas: 4 dni**

#### Zadania:

1. **JWT Implementation:**
    
    - Access token (15 min expiry)
    - Refresh token (7 days expiry)
    - Token blacklisting
    - Token rotation
2. **User Management:**
    
    - Registration endpoint (z email verification)
    - Login endpoint (z rate limiting)
    - Password reset flow
    - Change password
    - MFA (opcjonalnie - TOTP)
3. **RBAC (Role-Based Access Control):**
    
    - Role: ADMIN, OPERATOR, AUDITOR, READONLY
    - Permission matrix (kto może co robić)
    - Decorators: @require_role, @require_permission
    - API endpoint protection
4. **Security Features:**
    
    - Password hashing (bcrypt/argon2)
    - Brute force protection
    - Session management
    - CSRF protection
    - XSS protection

#### Deliverables:

- `backend/app/api/v1/auth.py` - auth endpoints
- `backend/app/core/security.py` - security utils
- `backend/app/services/auth_service.py` - auth logic
- `frontend/src/lib/auth.ts` - auth client

---

### 2.2 Secrets Management z Vault (cd.)

**Wykonawca: Ty (DevOps) | Czas: 3 dni**

#### Zadania (cd.):

3. **Backend Integration:**
    
    - VaultService z metodami: get_secret(), set_secret(), rotate_secret()
    - Caching sekretów w Redis (5 min TTL)
    - Automatic token renewal
    - Fallback mechanism przy Vault downtime
4. **Secret Rotation:**
    
    - Automated rotation policy (co 90 dni)
    - Notification przed expiracją
    - Zero-downtime rotation
    - Audit log rotacji
5. **CLI Tools:**
    
    - Script do inicjalizacji Vault
    - Script do dodawania sekretów
    - Script do backup/restore
    - Emergency unseal procedure

#### Deliverables:

- `backend/app/services/vault_service.py` - Vault integration
- `infrastructure/vault/policies/*.hcl` - Vault policies
- `scripts/vault-init.sh` - initialization script
- `docs/SECRETS_MANAGEMENT.md` - documentation

#### Kryteria sukcesu:

-  Backend pobiera sekrety z Vault, nie z .env
-  Możesz dodać nowy secret przez API
-  Rotation działa automatycznie
-  Backup/restore process działa

---

### 2.3 SNMP Collector Implementation

**Wykonawca: Osoba 3 (Collector) | Czas: 5 dni**

#### Zadania:

1. **SNMP Library Setup:**
    
    - Użyj `pysnmp` lub `easysnmp`
    - Support dla SNMPv1, v2c, v3
    - Async operations
    - Bulk operations dla efektywności
2. **OID Management:**
    
    - Zdefiniuj standardowe OIDs:
        - System: sysDescr, sysUpTime, sysContact, sysName, sysLocation
        - Interfaces: ifIndex, ifDescr, ifSpeed, ifOperStatus, ifInOctets, ifOutOctets
        - CPU: hrProcessorLoad (HOST-RESOURCES-MIB)
        - Memory: hrStorageUsed, hrStorageSize
        - Temperature: Vendor-specific MIBs
    - MIB browser integration (opcjonalnie)
3. **Collector Logic:**
    
    - Auto-discovery interfejsów (SNMP walk)
    - Parallel OID fetching
    - Error handling (timeout, no response, wrong credentials)
    - Metric normalization (różne vendorzy)
4. **Data Processing:**
    
    - Calculate bandwidth utilization (delta between polls)
    - Calculate CPU/Memory percentage
    - Interface status mapping (up/down/testing)
    - Unit conversion (bits/bytes, MB/GB)
5. **Vendor-Specific Support:**
    
    - Cisco IOS/IOS-XE
    - Juniper JunOS
    - Arista EOS
    - Mikrotik RouterOS
    - Generic SNMP devices
6. **Celery Task:**
    
    - Task: poll_device_snmp(device_id)
    - Schedule co 5 minut (konfigurowalny)
    - Priority queues (critical devices first)
    - Task chaining dla complex workflows

#### Deliverables:

- `backend/app/collectors/snmp_collector.py` - implementacja
- `backend/app/utils/oid_definitions.py` - OID mapping
- `backend/tests/test_snmp_collector.py` - testy
- `docs/SNMP_MONITORING.md` - dokumentacja

#### Kryteria sukcesu:

-  Collector zbiera metryki z real devices
-  Obsługuje SNMPv3 z authentication
-  Metryki są w TimescaleDB
-  Grafana dashboard pokazuje CPU/RAM/Interface stats

---

### 2.4 SSH Command Runner

**Wykonawca: Osoba 3 (Collector) | Czas: 4 dni**

#### Zadania:

1. **SSH Library Setup:**
    
    - Użyj `Netmiko` dla vendor compatibility
    - Alternatywnie: `Nornir` dla orchestration
    - Connection pooling
    - Timeout handling
2. **Command Execution:**
    
    - READ-ONLY commands tylko!
    - Whitelist dozwolonych komend:
        - Cisco: show running-config, show ip interface brief, show version
        - Juniper: show configuration, show interfaces terse
        - Arista: show running-config, show ip interface brief
    - Command validation przed wykonaniem
    - Output parsing
3. **TextFSM Integration:**
    
    - Parse structured data z command output
    - Templates dla common commands
    - Convert to JSON
    - Store parsed data w PostgreSQL
4. **Security:**
    
    - SSH key authentication only (no passwords)
    - Store private keys w Vault
    - Command logging (pre-execution)
    - Session recording (optional)
5. **API Endpoint:**
    
    - `POST /api/v1/devices/{id}/execute` - run command
    - Request body: { "command": "show version" }
    - Response: { "output": "...", "parsed": {...} }
    - Rate limiting (max 10 commands/minute per user)
6. **Audit Trail:**
    
    - Log do audit_logs table:
        - user_id, device_id, command, timestamp, execution_time
        - success/failure status
        - output preview (first 500 chars)

#### Deliverables:

- `backend/app/collectors/ssh_collector.py` - implementacja
- `backend/app/utils/parsers.py` - TextFSM parsers
- `backend/app/api/v1/commands.py` - API endpoint
- `frontend/src/app/(dashboard)/devices/[id]/console` - UI

#### Kryteria sukcesu:

-  Możesz wykonać command przez UI
-  Output jest sparsowany do JSON
-  Wszystkie komendy są logowane
-  Niemożliwe jest wykonanie write commands

---

### 2.5 Frontend - Authentication & Metrics UI

**Wykonawca: Osoba 2 (Frontend) | Czas: 5 dni**

#### Zadania:

1. **Login/Register Pages:**
    
    - Login form z remember me
    - Register form z email verification
    - Password reset flow
    - Error handling z user-friendly messages
    - Redirect po zalogowaniu
2. **Auth State Management:**
    
    - Store user info w Zustand
    - Persist auth state (localStorage)
    - Auto-logout po expiry
    - Refresh token logic
    - Protected routes (middleware)
3. **Metrics Dashboard:**
    
    - Device overview cards (Total, Online, Offline, Warning)
    - Real-time status updates (WebSocket opcjonalnie)
    - Charts:
        - Line chart: Latency over time
        - Bar chart: Top 10 devices by CPU usage
        - Pie chart: Device types distribution
        - Heatmap: Network health (grid of devices colored by status)
4. **Device Details - Metrics Tab:**
    
    - Time range selector (1h, 6h, 24h, 7d, 30d)
    - Multiple charts:
        - Ping latency + packet loss
        - CPU utilization
        - Memory utilization
        - Interface bandwidth (in/out)
    - Export to CSV/PNG
    - Auto-refresh toggle
5. **Real-time Updates:**
    
    - Poll API co 30s
    - Lub WebSocket connection dla live data
    - Optimistic UI updates
    - Notification toast dla alerts
6. **Charts Library:**
    
    - Użyj `recharts` lub `chart.js`
    - Responsive charts
    - Tooltips z detailed info
    - Zoom/pan dla large datasets

#### Deliverables:

- `frontend/src/app/(auth)/*` - auth pages
- `frontend/src/app/(dashboard)/metrics/*` - metrics dashboard
- `frontend/src/components/charts/*` - chart components
- `frontend/src/hooks/useAuth.ts` - auth hook

#### Kryteria sukcesu:

-  Login/logout flow działa
-  Protected routes wymagają auth
-  Dashboard pokazuje real metrics
-  Charts są interaktywne i responsywne

---

### 2.6 Grafana Dashboards

**Wykonawca: Ty (DevOps) | Czas: 2 dni**

#### Zadania:

1. **Network Overview Dashboard:**
    
    - Total devices stat panel
    - Devices by status (gauge)
    - Average latency (stat + sparkline)
    - Top 10 devices by packet loss (bar chart)
    - Network topology map (optional - world map plugin)
2. **Device Details Dashboard:**
    
    - Variables: $device (dropdown)
    - ICMP metrics: RTT, jitter, packet loss
    - SNMP metrics: CPU, RAM, uptime
    - Interface metrics: bandwidth, errors, discards
    - System info panel (sysDescr, sysUpTime)
3. **System Health Dashboard:**
    
    - Collector performance metrics
    - Database query performance
    - API response times
    - Celery queue length
    - Error rates
4. **Alerting Dashboard:**
    
    - Active alerts table
    - Alert history timeline
    - Alerts by severity (pie chart)
    - MTTR (Mean Time To Resolution)
5. **Provisioning:**
    
    - Dashboards as code (JSON files)
    - Datasources auto-configuration
    - Variables from environment
    - Automated import przy startup

#### Deliverables:

- `infrastructure/grafana/dashboards/*.json` - wszystkie dashboardy
- `infrastructure/grafana/datasources/datasources.yml` - datasources
- `infrastructure/grafana/grafana.ini` - config
- `docs/GRAFANA_SETUP.md` - dokumentacja

---

### 2.7 Integration & End-to-End Testing

**Wykonawca: Wszyscy | Czas: 3 dni**

#### Zadania:

1. **Integration Tests:**
    
    - Test full flow: Add device → Poll metrics → View in dashboard
    - Test auth flow: Register → Login → Protected endpoint
    - Test SSH flow: Execute command → Parse output → Store result
    - Test alert flow: Threshold breach → Alert created → Notification sent
2. **Performance Testing:**
    
    - Load test API (Locust): 1000 concurrent users
    - Load test collectors: 1000 devices polling
    - Database performance: query optimization
    - Frontend performance: Lighthouse score 90+
3. **Security Testing:**
    
    - OWASP ZAP scan
    - SQL injection tests
    - XSS tests
    - Authentication bypass attempts
    - CSRF tests
4. **Manual Testing:**
    
    - Full user journey testing
    - Edge cases
    - Error scenarios
    - Browser compatibility
    - Mobile responsiveness

#### Deliverables:

- `backend/tests/integration/*` - integration tests
- `backend/tests/load/locustfile.py` - load tests
- `docs/TEST_REPORT.md` - test report
- Bug tracking w GitHub Issues

---

##  FAZA 3: Production Features & Automation

**Czas: 2-3 tygodnie | Priorytet: ŚREDNI**

### 3.1 Syslog Collection & Log Management

**Wykonawca: Ty (DevOps) + Osoba 3 (Collector) | Czas: 4 dni**

#### Zadania:

1. **Loki + Promtail Setup:**
    
    - Loki configuration (retention, limits)
    - Promtail jako syslog server (UDP 514, TCP 601)
    - Log parsing rules (regex, JSON)
    - Label extraction (device_ip, severity, facility)
2. **Syslog Collector:**
    
    - Python syslog server (asyncio)
    - Parse syslog format (RFC 3164, RFC 5424)
    - Enrich logs (map IP to device_id)
    - Forward to Loki
    - Store critical logs w PostgreSQL
3. **Log Query API:**
    
    - `GET /api/v1/logs` - query logs
    - Filters: device_id, severity, time_range, keyword
    - Pagination
    - Export to CSV
4. **Frontend - Logs Viewer:**
    
    - Real-time log stream (live tail)
    - Advanced filters
    - Syntax highlighting
    - Full-text search
    - Log context (show surrounding logs)

#### Deliverables:

- `infrastructure/loki/config.yml` - Loki config
- `infrastructure/promtail/config.yml` - Promtail config
- `backend/app/collectors/syslog_collector.py` - collector
- `backend/app/api/v1/logs.py` - API
- `frontend/src/app/(dashboard)/logs/*` - UI

---

### 3.2 Alerting System

**Wykonawca: Ty (DevOps) | Czas: 4 dni**

#### Zadania:

1. **Alert Rules Engine:**
    
    - Define rules w PostgreSQL:
        - Threshold-based (CPU > 90% for 5 min)
        - Pattern-based (log contains "ERROR")
        - Availability-based (device down for 2 min)
    - Rule evaluation engine (Celery task co 1 min)
    - Alert deduplication (suppress repeated alerts)
    - Alert correlation (group related alerts)
2. **Notification Channels:**
    
    - Email (SMTP)
    - Slack (webhook)
    - Webhook (generic HTTP POST)
    - PagerDuty integration (optional)
3. **Alert Lifecycle:**
    
    - States: PENDING → FIRING → RESOLVED → ACKNOWLEDGED
    - Auto-resolve przy metric recovery
    - Manual acknowledgement
    - Escalation policy (notify manager po 30 min)
4. **API Endpoints:**
    
    - `GET /api/v1/alerts` - list alerts
    - `POST /api/v1/alerts/{id}/acknowledge` - ack alert
    - `POST /api/v1/alerts/{id}/resolve` - resolve alert
    - `GET /api/v1/alert-rules` - list rules
    - `POST /api/v1/alert-rules` - create rule
5. **Frontend - Alerts UI:**
    
    - Alerts table (filterable, sortable)
    - Alert details modal
    - Acknowledge/resolve buttons
    - Alert timeline
    - Create/edit alert rules form

#### Deliverables:

- `backend/app/services/alert_service.py` - alerting logic
- `backend/app/tasks/alert_tasks.py` - evaluation tasks
- `backend/app/api/v1/alerts.py` - API
- `frontend/src/app/(dashboard)/alerts/*` - UI

---

### 3.3 Reporting System

**Wykonawca: Osoba 2 (Frontend) + Ty (DevOps) | Czas: 3 dni**

#### Zadania:

1. **Report Types:**
    
    - **Availability Report**: Uptime % per device, SLA compliance
    - **Performance Report**: Avg/Max/Min CPU/RAM/Latency
    - **Alert Report**: Alert summary, MTTR, top alerting devices
    - **Inventory Report**: Device list z configurations
2. **Report Generation:**
    
    - Backend: Generate reports (PDF using WeasyPrint, CSV using pandas)
    - Scheduled reports (Celery Beat - daily/weekly/monthly)
    - On-demand report generation
    - Email delivery
3. **API Endpoints:**
    
    - `POST /api/v1/reports/generate` - generate report
    - `GET /api/v1/reports` - list generated reports
    - `GET /api/v1/reports/{id}/download` - download report
4. **Frontend - Reports UI:**
    
    - Report builder form (select type, date range, devices)
    - Preview report
    - Download button
    - Scheduled reports management

#### Deliverables:

- `backend/app/services/report_service.py` - report generation
- `backend/app/templates/reports/*.html` - PDF templates
- `backend/app/api/v1/reports.py` - API
- `frontend/src/app/(dashboard)/reports/*` - UI

---

### 3.4 Backup & Disaster Recovery

**Wykonawca: Ty (DevOps) | Czas: 3 dni**

#### Zadania:

1. **Database Backup:**
    
    - Automated daily backups (pg_dump, TimescaleDB dump)
    - Incremental backups (WAL archiving)
    - Backup retention (30 days)
    - Backup verification (restore test)
    - Off-site backup (S3, Google Cloud Storage)
2. **Configuration Backup:**
    
    - Backup Vault secrets
    - Backup Grafana dashboards
    - Backup Prometheus rules
    - Version control dla configs (Git)
3. **Restore Procedures:**
    
    - Documented restore process
    - Automated restore script
    - Test restore monthly
    - RTO: 1 hour, RPO: 24 hours
4. **Disaster Recovery Plan:**
    
    - Failover procedure
    - Data center failure scenario
    - Communication plan
    - Runbook

#### Deliverables:

- `scripts/backup.sh` - backup script
- `scripts/restore.sh` - restore script
- `docs/DISASTER_RECOVERY.md` - DR plan
- Cron job configuration

---

### 3.5 CI/CD Pipeline - Production Deployment

**Wykonawca: Ty (DevOps) | Czas: 4 dni**

#### Zadania:

1. **GitHub Actions Workflows:**
    
    - **CI Pipeline** (na każdy push):
        - Lint (black, isort, eslint, prettier)
        - Test (pytest, vitest)
        - Security scan (bandit, npm audit)
        - Build (Docker images)
    - **CD Pipeline - Dev** (na merge do `develop`):
        - Deploy do dev environment
        - Run smoke tests
        - Notify Slack
    - **CD Pipeline - Prod** (na tag `v*`):
        - Deploy do staging
        - Run E2E tests
        - Manual approval gate
        - Deploy do production
        - Rollback on failure
2. **Infrastructure as Code:**
    
    - Terraform scripts (optional dla cloud deployment)
    - Ansible playbooks (server provisioning)
    - Docker Swarm lub Kubernetes manifests (optional)
3. **Monitoring CI/CD:**
    
    - Pipeline metrics w Grafana
    - Failed deployment alerts
    - Deployment frequency tracking
    - Lead time for changes
4. **Deployment Strategy:**
    
    - Blue-green deployment
    - Canary releases (optional)
    - Rolling updates
    - Zero-downtime deployment

#### Deliverables:

- `.github/workflows/*.yml` - all pipelines
- `infrastructure/terraform/*` - IaC scripts
- `docs/DEPLOYMENT.md` - deployment guide
- Deployment dashboard w Grafana

---

### 3.6 Documentation & Knowledge Base

**Wykonawca: Wszyscy | Czas: 2 dni**

#### Zadania:

1. **Technical Documentation:**
    
    - Architecture diagrams (C4 model)
    - API reference (complete)
    - Database schema
    - Deployment guide
    - Troubleshooting guide
2. **User Documentation:**
    
    - User manual (PDF + online)
    - Video tutorials (screen recordings)
    - FAQ
    - Best practices
3. **Developer Documentation:**
    
    - Contributing guide
    - Code style guide
    - Testing guide
    - Local dev setup
    - ADRs (Architecture Decision Records)
4. **Operational Documentation:**
    
    - Runbooks (common tasks)
    - Incident response playbook
    - Monitoring guide
    - Backup/restore procedures

#### Deliverables:

- `docs/*` - wszystkie dokumenty
- `README.md` - complete project overview
- Wiki w GitHub
- Video tutorials (YouTube/internal)

---

### 3.7 Final Testing & Go-Live

**Wykonawca: Wszyscy | Czas: 3 dni**

#### Zadania:

1. **User Acceptance Testing (UAT):**
    
    - Test z real users
    - Collect feedback
    - Fix critical bugs
    - Performance tuning
2. **Security Audit:**
    
    - External security review (optional)
    - Penetration testing
    - Fix vulnerabilities
    - Update dependencies
3. **Performance Optimization:**
    
    - Database query optimization
    - API endpoint optimization
    - Frontend bundle size reduction
    - CDN setup dla static assets
4. **Go-Live Checklist:**
    
    - [ ] All tests passing
    - [ ] Documentation complete
    - [ ] Backups configured
    - [ ] Monitoring in place
    - [ ] Alerts configured
    - [ ] Team trained
    - [ ] Support plan ready
5. **Launch:**
    
    - Deploy to production
    - Monitor closely (first 48h)
    - Collect user feedback
    - Hotfix critical issues

#### Deliverables:

- Production-ready system
- Launch announcement
- Support documentation
- Post-launch report

---

##  FAZA 4: Post-Launch & Iteration (Ongoing)

### 4.1 Monitoring & Optimization

- Monitor system performance
- Optimize based on real usage
- Scale resources as needed
- Tune alert thresholds

### 4.2 Feature Enhancements

- Implement user feedback
- Add new collectors (REST API, NetFlow)
- Advanced analytics (ML-based anomaly detection)
- Mobile app (optional)

### 4.3 Maintenance

- Regular dependency updates
- Security patches
- Bug fixes
- Performance improvements

---

##  Kluczowe Metryki Sukcesu

|Metryka|Cel|
|---|---|
|System Uptime|99.5%+|
|API Response Time|< 200ms (p95)|
|Device Polling Success Rate|> 99%|
|Alert False Positive Rate|< 5%|
|User Satisfaction Score|> 4.0/5.0|
|Test Coverage|> 80%|
|Security Vulnerabilities|0 Critical, 0 High|
|Deployment Frequency|Weekly (po stabilizacji)|
|MTTR (Mean Time To Recovery)|< 1 hour|

---

##  Rekomendacje Techniczne

### Must-Have Libraries (Backend):

```python
# Core
fastapi[all]==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy[asyncio]==2.0.23
alembic==1.12.1

# Database
asyncpg==0.29.0
psycopg2-binary==2.9.9
redis==5.0.1

# Monitoring
	prometheus-client==0.19.0cd
python-json-logger==2.0.7

# Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# Collectors
icmplib==3.0.4
pysnmp==4.4.12
netmiko==4.3.0
textfsm==1.1.3

# Tasks
celery[redis]==5.3.4
flower==2.0.1

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
httpx==0.25.2
```

### Must-Have Libraries (Frontend):

```json
{
  "dependencies": {
    "next": "14.0.4",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "@tanstack/react-query": "^5.0.0",
    "zustand": "^4.4.7",
    "axios": "^1.6.2",
    "recharts": "^2.10.3",
    "@radix-ui/react-*": "latest",
    "tailwindcss": "^3.3.6",
    "lucide-react": "^0.294.0"
  },
  "devDependencies": {
    "typescript": "^5.3.3",
    "@types/react": "^18.2.45",
    "eslint": "^8.55.0",
    "prettier": "^3.1.1",
    "vitest": "^1.0.4",
    "playwright": "^1.40.1"
  }
}
```

---

##  Szacowany Timeline

|Faza|Czas|Zespół|
|---|---|---|
|Faza 0: POC|1 tydzień|Wszyscy|
|Faza 1: MVP|3 tygodnie|Wszyscy|
|Faza 2: Security & Advanced|3 tygodnie|Wszyscy|
|Faza 3: Production|2-3 tygodnie|Wszyscy|
|**TOTAL**|**~10 tygodni**|**3-osobowy zespół**|

---

##  Quick Start Commands

```bash
# Setup
make setup

# Development
make dev

# Testing
make test

# Build
make build

# Deploy
make deploy

# Backup
make backup

# Restore
make restore BACKUP_FILE=backup.sql
```

---

**Dokument zaktualizowany:** 2025-10-08  
**Wersja:** 2.0 Complete  
**Status:** Ready for Implementation 