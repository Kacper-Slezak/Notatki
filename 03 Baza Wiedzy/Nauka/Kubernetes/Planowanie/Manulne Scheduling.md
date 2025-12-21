---
typ: nauka
technologia:
  - Kubernetes
  - scheduler
status: nowa
data: 2025-12-21
---
---

# Manulne Scheduling

##  Co to jest? 
Jest to sposób manulanego zamiast automatycznego korzystającego z [[Scheduling - how work|Schedulera]] przypisywania odpowiedniego [[Node|Noda]] do [[Pod|Poda]]

##  Jak to działa?
1. Możemy to zrobić definiująć nodeName w pliku konfiguracyjnym .yaml przed stworzeniem poda
2. Możemy użyć `kind: Binding` i stworzyć zmianę Noda dla istniejącego Poda

##  Code Snippet / Komendy
```yaml
apiVersion: v1
kind: Binding
metadata: 
  name: nginx
target:
  apiVersion: v1
  kind: Node
  name: node02
```
```bash
curl --header "Content-Type:application/json" --request POST --data '{json format of yaml}' http://$SERVER/api/v1/namespaces/default/pods/$PODNAME/binding/
```
## Powiązania
[[Scheduling - how work]]
[[Node]]
[[Pod]]

## Notatki własne