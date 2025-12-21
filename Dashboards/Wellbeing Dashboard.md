---
typ: dashboard
kategoria: wellbeing
---

#  Wellbeing Dashboard

##  Przegląd Ostatnich 30 Dni
```dataview
TABLE
  trening AS "Trening",
  rozciąganie AS "Rozciąganie",
  sen AS "Sen",
  stres AS "Stres (1-10)"
FROM "06 Daily Notes"
WHERE file.day >= date(today) - dur(30 days)
SORT file.day DESC
```

---

##  Statystyki Miesięczne

- **Treningi:** X / 20 zaplanowanych (cel: 15+)
- **Rozciąganie:** X / 30 dni (cel: 25+)
- **Średni stres:** X/10
- **Dni bez stresu (≤3):** X

---

##  Cele Wellbeing

| Cel                    | Status | Postęp |
| ---------------------- | ------ | ------ |
| Trening 3-5x/tydzień   | 🟡     | 12/20  |
| Rozciąganie codziennie | 🟢     | 25/30  |
| Sen 7-8h               | 🔴     | Uwaga! |
| Dziennik emocji        | 🟢     | 28/30  |

---

##  Wzorce Emocjonalne

> **Pytania do refleksji:**
> - Kiedy czuję się najlepiej w ciągu dnia?
> - Co wyzwala zazdrosć?
> - Jak ruch wpływa na mój nastrój?

### Ostatnie Obserwacje
```dataview
LIST emocje
FROM "06 Daily Notes"
WHERE emocje != null
SORT file.day DESC
LIMIT 7
```

---

##  Powiązane

- [[Trening - Plan]]
- [[Rozciąganie - Rutyna]]
- [[Związek - Erasmus Plan]]