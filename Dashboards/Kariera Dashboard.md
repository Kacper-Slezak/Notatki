---
typ: dashboard
kategoria: kariera
---

#  Kariera Dashboard

##  Aktualny Status

- **Stanowisko:** SRE Intern @ IBM (start: 2.02.2025)
- **Etap:** [[Checklist|Przygotowanie do Junior DevOps]]
- **Cel:** Certyfikat CKA + 3 projekty w portfolio

---

##  Projekty

| Projekt | Status | Priorytet | Link |
|---------|--------|-----------|------|
| SOTP | Faza 1-2 | ⭐⭐⭐⭐⭐ | [[SOTP Master Document v3.5]] |
| LifeOps | Planowanie | ⭐⭐⭐ | [[MASTER PLAN - LifeOps Platform]] |
| ChronoBook | Zamrożony | ⭐⭐ | [[Master Document - Projekt ChronoBook]] |

---

##  Pipeline Rekrutacyjny
```dataview
TABLE
  firma AS "Firma",
  stanowisko AS "Stanowisko",
  status AS "Status"
FROM "02 Obszary/Kariera/Oferty Pracy/Rekrutacje"
WHERE typ = "rekrutacja"
SORT status ASC
```

### Firmy na Celowniku
- [[Firmy|Lista 30+ Firm IT/FinTech]]

---

##  Nauka (Checklist)
```dataview
TASK
FROM "02 Obszary/Kariera/Ścieżka Kariery/RoadMapy/Checklist"
WHERE !completed
LIMIT 20
```

---

##  Powiązane

- [[Master Hub - DevOps & Kariera]]
- [[Roadmapa - DevOps, Cloud, FinTech]]