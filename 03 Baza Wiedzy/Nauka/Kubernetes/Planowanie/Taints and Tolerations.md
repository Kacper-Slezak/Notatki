---
typ: nauka
technologia:
  - Kubernetes
  - Polityki
status: nowa
data: 2025-12-22
---
---

# Taints and Tolerations

##  Co to jest? 
Jest to używane do restrykcji który pod powienien wylądowac w któym nodzie

##  Jak to działa?
W przypadku braku restrykcji scheduler sdopasuje losowo do Node 
Na [[Node|Nodzie]] stawiamy skaze (warunek wejścia) na przykłąd Blue i w ty mmoemncie jeśli nie będzie na żadnym [[Pod|Podzie]] tolerancji ustawionej to [[Scheduling - how work| Scheduler]] nie może tam żadnego dopisać
Gdy dodamy tolernacje dany [[Pod]] będzie mógł zostac tam umieszczony przez scheduler 
`Noexecute` - nie wpuszcz a nowych [[Pod|Podów]] jednynie stare pody stworzone przed tą skazą mogązostac jeśli mają tolerancje, jeśli nie to wypadają
Skazy i Tolerancje gwarantują tylko, że pody bez zgody nie zostanaumieszczone a te ze zgdoąmogą nie gwarantują, że będą bo inny [[Node]] może je wpuścić jeśli nie ma skazy

##  Code Snippet / Komendy
```bash
kubectl taint node node-name key=value:taint-effect - wynieramy pare klucz wartosc do skazy oraz efekt w przypadku braku tolerancj

kubectl taint node node-name key=value:taint-effect- aby usunąć skaze piszzemy to samo tylk odoajemy na końcu '-'
```
`tainet-effect:`
- NoSchedule - nie można przydzielić
- PreferNoSchedule - próbuje nie przydzielić ale bez gwarancji
- NoExecute - nowe pody nie będą tu przydzielane

```yaml
spec:
  tolerations:
   - key: "app"
     operator: "Equal"
     value: "Blue"
     effect: "NoSchedule"
```
## Powiązania

## Notatki własne