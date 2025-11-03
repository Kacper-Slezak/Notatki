
**Cel:** Stworzenie platformy SOTP jako w pełni orkiestrowanego, obserwowalnego i bezpiecznego systemu gotowego do wdrożenia, demonstrującego nowoczesne praktyki DevOps/Platform Engineering w środowisku lokalnym.

### 1. Architektura Aplikacji (Logiczna)

_Bazując na diagramie z `Projekt 2.md`, rozszerzamy warstwę danych o pełną obserwowalność._

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                     │
│  React/Next.js Frontend                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   API & INGRESS LAYER                       │
│  Traefik (K8s Ingress) → FastAPI (REST + WebSocket)         │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  APPLICATION LAYER                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Inventory  │  │  Auth/RBAC   │  │   Alerting   │       │
│  │   Service    │  │   Service    │  │   Service    │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   CACHE & QUEUE LAYER                       │
│  Redis (Cache + Session) + Celery (Task Queue)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  COLLECTOR WORKERS                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │   SNMP   │ │   ICMP   │ │   SSH    │ │  Syslog  │        │
│  │ Collector│ │ Collector│ │ Collector│ │ Collector│        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   DATA & OBSERVABILITY LAYER                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐
│  │  PostgreSQL     │  │  TimescaleDB    │  │  Loki (Logs)   │
│  │  (Inventory)    │  │  (Time-Series)  │  │                │
│  └─────────────────┘  └─────────────────┘  └────────────────┘
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐
│  │  Vault          │  │  Prometheus     │  │  Tempo (Traces)│
│  │  (Secrets)      │  │  (Metrics)      │  │                │
│  └─────────────────┘  └─────────────────┘  └────────────────┘
└─────────────────────────────────────────────────────────────┘
```

### 2. Architektura Wdrożenia (GitOps Toolchain)

_Pokazuje, **jak** kod trafia na "produkcję" (lokalny klaster K3d) przy użyciu GitOps._

```
          ┌──────────────────────┐
          │     Deweloper        │
          │ (VSCode DevContainer)│
          └──────────┬───────────┘
                     │ 1. git push
┌────────────────────▼───────────────────────────────────────────┐
│                    GitHub (sotp-backend)                       │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ 2. Uruchom CI Pipeline (.github/workflows/ci.yml)         │  │
│ │   - Lint (Black, isort)                                   │  │
│ │   - Testy (Pytest, --cov)                                 │  │
│ │   - Skanowanie (Bandit, Safety)                           │  │
│ └───────────────────────────────────────────────────────────┘  │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ 3. Uruchom CD Pipeline (.github/workflows/deploy-prod.yml)│  │
│ │   - Zbuduj i wypchnij obraz Docker                        │  │
│ └───────────────────────────────────────────────────────────┘  │
└────────────────────┬───────────────────────────────────────────┘
                     │ 4. Zaktualizuj image.tag w repozytorium...
┌────────────────────▼───────────────────────────────────────────┐
│                   GitHub (sotp-k8s-config)                     │
│    (Przechowuje stan klastra w postaci kodu - Helm Chart)      │
└────────────────────┬───────────────────────────────────────────┘
                     │ 5. ArgoCD wykrywa zmianę (Pull model)
┌────────────────────▼───────────────────────────────────────────┐
│              Lokalny Klaster K8s (K3d + ArgoCD)                │
│                                                                │
│ ┌────────┐ 6. ArgoCD synchronizuje stan, robi `helm upgrade`   │
│ │ ArgoCD ├────────────────────────────────────────┐            │
│ └────────┘                                        │            │
│                                                   ▼            │
│  ┌─────────────────────────────────────-────────────────────┐  │
│  │                Wdrożona Aplikacja SOTP                   │  │
│  │ ┌─────-─┐  ┌─────────┐  ┌───────┐  ┌───────────┐  ┌─────┐│  │
│  │ │FastAPI│  │ Celery  │  │ Redis │  │ Postgres  │  │ ... ││  │
│  │ └─────-─┘  └─────────┘  └───────┘  └───────────┘  └─────┘│  │
│  └─────────────────────────────────────────────-────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### 3. Zaktualizowany Stos Technologiczny

