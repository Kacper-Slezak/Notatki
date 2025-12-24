---
typ:
technologia:
status: nowa
data: 2025-12-22
---
---

# Labels and Selector

##  Co to jest? 
Klasyfikasja i grupo9wanie jest umożliwiane miedzy nim sa to etykiety przypisane do obiektów

##  Jak to działa?
Jest to używane do filtrownia i wybierania obiektów
Dla każdego obiektu dopisz etykiete aby móc je grupować i filtrować
W przypadku definiowania [[Deployment]] lub [[ReplicaSet]] używamy `matchLabels:` aby grupować [[Pod|Pody]]
Dodatkowo możemy dodac annotations do obiektu w metadata i służy to do dotakowych informacji jakie chcemy przekazać innym 


##  Code Snippet / Komendy
```yaml
...
metadata:
  name: simple_example
  labels:
    app: App1
    type: frontend
```
```bash
kubectl get pods --selector app=App1
```

## Powiązania
[[Deployment]]
[[ReplicaSet]]
[[Pod]]

## Notatki własne