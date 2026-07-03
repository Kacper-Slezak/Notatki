import os
import shutil

# --- KONFIGURACJA ŚCIEŻEK ---
VAULT_ROOT = "."
ARCHIVE_DIR = os.path.join(VAULT_ROOT, "04 Archiwum")
DASHBOARDS_DIR = os.path.join(VAULT_ROOT, "Dashboards")
PROJECTS_DIR = os.path.join(VAULT_ROOT, "01 Projekty")
TEMPLATES_DIR = os.path.join(VAULT_ROOT, "05 Szablony")

# 1. LISTA RZECZY DO ZARCHIWIZOWANIA (Przestarzałe)
TO_ARCHIVE = [
    "01 Projekty/Semestr 6 TODO.md",
    "01 Projekty/Biblioteka predict",
    "01 Projekty/Klasyfikator pakietów",
    "01 Projekty/Koło naukowe",
    "01 Projekty/Ops Automatization"
]

# 2. LISTA RZECZY DO RESTRUKTURYZACJI
TO_MOVE = {
    # Źródło : Docelowe miejsce
    "01 Projekty/FIRE/DevOps/Umiejętności": "03 Baza Wiedzy/Nauka/DevOps"
}

# --- TREŚCI NOWYCH PLIKÓW (DASHBOARDY I SZABLONY) ---

DASHBOARD_CONTENT = """---
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
"""

SUMMER_PLAN_CONTENT = """# ☀️ Master Plan Letni (Lipiec & Sierpień 2026)

## 🩺 Tydzień 1 & 2 Lipca: Administracja Zdrowiem (One-off)
- [ ] Umówić pobranie krwi (Internista GP)
- [ ] Umówić wizytę u Dentysty
- [ ] Umówić Fizjoterapeutę
- [ ] Umówić Optometrystę

## 🎓 CKA Sprint (Lipiec)
- [ ] Przerobić sekcję Core Concepts & Scheduling
- [ ] Przerobić sekcję Networking & Storage
- [ ] Zrobić Mock Exam #1 (killer.sh)
- [ ] Zrobić Mock Exam #2 (killer.sh)
- [ ] **Zdać egzamin CKA (Deadline: Koniec Lipca)**

## 🚀 Praca Inżynierska (K8s, Envoy, mTLS, PQC)
### Lipiec
- [ ] Wybrać algorytmy PQC (Kyber/Dilithium) do testów
- [ ] Zestawić lokalny klaster testowy (Kind / Minikube)
- [ ] Skonfigurować Envoya z bazowym mTLS (bez PQC)
- [ ] Skonfigurować narzędzia obciążeniowe (Fortio/wrk)

### Sierpień
- [ ] Zaimplementować filtry PQC w Envoy
- [ ] Przeprowadzić testy opóźnień i narzutu na CPU
- [ ] Przeanalizować dane z testów
- [ ] Napisać rozdział badawczy i wnioski

## 💻 Projekty Osobiste
- [ ] SOTP: Ustabilizować stack monitoringu (Prometheus/Grafana)
- [ ] Portfolio Website: Opublikować stronę z projektami (Docker/Hugo/K8s)
- [ ] Cyfrowy Schron: Odpalić Immich lub skończyć skrypt Pythona na serwerze

## 📆 Harmonogram Typowego Dnia Roboczego
1. **06:00 - 08:00:** Bieg/Trening + BuJo (3 MITs)
2. **08:00 - 13:00:** 🏢 **Praca IBM (5h MAX)** - *Po 13:00 zamykasz firmowego Slacka!*
3. **13:00 - 14:00:** Reset, Obiad
4. **14:00 - 16:30:** 🎓 **Deep Work:** Inżynierka / CKA
5. **17:00 - 19:30:** Projekty Osobiste (SOTP/Portfolio) + Czytanie (1h)
6. **Po 19:30:** 🚫 ZERO EKRANÓW (Kaletnictwo, Relacje, Odpoczynek)
"""

