# SOTP - System Observability & Telemetry Platform

## Opis Projektu

SOTP to platforma do monitorowania i zarządzania infrastrukturą sieciową, która umożliwia centralne zbieranie metryk, logów i zarządzanie urządzeniami sieciowymi w czasie rzeczywistym.

---

##  Główne Funkcjonalności

### 1. **Zarządzanie Urządzeniami**

- Centralna baza danych urządzeń sieciowych (routery, switche, serwery)
- Pełny CRUD z interfejsem webowym
- Automatyczne wykrywanie i kategoryzacja urządzeń
- Historia zmian i konfiguracji

### 2. **Monitoring w Czasie Rzeczywistym**

- **ICMP Monitoring**: Sprawdzanie dostępności, RTT, packet loss
- **SNMP Monitoring**: CPU, RAM, bandwidth, statusy interfejsów
- **SSH Command Runner**: Wykonywanie komend diagnostycznych na urządzeniach
- **Syslog Collection**: Zbieranie i analiza logów systemowych

### 3. **Wizualizacja Danych**

- Interaktywne dashboardy w Grafanie
- Wykresy trendów (latency, bandwidth, CPU/RAM)
- Mapy topologii sieci
- Real-time status indicators
- Custom dashboardy per urządzenie/grupa

### 4. **System Alertów**

- Konfigurowalne reguły alertów (threshold-based, pattern-based)
- Multiple notification channels (Email, Slack, Webhook)
- Alert correlation i deduplication
- Escalation policies
- Alert history i MTTR tracking

### 5. **Bezpieczeństwo**

- Multi-user authentication (JWT)
- Role-based access control (Admin, Operator, Auditor, Read-only)
- Secrets management (HashiCorp Vault integration)
- Audit logging wszystkich akcji
- Encrypted credentials storage

### 6. **Raportowanie**

- Automated reports (uptime, performance, alerts)
- Export do PDF/CSV
- Scheduled delivery (daily/weekly/monthly)
- SLA compliance reports
- Custom report builder

### 7. **API & Integracje**

- RESTful API z pełną dokumentacją
- WebSocket support dla real-time updates
- Webhook notifications
- Third-party integrations (PagerDuty, ServiceNow)

---

##  Stack Technologiczny

### Backend

- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational data (devices, users, configs)
- **TimescaleDB** - Time-series metrics
- **Redis** - Caching & message broker
- **Celery** - Distributed task queue dla collectorów

### Frontend

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Modern UI
- **React Query** - Data fetching
- **Recharts** - Interactive charts

### Monitoring & Observability

- **Prometheus** - Metrics storage
- **Grafana** - Visualization
- **Loki** - Log aggregation
- **Alertmanager** - Alert routing

### Infrastructure

- **Docker** - Containerization
- **Traefik** - Reverse proxy & load balancing
- **HashiCorp Vault** - Secrets management

---

##  Podział Ról w Projekcie

### **Role 1: Backend/DevOps Engineer**

**Główne zadania:**

- Projektowanie architektury backendu
- Implementacja REST API (FastAPI)
- Database schema design i migracje
- CI/CD pipeline setup
- Docker/Docker Compose configuration
- Security implementation (JWT, RBAC, Vault)
- Monitoring setup (Prometheus, Grafana)

**Wymagane umiejętności:**

- Python (FastAPI, SQLAlchemy, Celery)
- PostgreSQL, Redis
- Docker, Docker Compose
- Linux administration
- Git, CI/CD (GitHub Actions)

---

### **Role 2: Frontend Engineer**

**Główne zadania:**

- Implementacja UI w React/Next.js
- Responsive design (desktop + mobile)
- Integration z backend API
- Real-time data visualization (charts, graphs)
- State management (React Query, Zustand)
- Form validation i UX

**Wymagane umiejętności:**

- React, Next.js, TypeScript
- Tailwind CSS / modern CSS
- REST API integration
- Charts libraries (Recharts, Chart.js)
- Responsive design

---

### **Role 3: Network/Collector Engineer**

**Główne zadania:**

- Implementacja data collectors (ICMP, SNMP, SSH, Syslog)
- Network protocols expertise
- Data parsing i normalization
- Vendor-specific integrations (Cisco, Juniper, Arista)
- Performance optimization dla mass polling

**Wymagane umiejętności:**

- Python (async programming)
- Network protocols (SNMP, SSH, Syslog)
- Network equipment knowledge
- Vendor CLI experience
- Performance optimization

---

##  Kluczowe Metryki Projektu

- **Skala**: System dla 1000+ urządzeń
- **Performance**: < 200ms API response time, 99.5% uptime
- **Polling**: Co 30s (ICMP), co 5 min (SNMP)
- **Data Retention**: 90 dni time-series, 30 dni logs
- **Security**: OWASP Top 10 compliance, encrypted secrets

---

##  Timeline (Szacowany)

|Faza|Czas|Deliverables|
|---|---|---|
|**MVP**|3 tygodnie|Device management, ICMP monitoring, basic UI|
|**Advanced**|3 tygodnie|SNMP, SSH, security, advanced UI|
|**Production**|2-3 tygodnie|Alerts, reports, CI/CD, documentation|
|**TOTAL**|**~10 tygodni**|Production-ready platform|

---

##  Co Zyskujesz Uczestnicząc

 **Real-world experience** z production-grade stack  
 **Portfolio project** - kompleksowy system z wieloma technologiami  
 **Praca w zespole** - code reviews, Git workflow, agile practices  
 **Modern stack** - nauczysz się najbardziej востребowanych technologii  
 **Dokumentacja** - każdy feature jest udokumentowany  
 **Testing** - unit tests, integration tests, E2E tests  
 **DevOps practices** - Docker, CI/CD, monitoring, security

---

##  Kontakt & Onboarding

**Jeśli jesteś zainteresowany**, napisz na: [k.slezak2207@gmail.com] lub na discord: _pustel_

**Podaj:**
- Preferowaną rolę (Backend/Frontend/Collector)
- Swoje doświadczenie z wymienionymi technologiami
- Dostępność (ile godzin/tydzień możesz poświęcić)

**Onboarding:**

1. Setup środowiska (1 dzień)
2. Code walkthrough existing POC
3. Przydzielenie pierwszego taska z Fazy 1
4. Daily standups + code reviews

---