| **Warstwa**        | **Technologia**           | **Uzasadnienie**                                                                                                                              |
| ------------------ | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Orkiestracja**   | **K3d (K3s)** & **Helm**  | Zastępuje Docker Compose. Lekki, błyskawiczny klaster K8s do lokalnego developmentu i testowania wdrożeń. Helm standaryzuje proces wdrożenia. |
| **Deployment**     | **ArgoCD**                | Zastępuje skrypty `make deploy`. Wprowadza nowoczesny, deklaratywny model **GitOps** (pull-based) dla wdrożeń. Kluczowy element CV.           |
| **Frontend**       | Next.js (React), Tailwind | Bez zmian. Nowoczesny, wydajny UI.                                                                                                            |
| **Backend**        | FastAPI (Python)          | Bez zmian. Idealny do asynchronicznych zadań I/O (sieć, bazy danych).                                                                         |
| **Bazy Danych**    | PostgreSQL & TimescaleDB  | Bez zmian. Idealne rozdzielenie danych relacyjnych (Postgres) od szeregów czasowych (Timescale).                                              |
| **Kolejka Zadań**  | Celery & Redis            | Bez zmian. Niezbędne do asynchronicznego uruchamiania kolektorów.                                                                             |
| **Sekrety**        | **HashiCorp Vault**       | **(Ulepszenie)** Nie tylko uruchomiony, ale aktywnie zintegrowany z FastAPI (przez `hvac`) i K8s (przez **Vault Secrets Injector**).          |
| **Obserwowalność** | **(Nowy Stos "PLT")**     | Trzy filary obserwowalności – to robi największe wrażenie.                                                                                    |
|                    | **Prometheus** (Metrics)  | **(Ulepszenie)** W pełni zintegrowany z FastAPI (`starlette-prometheus`) do zbierania metryk aplikacyjnych.                                   |
|                    | **Loki** (Logs)           | Bez zmian. Agregacja logów ze wszystkich kontenerów.                                                                                          |
|                    | **Tempo** (Traces)        | **(NOWOŚĆ)** Śledzenie rozproszone (OpenTelemetry) pokazujące pełny cykl życia żądania (Frontend -> Backend -> Baza Danych).                  |
| **CI/CD**          | GitHub Actions            | Bez zmian. Budowanie, testowanie i publikowanie obrazów.                                                                                      |
| **Dev Env**        | VS Code DevContainers     | Bez zmian. Gwarantuje spójne środowisko deweloperskie dla każdego.                                                                            |

### 4. Struktura Projektu (Zaktualizowana)

```
sotp/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── infrastructure/
│   ├── docker/  (Używane tylko przez DevContainer)
│   │   ├── docker-compose.dev.yml
│   │   └── init-scripts/
│   ├── kubernetes/  (NOWOŚĆ - Manifesty bazowe)
│   │   ├── 01-namespace.yml
│   │   ├── 02-postgres.yml
│   │   ├── 03-timescale.yml
│   │   └── ...
│   ├── helm/  (NOWOŚĆ - Główna metoda wdrożenia)
│   │   └── sotp/
│   │       ├── Chart.yaml
│   │       ├── values.yaml
│   │       └── templates/
│   │           ├── _helpers.tpl
│   │           ├── backend-deployment.yml
│   │           ├── frontend-service.yml
│   │           └── ingress.yml
│   ├── argocd/  (NOWOŚĆ - Definicja aplikacji GitOps)
│   │   └── application.yml
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── rules/
│   ├── grafana/
│   │   ├── dashboards/
│   │   └── datasources/
│   └── vault/
│       ├── config.json
│       └── policies/
├── docs/
├── scripts/
├── .github/
│   └── workflows/
├── .gitignore
├── .env.example
├── Makefile  (Zaktualizowany o komendy Helm/K3d)
└── README.md (Zaktualizowany o instrukcje K3d/Argo)
```

### 5. Zaktualizowany Plan Wykonawczy (Fazy)

#### FAZA 1: MVP - Orkiestracja i Podstawy Aplikacji

**Cel:** Uruchomienie szkieletu aplikacji na lokalnym klastrze Kubernetes.

