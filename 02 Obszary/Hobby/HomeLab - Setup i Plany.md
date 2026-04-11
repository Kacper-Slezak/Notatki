---
typ: projekt
kategoria: hobby
status: planowanie
data_aktualizacji: 2026-03-15
---

# HomeLab — Setup i Plany

> [!abstract] Cel
> IT traktowane jak inżynieria oprogramowania. Każda konfiguracja jako kod. Nauka K8s, IaC i observability na własnym sprzęcie — bo to działa na produkcji.

---

## Sprzęt — co kupić

### Krok 1: Jeden mini PC (~500 PLN)
| Model                         | Cena       | Specs               |
|-------------------------------|------------|---------------------|
| Dell OptiPlex Micro 7060/7070 | ~500 PLN   | i5-8500T, 16GB, SSD |
| Beelink SEi12                 | ~900 PLN   | i5-12, 16GB, nowszy |

**Rekomendacja:** OptiPlex 7060/7070 — tani, popularny w homelab community, cichy, mało prądu.

### Krok 2: Klaster K8s (opcjonalnie 3 mini PC)
- 1 control plane + 2 worker nodes
- Lub k3s na jednej maszynie jako start (wystarczy do nauki)

### Gdzie kupować
- Allegro — "używany, stan bardzo dobry"
- OLX — często taniej
- Nie kupujesz nowego jeśli używany wystarczy

---

## Stack technologiczny

```
Wirtualizacja:    Proxmox VE (darmowy, open source)
Orkiestracja:     k3s (lekki Kubernetes)
GitOps:           ArgoCD
IaC:              Terraform + Ansible
CI/CD:            GitHub Actions
Monitoring:       Prometheus + Grafana
Logi:             Loki + Promtail
DNS:              Pi-hole (opcjonalnie)
Reverse Proxy:    Traefik
```

---

## Fazy wdrożenia

- [ ] **Faza 0:** Kup OptiPlex → zainstaluj Proxmox VE
- [ ] **Faza 1:** Postaw k3s jako VM → wdróż pierwszą aplikację
- [ ] **Faza 2:** ArgoCD + GitHub Actions → GitOps workflow
- [ ] **Faza 3:** Terraform dla Proxmox (IaC dla infrastruktury)
- [ ] **Faza 4:** Ansible dla konfiguracji VM
- [ ] **Faza 5:** Prometheus + Grafana + Loki
- [ ] **Faza 6:** Pi-hole + Traefik (sieć domowa jako kod)

---

## Projekt CV: HomeLab as Code

```
repo: homelab-as-code/
├── terraform/       # Infrastruktura Proxmox
├── ansible/         # Konfiguracja VM
├── k8s/             # Manifesty K8s
│   ├── apps/
│   └── system/
└── docs/
    └── README.md    # Architektura + diagramy
```

**Dlaczego ważne na CV:** Pokazuje że rozumiesz IaC w praktyce, nie tylko teorii.

---

## Zasoby
- Reddit: r/homelab
- Discord: Homelab PL
- YouTube: TechnoTim, Christian Lempa, Wolfgang's Channel

---

## Powiązane
- [[Moja Ścieżka DevOps 2025-2028]]
- [[Zakupy - Kolejka Priorytetów]]
