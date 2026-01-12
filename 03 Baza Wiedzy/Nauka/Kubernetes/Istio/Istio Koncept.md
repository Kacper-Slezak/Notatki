---
typ: nauka
technologia:
  - Istio
  - Kubernetes
status: nowa
data: 2026-01-12
---
---

# Istio Koncept
 
##  Co to jest? 
Jest to darmowy i open source-owy service mesh, który zapewnia szytsko to co service mesh

##  Jak to działa?
1. Dzielimy naszą architekture na Control Plane i Data plane 
2. Control Plane składa sięz trzech komponentów skłądających sięna Istiod:
	- Citadel - zarządza generowaniem certyfikatów
	- Pilot - pomaga w service discovery
	- Galley - pomaga w validacji plików konfiguracyjnych 

3. W Data Plane jako proxy służy ENVOY na każdym serwisie, komunikuje on się z Control Plane jest to Istio Agent

##  Code Snippet / Komendy
```bash
# Miejsce na kod\

```

## Powiązania

## Notatki własne