- **1.1 Orkiestracja - Lokalny Klaster (K3d) i Helm:**
    
    - **Zadanie:** Stworzenie klastra K3d (`k3d cluster create sotp`).
        
    - **Zadanie:** Stworzenie **Helm Chart** (`infrastructure/helm/sotp`) opisującego wszystkie komponenty (Postgres, Timescale, Redis, Backend, Frontend).
        
    - **Deliverable:** `helm install dev ./infrastructure/helm/sotp` pomyślnie wdraża cały stos.
        
- **1.2 Schemat Baz Danych i Migracje:**
    
    - **Zadanie:** Zdefiniowanie modeli SQLAlchemy (Users, Devices, PingResult, itd.).
        
    - **Zadanie:** Skonfigurowanie Alembic do zarządzania dwoma bazami danych (Postgres, Timescale) i stworzenie początkowych migracji.
        
    - **Zadanie:** Użycie `Job` w Kubernetes (w ramach Helm Charta) do automatycznego uruchamiania migracji Alembic (`alembic -x db=postgres upgrade postgres@head` && `alembic -x db=timescale upgrade timescale@head`) przy każdym wdrożeniu.
        
- **1.3 Backend API - CRUD Urządzeń i Metryki:**
    
    - **Zadanie:** Implementacja endpointów CRUD dla `/api/v1/devices` w `main.py`.
        
    - **Zadanie (Ulepszenie):** Dodanie `starlette-prometheus` i wystawienie endpointu `/metrics` dla Prometheusa.
        
- **1.4 Kolektor ICMP:**
    
    - **Zadanie:** Potwierdzenie, że `monitoring_tasks.py` i `celery_Beat_for_icmp.py` działają poprawnie jako Deployment K8s (oddzielne Pody dla `worker` i `beat`).
        
- **1.5 Frontend - Szkielet UI:**
    
    - **Zadanie:** Zbudowanie layoutu (Sidebar, Navbar).
        
    - **Zadanie:** Implementacja strony `/devices` (tabela, formularz) używając `react-query` do komunikacji z API.
        
- **1.6 Potok CI (Test & Build):**
    
    - **Zadanie:** Rozbudowa `ci.yml` o realne testy (`pytest --cov=app`).
        
    - **Zadanie:** Rozbudowa `deploy-prod.yml` o budowanie obrazów frontend i backend i publikowanie ich do rejestru (np. GHCR).
        
    - **Zadanie:** Wprowadzenie `Codecov` lub podobnego narzędzia do śledzenia pokrycia testami.
        

#### FAZA 2: Bezpieczeństwo i Zaawansowany Monitoring

**Cel:** Zabezpieczenie aplikacji i rozbudowa możliwości zbierania danych.

- **2.1 Uwierzytelnianie i RBAC:**
    
    - **Zadanie:** Implementacja JWT (login, register) i ról użytkowników (Admin, Operator, etc.).
        
    - **Zadanie:** Zabezpieczenie endpointów API w oparciu o role.
        
    - **Zadanie (Frontend):** Stworzenie stron logowania i rejestracji oraz "Protected Routes".
        
- **2.2 Pełna Integracja z HashiCorp Vault:**
    
    - **Zadanie (Aplikacja):** Stworzenie `VaultService` w backendzie (używając `hvac`). Zmodyfikowanie `main.py` tak, aby hasła do baz danych były pobierane z Vault _przy starcie aplikacji_, a nie ze zmiennych środowiskowych.
        
    - **Zadanie (Infrastruktura):** Skonfigurowanie **Vault Secrets Injector** w K8s. Aplikacja (Pod) dostaje sekrety jako zamontowane pliki, co eliminuje potrzebę zarządzania tokenem Vault w kodzie.
        
- **2.3 Kolektor SNMP:**
    
    - **Zadanie:** Implementacja kolektora SNMP (używając `pysnmp`) jako nowego zadania Celery.
        
    - **Zadanie:** Zbieranie podstawowych metryk (CPU, RAM, ruch interfejsu) i zapisywanie ich do TimescaleDB.
        
