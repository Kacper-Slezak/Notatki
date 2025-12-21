---
typ: dashboard
---
# 🚀 Dashboard Główny

## 📅 Dzisiaj: `$= dateformat(date(today), "cccc, d MMMM yyyy")`
`$= "[[ " + dateformat(date(today), "yyyy-MM-dd") + " | 📅 Otwórz dzisiejszą notatkę ]]" ` | `$= "[[ " + dateformat(date(today) + dur(1 day), "yyyy-MM-dd") + " | ⏭️ Jutro ]]" `

---
## 📊 Postęp w tym tygodniu
```dataview
TABLE WITHOUT ID
  file.link AS "Dzień",
  trening AS "Trening",
  rozciąganie AS "Rozciąganie",
  stres AS "Stres"
FROM "06 Codzienne Notatki"
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC
```

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