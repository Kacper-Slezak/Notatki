---
typ: dashboard
---
#  Dashboard Główny

##  Dzisiaj
```dataviewjs
const today = moment().format("YYYY-MM-DD");
const tomorrow = moment().add(1, 'days').format("YYYY-MM-DD");
dv.paragraph(`**${moment().format("dddd, D MMMM YYYY")}**`);
dv.paragraph(`[[${today}| Dzisiejsza notatka]] | [[${tomorrow}| Jutro]]`);
```

---

##  Postęp w tym tygodniu
```dataview
TABLE WITHOUT ID
  file.link AS "Dzień",
  choice(trening, "✅", "❌") AS "Trening",
  choice(rozciąganie, "✅", "❌") AS "Rozciąganie",
  (string(sen) + "/10") AS "Sen",
  (string(stres) + "/10") AS "Stres"
FROM "06 Codzienne Notatki"
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC
```

---

##  Kluczowe Obszary

| Obszar    | Link                              |
| --------- | --------------------------------- |
| Kariera   | [[Kariera Dashboard]]             |
| Wellbeing | [[Wellbeing Dashboard]]           |
| Projekty  | [[Master Hub - DevOps & Kariera]] |

---

##  Szybkie Akcje

-  [[00 Inbox/Quick Notes|Szybka Notatka]]
-  [[Trening - Plan|Plan Treningowy]]
-  [[Pomysły na wpisy|Blog - Pomysły]]

---

##  Hot Topics (Ostatnie 5 edycji)
```dataview
TABLE WITHOUT ID
  file.link AS "Notatka",
  file.mtime AS "Edycja"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 5
```

---

##  Przypomnienia

- [ ] Weekly Review w niedzielę wieczorem
- [ ] Sprawdź oferty pracy (czwartek)
- [ ] Video call z dziewczyną (wtorek + sobota)