- **2.4 Filar Obserwowalności 1: Metryki (Prometheus):**
    
    - **Zadanie:** Wdrożenie Prometheusa (przez Helm Chart).
        
    - **Zadanie:** Skonfigurowanie Prometheusa, aby automatycznie zbierał dane z endpointu `/metrics` backendu.
        
    - **Zadanie:** Stworzenie dashboardu w Grafanie (też przez Helm) pokazującego metryki API (latency, błędy, żądania na sekundę).
        

#### FAZA 3: Obserwowalność i Automatyzacja CD (GitOps)

**Cel:** Osiągnięcie pełnej obserwowalności i wdrożenie wzorca GitOps.

- **3.1 Filar Obserwowalności 2: Logi (Loki):**
    
    - **Zadanie:** Wdrożenie Loki i Promtail (przez Helm Chart).
        
    - **Zadanie:** Skonfigurowanie Promtail do automatycznego zbierania logów ze wszystkich Podów (backend, frontend, celery, bazy danych) w klastrze K8s.
        
    - **Zadanie:** Zintegrowanie Loki jako źródła danych w Grafanie.
        
- **3.2 Filar Obserwowalności 3 (Piąta Myśl): Ślady (OpenTelemetry & Tempo):**
    
    - **Zadanie:** Wdrożenie Grafana Tempo (przez Helm Chart).
        
    - **Zadanie (Backend):** Dodanie bibliotek `opentelemetry-distro` i `opentelemetry-instrumentation-fastapi`. Skonfigurowanie FastAPI do wysyłania _traces_ (śladów) do Tempo.
        
    - **Zadanie (Frontend):** Skonfigurowanie Next.js do wysyłania _traces_ do Tempo.
        
    - **Rezultat:** Możliwość śledzenia pojedynczego kliknięcia w UI, przez żądanie API, aż do zapytania w bazie danych i z powrotem. **To jest funkcja "flagowa".**
        
- **3.3 Wdrożenie GitOps (ArgoCD):**
    
    - **Zadanie:** Stworzenie _drugiego_ repozytorium Git (`sotp-k8s-config`) zawierającego wyłącznie Helm Chart aplikacji.
        
    - **Zadanie:** Instalacja ArgoCD w klastrze K3d.
        
    - **Zadanie:** Skonfigurowanie ArgoCD, aby monitorowało repozytorium `sotp-k8s-config` i automatycznie wdrażało zmiany.
        
    - **Zadanie:** Modyfikacja `deploy-prod.yml`: po zbudowaniu obrazu, pipeline ma _tylko_ zaktualizować `image.tag` w repozytorium `sotp-k8s-config`. ArgoCD zajmie się resztą.
        
- **3.4 System Alertów:**
    
    - **Zadanie:** Konfiguracja Alertmanagera (część Prometheusa).
        
    - **Zadanie:** Zdefiniowanie alertów (w plikach `.yaml` w Helm Chart) dla reguł (np. "API 500 error rate > 2%", "Device DOWN for 5 min").
        
    - **Zadanie:** Integracja z Discordem (lub Slackiem) dla powiadomień o alertach.
        

#### FAZA 4: Funkcjonalność Biznesowa (Ukończenie Produktu)

**Cel:** Dokończenie implementacji funkcji z `Projekt 2.md`.

- **4.1 Kolektor SSH (Netmiko):**
    
    - **Zadanie:** Implementacja kolektora SSH (używając `netmiko`) do wykonywania poleceń typu `show version` na żądanie przez UI.
        
    - **Zadanie:** Bezpieczne przechowywanie kluczy SSH w Vault i pobieranie ich przez backend.
        
- **4.2 Kolektor Syslog & Logi Audytowe:**
    
    - **Zadanie:** Stworzenie serwisu w backendzie, który potrafi przyjmować logi Syslog i przekazywać je do Loki z odpowiednimi etykietami.
        
    - **Zadanie:** Implementacja modelu `AuditLog` i automatyczne zapisywanie zdarzeń (logowanie, CRUD na urządzeniach).
        
    - **Zadanie (Frontend):** Budowa UI do przeglądania logów z Loki oraz logów audytowych z Postgres.
        
