---
typ: dashboard
kategoria: wellbeing
---
##  Przegląd Ostatnich 30 Dni
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

##  Statystyki
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
```dataviewjs
// 1. Ustawienia i dane
const folder = '"06 Codzienne Notatki"'; // Upewnij się, że nazwa jest poprawna
const dni = 30;
const start = dv.date('today').minus({days: dni});
const pages = dv.pages(folder).where(p => p.file.day >= start);

// 2. Obliczenia
const treningi = pages.where(p => p.trening === true).length;
const rozciaganie = pages.where(p => p.rozciąganie === true).length;
const dziennik = pages.where(p => p.emocje != null).length;
const avgSen = pages.array().map(p => p.sen || 0).filter(x => x > 0).reduce((a,b) => a+b, 0) / pages.length || 0;

// 3. Funkcja pomocnicza do statusów (ikonki)
const getStatus = (aktualny, cel) => {
    const ratio = aktualny / cel;
    if (ratio >= 0.9) return "🟢";
    if (ratio >= 0.6) return "🟡";
    return "🔴";
};

// 4. Budowa tabeli
dv.table(
    ["Cel", "Status", "Postęp (30 dni)", "Wartość / Średnia"],
    [
        [
            "Trening (cel: 15/msc)", 
            getStatus(treningi, 15), 
            `<progress value="${treningi}" max="15"></progress>`, 
            `${treningi} / 15`
        ],
        [
            "Rozciąganie (codziennie)", 
            getStatus(rozciaganie, 30), 
            `<progress value="${rozciaganie}" max="30"></progress>`, 
            `${rozciaganie} / 30`
        ],
        [
            "Sen (cel: > 7/10)", 
            avgSen >= 7 ? "🟢" : (avgSen >= 5 ? "🟡" : "🔴"), 
            `<progress value="${avgSen}" max="10"></progress>`, 
            `${avgSen.toFixed(1)} / 10`
        ],
        [
            "Dziennik emocji", 
            getStatus(dziennik, 30), 
            `<progress value="${dziennik}" max="30"></progress>`, 
            `${dziennik} / 30`
        ]
    ]
);
```

---

##  Wzorce Emocjonalne

> **Pytania do refleksji:**
> - Kiedy czuję się najlepiej w ciągu dnia?
> - Co wyzwala zazdrosć?
> - Jak ruch wpływa na mój nastrój?

### Ostatnie Obserwacje
```dataview
LIST emocje
FROM "06 Daily Notes/2025/12 Grudzień"
WHERE emocje != null
SORT file.day DESC
LIMIT 7
```

---

##  Powiązane

- [[Trening - Plan]]
- [[Rozciąganie - Rutyna]]
- [[Związek - Erasmus Plan]]