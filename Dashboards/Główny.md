---
typ: dashboard
---

#  Dashboard Główny

##  Dzisiaj: {{date:dddd, D MMMM YYYY}}

[[{{date:YYYY-MM-DD}}| Otwórz Dzisiejszą Notatkę]] | [[{{date:YYYY-MM-DD,+1}}| Jutro]]

---

##  Kluczowe Obszary

| Obszar    | Link                              |
| --------- | --------------------------------- |
| Kariera   | [[Kariera Dashboard]]             |
| Wellbeing | [[Wellbeing Dashboard]]           |
| Finanse   | [[Budget 2025]]                   |
| Projekty  | [[Master Hub - DevOps & Kariera]] |

---

##  Szybkie Akcje

-  [[00 Inbox/Quick Notes|Szybka Notatka]]
-  [[Trening - Plan|Plan Treningowy]]
-  [[Pomysły na wpisy|Blog - Pomysły]]

---

##  Postęp w Tym Tygodniu
```dataview
TABLE WITHOUT ID
  file.link AS "Dzień",
  trening AS "Trening",
  rozciąganie AS "Rozciąganie",
  stres AS "Stres"
FROM "06 Daily Notes"
WHERE file.day >= date({{monday:YYYY-MM-DD}}) 
  AND file.day <= date({{date:YYYY-MM-DD}})
SORT file.day DESC
```

---

##  Hot Topics (Ostatnie 5 notatek)
```dataview
TABLE file.mtime AS "Ostatnia Edycja"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 5
```

---

##  Przypomnienia

- [ ] Weekly Review w niedzielę wieczorem
- [ ] Sprawdź [[Firmy|Oferty Pracy]] (czwartek)
- [ ] Video call z dziewczyną (wtorek + sobota)