- **4.3 Raportowanie:**
    
    - **Zadanie:** Budowa serwisu do generowania raportów PDF/CSV (np. tygodniowy raport uptime).
        
    - **Zadanie (Frontend):** UI do generowania i pobierania raportów.
        
- **4.4 Backup & Restore:**
    
    - **Zadanie:** Stworzenie `CronJob` w Kubernetes, który wykonuje `pg_dump` i `ts-dump` i wysyła backupy np. na lokalne S3 (MinIO).
        
    - **Zadanie:** Dokumentacja procedury odtwarzania (`docs/DISASTER_RECOVERY.md`).
        

---

### FAZA 5: Wizja i Dalszy Rozwój (Co dalej?)

#### 5.1 Wdrożenie Service Mesh (Linkerd)

- **Cel:** Pokazanie zrozumienia dla zaawansowanej komunikacji i bezpieczeństwa w architekturze mikroserwisów.
    
- **Zadanie:** Zainstalowanie **Linkerd** (lżejszy niż Istio, idealny na start) w klastrze K3d.
    
- **Zadanie:** "Wstrzyknięcie" proxy Linkerd do deploymentów Backendu i Baz Danych.
    
- **Rezultat (Flagowy):**
    
    1. **mTLS (Mutual TLS):** Cała komunikacja między serwisami (Backend -> Postgres, Backend -> Redis) jest automatycznie szyfrowana, bez zmiany _ani jednej linii kodu_ w Pythonie.
        
    2. **Golden Metrics:** Linkerd automatycznie dostarcza metryki L7 (success rate, request/s, latency) dla _całego_ ruchu w klastrze.
        
    3. **Resilience:** Możliwość skonfigurowania automatycznych ponowień (retries) i timeoutów na poziomie sieci, a nie aplikacji.
        

#### 5.2 Automatyzacja w Zamkniętej Pętli (Closed-Loop Automation)

- **Cel:** Połączenie Obserwowalności z Automatyzacją Sieciową.
    
- **Zadanie:** Stworzenie "silnika naprawczego".
    
    1. **Alert:** Prometheus wykrywa alert (np. "Wysoki packet loss na interfejsie Gi0/1 urządzenia X") i wysyła go do Alertmanagera.
        
    2. **Webhook:** Alertmanager wysyła webhook do dedykowanego endpointu w FastAPI (`/api/v1/webhooks/remediate`).
        
    3. **Akcja:** Endpoint FastAPI waliduje webhook i kolejkuje zadanie Celery (`tasks.remediate_interface(device_id=X, if_name='Gi0/1')`).
        
    4. **Naprawa:** Zadanie Celery używa Netmiko/Nornir (z Fazy 4.1), loguje się do urządzenia i wykonuje `shutdown` a następnie `no shutdown` na tym interfejsie.
        
- **Rezultat (Flagowy):** System, który nie tylko _informuje_ o problemie, ale sam go _naprawia_. To jest szczyt automatyzacji.
    
#### 5.3 Anomalia i Predykcja (AI/ML)

- **Cel:** Wykorzystanie zebranych danych do inteligentnych przewidywań.
    
- **Zadanie:** Użycie wbudowanych funkcji **TimescaleDB Toolkit** (darmowy dodatek) do analizy AI/ML.
    
- **Zadanie:** Stworzenie nowego zadania Celery (`tasks.predict_trends()`), które raz dziennie:
    
    1. Używa modelu `Prophet` (lub podobnego) na danych z ostatnich 30 dni (np. ruch sieciowy).
        
    2. Generuje predykcję na następne 7 dni.
        
    3. Wykrywa anomalie (np. "Ruch o 3:00 w nocy był o 50% wyższy niż przewidywano").
        
- **Rezultat (Flagowy):** Przejście od monitoringu reaktywnego ("coś się zepsuło") do proaktywnego ("coś się _zaraz_ zepsuje") i analitycznego ("to jest _dziwne_").
    

#### 5.4 Network Configuration Management (GitOps dla Sieci)

- **Cel:** Traktowanie konfiguracji urządzeń sieciowych jak kodu.
    
