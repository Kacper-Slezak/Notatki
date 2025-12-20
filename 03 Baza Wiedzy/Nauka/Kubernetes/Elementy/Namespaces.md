---
typ: nauka
technologia:
  - Kubernetes
status: do-powtórki
data: 2025-12-20
---
---

# Namespaces

##  Co to jest? (ELI5)
 - Jest to w pewnym sensie dom wewnątrz klastra, służa do izolowani pewnych części
 - Można stworzyć kilka namespaces
 - Podstawowe to:
	 - kube-system
	 - kube-public
	 - default

##  Jak to działa?
- Pozwala na DNS wewnatrz [[Namespaces]]
- Aby komunikowac się z podem z innego [[Namespaces]] trzbea dodać nazwe [[Namespaces]] razem z nazwą poda np. `db-service.dev.svc.cluster.local`
- W przypadku koemnd aby dostać się do innego trzeba dodać flage --namespace
- Mozemy ograniczać zasoby dla konkretnego namespace za pomocą [[ResourceQuota]]

##  Code Snippet / Komendy
	przypisywanie namespace
```bash
kubectl get pods --namespace=example
kubectl get pods --all-namespace
kubectl create -f nazwa_pliku --namespace=example

metadata:
	namespace: dev - aby byćpewnym i nie musieć uzywac flagi

```

	tworzenie namespace
```yaml
apiVersion: v1
kind: Namespace
metadata:
	name: dev
```

```bash
kubectl create namespace dev
```

	ustawianie namespace w cli
```bash
kubectl config set-context $(kubectl config current-context) --namespace=dev
```

## Powiązania

## Notatki własne