DAILY_TEMPLATE_CONTENT = """---
date: {{date:YYYY-MM-DD}}
ibm_hours: 0
thesis_hours: 0
running: false
calisthenics: false
mobility: false
reading_minutes: 0
tags: [daily]
---
# {{date:dddd, MMMM D}}

## 🎯 3 MITs (Przepisane z Bullet Journala)
- [ ] 
- [ ] 
- [ ] 

## ⏱️ Logowanie Czasu (Wypełnij Wieczorem)
* IBM Hours: 0
* Thesis Hours: 0

## 🌙 Refleksja Wieczorna
* **Zwycięstwo dnia:** * **Wąskie gardło (co poszło nie tak):** * **Priorytet na jutro (Zapisz to w fizycznym BuJo):** """

def force_move(src, dest):
    """Przenosi pliki/foldery nadpisując je w docelowym miejscu w razie konfliktu."""
    if not os.path.exists(src):
        return
    if not os.path.exists(dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        shutil.move(src, dest)
        print(f"✅ Przeniesiono: {src} -> {dest}")
    except Exception as e:
        print(f"⚠️ Błąd podczas przenoszenia {src}: {e}")

def run_deep_refactor():
    print("🚀 ROZPOCZYNAM GŁĘBOKĄ REFAKTORYZACJĘ VAULTA...\n")

    # 1. ARCHIWIZACJA STARYCH PROJEKTÓW
    print("🗄️ 1. Czyszczenie starych projektów (Przenoszenie do Archiwum)...")
    for item in TO_ARCHIVE:
        full_src = os.path.join(VAULT_ROOT, item)
        if os.path.exists(full_src):
            basename = os.path.basename(full_src)
            full_dest = os.path.join(ARCHIVE_DIR, basename)
            force_move(full_src, full_dest)
        else:
            print(f"ℹ️ Nie znaleziono '{item}' (Zapewne już zarchiwizowane).")

    # 2. RESTRUKTURYZACJA BAZY WIEDZY
    print("\n🧠 2. Przenoszenie notatek do odpowiednich sekcji Bazy Wiedzy...")
    for src, dest in TO_MOVE.items():
        full_src = os.path.join(VAULT_ROOT, src)
        full_dest = os.path.join(VAULT_ROOT, dest)
        if os.path.exists(full_src):
            force_move(full_src, full_dest)

    # 3. GENEROWANIE NOWYCH DASHBOARDÓW I CHECKLIST
    print("\n🛠️ 3. Generowanie Dashboardów i Checklist...")

    # Upewnienie się, że foldery docelowe istnieją
    os.makedirs(DASHBOARDS_DIR, exist_ok=True)
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    os.makedirs(TEMPLATES_DIR, exist_ok=True)

    # Zapis Dashboardu
    dashboard_path = os.path.join(DASHBOARDS_DIR, "00_Sovereign_Dashboard.md")
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(DASHBOARD_CONTENT)
    print("✅ Wygenerowano główny Dashboard: Dashboards/00_Sovereign_Dashboard.md")

    # Zapis Planu Letniego z Checklistami
    plan_path = os.path.join(PROJECTS_DIR, "00_Plan_Letni_Checklisty.md")
    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(SUMMER_PLAN_CONTENT)
    print("✅ Wygenerowano Plan Letni: 01 Projekty/00_Plan_Letni_Checklisty.md")

    # Zapis Szablonu Codziennego
    template_path = os.path.join(TEMPLATES_DIR, "Daily_Sovereign_Template.md")
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(DAILY_TEMPLATE_CONTENT)
    print("✅ Wygenerowano Szablon Codzienny: 05 Szablony/Daily_Sovereign_Template.md")

    print("\n🎯 GŁĘBOKA REFAKTORYZACJA ZAKOŃCZONA SUKCESEM.")
    print("-> Otwórz 'Dashboards/00_Sovereign_Dashboard.md' w Obsidianie, aby zacząć pracę.")

if __name__ == "__main__":
    run_deep_refactor()