---
typ: nauka
technologia:
  - Kubernetes
status: do-powtórki
data: 2025-12-20
---
---

# Services

##  Co to jest? (ELI5)

1. Umożlwia połączenie między komponentami z rzeczami poza kontenerem i samymi komponentami groupami [[Pod]]


##  Jak to działa?

1. **Typy**

- Serwis znajduje się miedzy podem a zewnętrznym komputerem

	**NodePort**
	- Słucha portu na [[Node]] i przekazuje do [[Pod]]
	- Port na [[Pod]] jest nazwany **TargetPort** np. 80
	- Port na [[Services]] dowiązany do TargetPortu nazwany jest **Port** np. 80
	- Port na [[Node]] to **NodePort** jest on z zakresu 30000-32767 podstowowo


	**ClusterIP**
	- Podstawowe, gdy nic nie zdefinujesz
	- Tworzy wirtualne IP, aby umożliwić komunikacje miedzy różnymi serwisami w klastrze
	- Grupuje Pody razem i losowo przypsiuje ruch do konkretnego [[Pod]]
	
	**LoadBalancer**
	- Służy do ruchu zewnętrznego i LoadBalancingu ruchu
	- Głównie używa natywnego LoadBalancera z chmury
	- Gdy nie ma wsparcia to będzie dizałał jak NodePort

2. **Kilka Podów w jednym Nodzie**

	- W tym przypadku Serwis bierze wszytskei [[Pod]] któe mają poprawne labels i używa algorytmu Losowego aby rozłożyć ruch

3. **Kilka Podów w kilku Nodach**

	- Działa tak sam jak w poprzednim przypadku
##  Code Snippet / Komendy
	NodePort
	LoadBalancer
```yaml
apiVersion: v1
kind: Service
metadata:
	name: myapp-service
spec:
	type: NodePort/LoadBalancer
	ports:
	 - targetPort: 80
	   port: 80 - needed
	   nodePort: 30008
	selector:
		app: myapp
		type: frontend
```

	ClusterIP
```yaml
apiVersion: v1
kind: Service
metadata:
	name: back-end
spec:
	type: ClusterIP
	ports:
	 - targetPort: 80
	   port: 80 - needed
	selector:
		app: myapp
		type: back-end
```

## Powiązania

## Notatki własne