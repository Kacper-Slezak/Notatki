---
typ: nauka
technologia:
  - Kubernetes
status: do-powtórki
data: 2025-12-20
---
---

# ResourceQuota

##  Co to jest? (ELI5)
- Służy do ograniczania zasobów w Namespace

##  Jak to działa?
- Piszemy plik yaml, w którym ograniczamy zasoby w specyfikacji

##  Code Snippet / Komendy
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
	name: compute-quota
	namespace: dev
spec:
	hard:
	  pods: "10"
	  requests.cpu: "4"
	  requests.memory: 5Gi
	  limits.cpu: "10"
	  limits.memory: 10Gi 
```

## Powiązania

## Notatki własne