- **Zadanie:** Stworzenie zadania Celery (`tasks.backup_config()`), które:
    
    1. Używa Netmiko do logowania się na _każde_ urządzenie (np. raz dziennie).
        
    2. Wykonuje `show running-config`.
        
    3. Zapisuje wynik do repozytorium `sotp-k8s-config` w folderze `configs/`.
        
- **Rezultat (Flagowy):**
    
    1. `git diff` na pliku konfiguracyjnym urządzenia pokazuje, co zmieniło się w sieci.
        
    2. ArgoCD może alertować o "dryfie" konfiguracji (zmiana wykryta poza Git).
        
    3. Posiadanie pełnej historii zmian konfiguracji całej infrastruktury.
        

#### 5.5 Zaawansowane Kolektory (NetFlow/sFlow)

- **Cel:** Zrozumienie, _kto_ generuje ruch w sieci.
    
- **Zadanie:** Implementacja kolektora **NetFlow/sFlow**. Jest to trudniejsze (wymaga obsługi pakietów UDP), ale pokazuje dogłębne zrozumienie sieci.
    
- **Rezultat (Flagowy):** Zamiast wiedzieć tylko "interfejs ma 80% obciążenia" (SNMP), wiesz "interfejs ma 80% obciążenia, _z czego 90% to ruch z serwera X do serwera Y po porcie 443_".
    

### 6. Kluczowe Metryki Sukcesu

_Przeniesione z `Projekt 2.md`._

|**Metryka**|**Cel**|
|---|---|
|System Uptime|99.5%+|
|API Response Time|< 200ms (p95)|
|Device Polling Success Rate|> 99%|
|Alert False Positive Rate|< 5%|
|Test Coverage (Backend)|> 80%|
|Security Vulnerabilities|0 Critical, 0 High|
|Deployment Frequency|Codziennie (dzięki GitOps)|
|MTTR (Mean Time To Recovery)|< 15 minut (automatyczne rollbacki)|

### 7. Rekomendowane Biblioteki (Dodatki)

_Bazując na `Projekt 2.md`, dodajemy kluczowe pakiety do `backend/requirements.txt`._

Python

```
# ... (istniejące: fastapi, uvicorn, sqlalchemy, alembic, asyncpg, redis, prometheus-client, python-jose, passlib, icmplib, pysnmp, netmiko, celery, hvac, pytest, httpx) ...

# 💎 FLAGOWE DODATKI 💎

# Integracja z Vault
hvac==1.2.1 # Już masz, kluczowe do Fazy 2

# Obserwowalność (Metrics)
starlette-prometheus==0.15.0  # Dla metryk /metrics w FastAPI

# Obserwowalność (Tracing - Faza 3.2)
opentelemetry-distro==0.45b0   # Główny pakiet OpenTelemetry
opentelemetry-instrumentation-fastapi==0.45b0
opentelemetry-instrumentation-celery==0.45b0
opentelemetry-instrumentation-sqlalchemy==0.45b0
opentelemetry-instrumentation-httpx==0.45b0
opentelemetry-exporter-otlp==1.24.0 # Do wysyłania danych do Tempo

# Raportowanie (Faza 4.3)
weasyprint==62.1 # Do generowania PDF z HTML

# AI/ML (Faza 5.3)
timescaledb-toolkit==1.18.0 # Wymaga instalacji w kontenerze Timescale
prophet==1.1.5 # Do predykcji
```

### 8. Szacowany Timeline

_Dostosowany do nowej, ambitniejszej listy faz._

| **Faza**                                | **Czas**           | **Zespół**           |
| --------------------------------------- | ------------------ | -------------------- |
| Faza 0: POC                             | 1 tydzień          | Wszyscy              |
| Faza 1: MVP & K8s                       | 3-4 tygodnie       | Wszyscy              |
| Faza 2: Security & Obserwowalność (PLT) | 3 tygodnie         | Wszyscy              |
| Faza 3: GitOps & Alerty                 | 2 tygodnie         | (DevOps)             |
| Faza 4: Dokończenie Funkcji             | 2 tygodnie         | Wszyscy              |
| Faza 5: Wizja (Funkcje Flagowe)         | 3-4 tygodnie       | Wszyscy              |
| **TOTAL**                               | **~14-16 tygodni** | **4-osobowy zespół** |
