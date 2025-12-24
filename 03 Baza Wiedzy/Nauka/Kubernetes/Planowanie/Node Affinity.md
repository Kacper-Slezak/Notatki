---
typ:
technologia:
status: nowa
data: 2025-12-22
---
---

# Node Affinity

##  Co to jest? 
Jest to narzędzie dzięki któremu upewniamy sie, że pod wyladuje w konkretnym [[Node|Nodzie]] spełniajacym pewne wymagania. Jest to bardziej zaawansowane i elastyczne niz [[Node Selectors]]

##  Jak to działa?
Używamy do tego dośc złożonej składni w pliku konfiguracyjny , ale dzięki temu mozemy wybrać zakres Nodów, a nie tylko jednego z konkretnym label
Dzieję się to znowu na poziomie specyfikacji `spec : affinity: ...`

Wyróżniamy rózne typy:
 - `requiredDuringSchedulingIgnoredDuringExecution`
	 - Duringscheduling - to moment w którym Pod nie jest przypisany do żadnego Noda 
		 - Kiedy nieznajdzie pasujących założeń Pod nie zostanie przypisany i bedzie w stanie pending 
	 - DuringExecution - Pod jest w running state i Przypisany do Node 
		 - Jeśli zmienią się zasady zostaną one zignorowane i bedzie dalej w tym samym Node 
 - `preferredDuringSchedulingIgnoredDuringExecution`
	 - Duringscheduling
		 -  Kiedy nieznajdzie pasujących założeń [[Scheduling - how work|Scheduler]] zignoruje zasady i przypsie do jakiegoś [[Node]]
	 - DuringExecution
		 - Jeśli zmienią się zasady zostaną one zignorowane i bedzie dalej w tym samym Node

##  Code Snippet / Komendy
```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution: / preferredDuringSchedulingIgnoredDuringExecution: 
        nodeSelectorTerms:
         - matchExpressions:
            - key: size 
              operator: Exist / NotIn

```

## Powiązania

## Notatki własne