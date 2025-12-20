---
typ: projekt
status: w-produkcji
priorytet: 7
tagi:
  - devops
  - k8s
  - observability
  - python
data_aktualizacji: 2025-12-20
---
#  SOTP - System Observability & Telemetry Platform

> [!abstract] Cel Projektu
> Budowa kompleksowej platformy monitoringu infrastruktury sieciowej z wykorzystaniem [[Kubernetes]], podejścia [[GitOps]] oraz pełnego stosu [[Observability]] (PLT).

##  Nawigacja po projekcie
- **[[Roadmapa i Fazy]]** – Harmonogram, aktualny postęp (Faza 0-5) i kamienie milowe.
- **[[Architektura Systemu]]** – Diagramy komunikacji, warstwy aplikacji i infrastruktura.
- **[[Stack Technologiczny]]** – Lista użytych narzędzi z uzasadnieniem (decyzje ADR).
- **[[Wymagania i Role]]** – Kto co robi i czego oczekujemy od systemu.

##  Status
- **Obecna Faza:** [[Roadmapa i Fazy#FAZA 2 Bezpieczeństwo i Monitoring|FAZA 2: Bezpieczeństwo i Monitoring]]
- **Najbliższy Milestone:** Uruchomienie kolektora [[ICMP]] w kontenerze.

##  Kluczowe pojęcia (Wiedza)
- [[GitOps]] z użyciem [[ArgoCD]]
- [[Service Mesh]] ([[Linkerd]])
- Bezpieczeństwo [[Zero Trust]] i zarządzanie sekretami przez [[HashiCorp Vault]]
- Monitoring: [[Prometheus]], [[Loki]], [[Tempo]]