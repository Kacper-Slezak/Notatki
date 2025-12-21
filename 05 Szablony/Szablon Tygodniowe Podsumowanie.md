---
typ: weekly-review
tydzień: <% tp.date.now("YYYY-[W]ww") %>
data: <% tp.date.now("YYYY-MM-DD") %>
---
#  Przegląd Tygodnia: <% tp.date.now("YYYY-[W]ww") %>

##  Podsumowanie Nawyków
```dataviewjs
// Obliczamy poniedziałek i niedzielę bieżącego tygodnia
const today = dv.date('today');
const dayOfWeek = today.toFormat('c'); // 1=poniedziałek, 7=niedziela
const monday = today.minus({ days: dayOfWeek - 1 });
const sunday = today.plus({ days: 7 - dayOfWeek });

// Pobieramy notatki z tego tygodnia
const notes = dv.pages('"06 Codzienne Notatki"')
  .where(p => p.file.day >= monday && p.file.day <= sunday)
  .sort(p => p.file.day, 'asc');

// Wyświetlamy tabelę
dv.table(
  ["Dzień", "Trening", "Rozciąganie", "Stres"],
  notes.map(p => [
    p.file.link,
    p.trening ? "✅" : "❌",
    p.rozciąganie ? "✅" : "❌",
    p.stres ? p.stres + "/10" : "-"
  ])
);
```

##  Cele vs Realizacja

| Cel Tygodnia | Status | Uwagi |
|--------------|--------|-------|
| Priorytet #1 | ⬜ | |
| Priorytet #2 | ⬜ | |
| Priorytet #3 | ⬜ | |

##  Refleksja

###  Co poszło świetnie?
- 

###  Co mogło pójść lepiej?
- 

###  Czego się nauczyłem?
- 

###  Co zmieniam w następnym tygodniu?
- 

##  Wellbeing

- **Poziom stresu (śr.):** /10
- **Jakość snu:** 
- **Treningi:** 0 / 5 zaplanowanych
- **Emocje dominujące:** 

##  Plan na Następny Tydzień

1. [ ] Priorytet #1
2. [ ] Priorytet #2
3. [ ] Priorytet #3

---

##  Powiązania
- [[<% tp.date.now("YYYY-[W]ww", 7) %>]] - Następny tydzień
- [[Wellbeing Dashboard]]