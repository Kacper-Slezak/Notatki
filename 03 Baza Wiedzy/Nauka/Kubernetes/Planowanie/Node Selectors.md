---
typ: nauka
technologia:
  - Kubernetes
status: nowa
data: 2025-12-22
---
---

# Node Selectors

##  Co to jest? 
Łatwa metoda która pozwala na specyfikacje do jakiego [[Node|Noda]] ma zostac przypisany nasz [[Pod]]


##  Jak to działa?
Przypisujemy w plik ukonfugracyjnym wewnątrz specyfikacji pole `nodeSelector` i przydzielamy mu label 
Jest to bardzo podstawowe i prosty mechanizm 
Bardziej zaawansowane będzie [[Node Affinity]]

##  Code Snippet / Komendy
```yaml
spec:
 nodeSelector:
   size: Large -> label na Nodzie
```
```bash
kubectl label node node-name key=value
```

## Powiązania
[[Node]]
[[Pod]]
[[Node Affinity]]

## Notatki własne