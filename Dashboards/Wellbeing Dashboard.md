---
typ: dashboard
kategoria: wellbeing
---
## 📊 Przegląd Ostatnich 30 Dni
```dataview
TABLE WITHOUT ID
  file.link AS "Dzień",
  choice(trening, "✅", "❌") AS "Trening",
  choice(rozciąganie, "✅", "❌") AS "Rozciąganie",
  (string(sen) + "/10") AS "Sen",
  (string(stres) + "/10") AS "Stres"
FROM "06 Codzienne Notatki"
WHERE file.day >= date(today) - dur(30 days)
SORT file.day DESC
LIMIT 30
```

## 📈 Statystyki
```dataviewjs
const days = dv.pages('"06 Codzienne Notatki"')
  .where(p => p.file.day >= dv.date('today').minus({days: 30}));

const treningi = days.where(p => p.trening === true).length;
const rozciaganie = days.where(p => p.rozciąganie === true).length;
const sleepData = days.array().map(p => parseInt(p.sen) || 0).filter(x => x > 0);
const avgSen = sleepData.length > 0 ? sleepData.reduce((a,b) => a+b, 0) / sleepData.length : 0;
const stressData = days.array().map(p => parseInt(p.stres) || 0).filter(x => x > 0);
const avgStres = stressData.length > 0 ? stressData.reduce((a,b) => a+b, 0) / stressData.length : 0;

dv.paragraph(`
- **Treningi:** ${treningi} / 20 zaplanowanych (${Math.round(treningi/20*100)}%)
- **Rozciąganie:** ${rozciaganie} / 30 dni (${Math.round(rozciaganie/30*100)}%)
- **Średni sen:** ${avgSen.toFixed(1)}/10
- **Średni stres:** ${avgStres.toFixed(1)}/10
- **Dni bez stresu (≤3):** ${stressData.filter(x => x <= 3).length}
`);
```

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