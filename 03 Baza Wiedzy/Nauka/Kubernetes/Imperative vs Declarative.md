---
typ: nauka
technologia:
  - Kubernetes
status: do-powtórki
data: 2025-12-20
---
---

# Imperative vs Declarative

##  Co to jest? 
1. Imperative
	- Jest to podejście w którym opisujesz co i jak zorbić dokładnie
2. Declarative
	- Opisujesz tylko co powinno zostać zrobione, a nie jak

##  Jak to działa
1. Imperative
	- Intrukcja krok po kroku co i jak powinno zostać wykonane
	- I robimy to sami
	- używamy wbudowanych komend kubectl

2. Declarative
	- Deklarujemy tylko nasze wymagania i system lub narzędzie robi za nas
	- tworzymy dokłądne pliki yaml i działamy na nich 
	- Pozwala na łątwiejsze zarządzanie złożonymi strukturami

##  Code Snippet / Komendy
	imperative
```bash
kubectl run --image=nginx nginx
kubectl create deployment --image=nginx nginx
kubectl expose deployment nginx --port 80
kubectl edit deployment nginx
kubectl scale deployment nginx --replicas=5
kubectl set iamge deployment nginx nginx=nginx:1.18
kubectl create -f nginx.yaml
kubectl replace -f nginx.yaml
kubectl delete -f nginx.yaml
```

	declarative
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
```bash
kubectl apply -f example_file.yaml
```
## Powiązania

## Notatki własne
- W przyapdku egazminu gdy trzeba coś zrobicmałego szybkeigo używa się imperatywnego 
- Imperatywny łatwo tworzy szablony do pracy 
- W przyapodku bardziej złożonych zadań lepiej używac deklaratywnego 