---
typ: MOC
temat: kubernetes
status: aktywny
priorytet: "10"
---

#  Kubernetes MOC (Map of Content)

> [!abstract] Cel
> Centralny punkt nawigacji po ekosystemie K8s. Łączy teorię, komendy i praktyczne wdrożenia w projektach (np. SOTP).

---

##  Architektura i Koncepcje
- [[Kubernetes Core Concepts|Kluczowe Pojęcia]]
- [[Kubernetes Podstawy|Wprowadzenie do K8s]]
- [[Docker vs containerD|Runtime kontenerowy]]

### Control Plane (Master)
- [[kube-apiserver]] - Mózg klastra
- [[etcd]] - Magazyn danych
- [[kube-scheduler]] - Planista
- [[Kube Controller Manager]]

### Node (Worker)
- [[kubelet]] - Agent węzła
- [[Kube Proxy]] - Sieciowość
- [[Worker Nodes]]

---

##  Zarządzanie klastrem
- [[Przydatne komendy|Cheat Sheet kubectl]]
- [[Deployment]] - Zarządzanie aplikacją
- [[ReplicaSet]] & [[Replications-Controller]]

---

##  Projekty i Praktyka
- [[SOTP Master Document v3.5|Wdrożenie SOTP na K8s]]
- [[MASTER PLAN - LifeOps Platform|Automatyzacja LifeOps]]

---

##  Materiały i Linki
- [Oficjalna dokumentacja](https://kubernetes.io/docs/)
- [Interaktywne tutoriale (Killercoda)](https://killercoda.com/)