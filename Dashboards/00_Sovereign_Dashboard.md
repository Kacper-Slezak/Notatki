---
cssclasses: [dashboard]
---
# 🏛️ Sovereign Engineer Dashboard

> **Focus:** K8s Thesis | CKA Cert | SOTP | IBM 100h Limit

## ⏱️ Wykorzystanie limitu IBM (Miesiąc)
```dataviewjs
const pages = dv.pages('"06 Codzienne Notatki"')
  .where(p => p.date && p.date.month === dv.date("today").month);
const total = pages.array().reduce((sum, p) => sum + (p.ibm_hours || 0), 0);
dv.paragraph(`**W tym miesiącu przepracowano: ${total} / 100 godzin** 🔴`);
```

## 🎓 Deep Work Inżynierka (Suma)
```dataviewjs
const pages = dv.pages('"06 Codzienne Notatki"').where(p => p.thesis_hours);
const total = pages.array().reduce((sum, p) => sum + p.thesis_hours, 0);
dv.paragraph(`**Zainwestowano: ${total} godzin w projekt** 🚀`);
```

## 🗓️ Ostatnie 7 dni (Nawykownik)
```dataview
TABLE running as "🏃 Bieganie", calisthenics as "💪 Kalistenika", reading_minutes as "📖 Czytanie (min)", ibm_hours as "IBM (h)", thesis_hours as "Inżynierka (h)"
FROM "06 Codzienne Notatki"
WHERE date >= date(today) - dur(7 days)
SORT date ASC
```

## 📂 Szybki dostęp
- [[00_Plan_Letni_Checklisty|🔥 Mój Plan Letni (Lipiec - Sierpień)]]
- [[00 SOTP Dashboard|💻 SOTP Dashboard]]
- [[Plan Inżynierki|🎓 Plan Inżynierki]]
