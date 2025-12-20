---
typ: wiedza
projekt: 00 SOTP Dashboard
---
#  Stack Technologiczny i Decyzje (ADR)

| Warstwa | Technologia | Link do Wiedzy | Uzasadnienie |
| :--- | :--- | :--- | :--- |
| **Orkiestracja** | [[K3d]] + [[Helm]] | [[Kubernetes]] | Lekki K8s do deweloperki, Helm do templatingu. |
| **GitOps** | [[ArgoCD]] | [[CI/CD]] | Standard branżowy, auto-sync, wykrywanie dryfu konfiguracji. |
| **Backend** | [[FastAPI]] | [[Python]] | Asynchroniczność, Pydantic, łatwa integracja z AI. |
| **Kolejki** | [[Celery]] + [[Redis]] | [[Systemy Rozproszone]] | Skalowalne przetwarzanie zadań w tle. |
| **Baza Danych** | [[PostgreSQL]] | [[SQL]] | Solidny standard dla danych relacyjnych. |
| **Time Series** | [[TimescaleDB]] | [[Bazy Danych]] | Wydajność dla metryk, SQL-owy interfejs. |
| **Sekrety** | [[HashiCorp Vault]] | [[Cybersecurity]] | Dynamiczne sekrety, brak haseł w kodzie. |
| **Metryki** | [[Prometheus]] | [[Monitoring]] | Standard w świecie Cloud Native. |
| **Logi** | [[Loki]] | [[Loggowanie]] | "Prometheus dla logów", tanie składowanie. |
| **Wizualizacja** | [[Grafana]] | [[Dashboardy]] | Jeden UI dla całego stosu obserwowalności. |
