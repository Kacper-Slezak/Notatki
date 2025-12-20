---
typ: plan
projekt: 00 SOTP Dashboard
status: zdefiniowane
---

#  Wymagania i Role w Zespole

## Zespół Projektowy (4 Osoby)

Jasny podział odpowiedzialności to klucz do uniknięcia konfliktów przy merge'owaniu.

###  Osoba 1: Lider DevOps & Infrastruktura
**Odpowiedzialność:** Fundamenty platformy i automatyzacja.
- **Kluczowe zadania:**
    - Konfiguracja klastra [[Kubernetes]] ([[K3d]]).
    - Zarządzanie infrastrukturą jako kod: [[Helm]], [[Terraform]] (opcjonalnie).
    - Wdrożenie [[GitOps]] przy użyciu [[ArgoCD]].
    - Konfiguracja stosu obserwowalności ([[Prometheus]], [[Loki]], [[Tempo]]).
    - Bezpieczeństwo infrastruktury ([[HashiCorp Vault]], [[Linkerd]]).

###  Osoba 2: Frontend Developer
**Odpowiedzialność:** Doświadczenie użytkownika (UX/UI).
- **Kluczowe zadania:**
    - Budowa interfejsu w [[Next.js]] + [[React]].
    - Stylowanie za pomocą [[Tailwind CSS]].
    - Wizualizacja danych (wykresy metryk, logi).
    - Integracja z API Backendowym.

###  Osoba 3: Specjalista ds. Kolektorów
**Odpowiedzialność:** "Oczy i uszy" systemu - zbieranie danych z sieci.
- **Kluczowe zadania:**
    - Implementacja workerów w [[Python]].
    - Protokoły sieciowe: [[ICMP]] (ping), [[SNMP]] (v2/v3), [[SSH]] (netmiko).
    - Parsowanie surowych danych (np. TextFSM).

###  Osoba 4: Backend Developer
**Odpowiedzialność:** Logika biznesowa i API.
- **Kluczowe zadania:**
    - Rozwój API w [[FastAPI]].
    - Modele bazy danych ([[SQLAlchemy]]) i migracje ([[Alembic]]).
    - Logika zadań asynchronicznych ([[Celery]]).
    - Integracja z bazami [[PostgreSQL]] i [[TimescaleDB]].

---

##  Wymagania i Metryki Sukcesu (KPI)

### Wymagania Funkcjonalne
1. **Pełna Obserwowalność:** System musi zbierać metryki, logi i ślady (Tracing) w jednym dashboardzie [[Grafana]].
2. **Bezpieczeństwo Zero-Trust:** Brak haseł w kodzie (użycie Vault), szyfrowanie mTLS między serwisami.
3. **Automatyzacja:** Wykrywanie awarii i (w fazie 5) automatyczna naprawa (Self-healing).

### Wymagania Niefunkcjonalne (SLA)
| Metryka | Cel |
| :--- | :--- |
| **Dostępność (Uptime)** | 99.5%+ |
| **Czas odpowiedzi API** | < 200ms (p95) |
| **Skuteczność Pollingu** | > 99% udanych prób odpytania urządzeń |
| **Bezpieczeństwo** | 0 krytycznych podatności w skanach obrazów |
| **Deployment** | W pełni zautomatyzowany przez [[GitOps]] (push-to-deploy) |