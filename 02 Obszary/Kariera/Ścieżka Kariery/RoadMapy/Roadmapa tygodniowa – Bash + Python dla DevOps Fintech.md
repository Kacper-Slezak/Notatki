
## 🔹 Etap 1: Fundamenty Bash (Tydzień 1–4)

**Cel:** pisać czytelne skrypty, używać narzędzi Unixowych.

- **Tydzień 1**
    
    - Nauka: podstawy Basha (zmienne, if/else, pętle).
        
    - Źródło: [LinuxCommand.org](http://linuxcommand.org/), [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/).
        
    - Projekt: skrypt do backupu katalogu (`tar` + timestamp).
        
- **Tydzień 2**
    
    - Nauka: `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`.
        
    - Projekt: analizator logów (`/var/log/syslog` – zlicz wystąpienia błędów).
        
- **Tydzień 3**
    
    - Nauka: funkcje w Bash, przekierowania, pipe’y.
        
    - Projekt: skrypt monitorujący wolne miejsce na dysku + alert do pliku.
        
- **Tydzień 4**
    
    - Nauka: cron, zmienne środowiskowe, `trap` (obsługa sygnałów).
        
    - Projekt: monitor SSL (sprawdzaj ważność certyfikatów, loguj wyniki).
        

---

## 🔹 Etap 2: Fundamenty Python (Tydzień 5–8)

**Cel:** podstawowe skrypty automatyzacyjne.

- **Tydzień 5**
    
    - Nauka: typy danych, pętle, funkcje, pliki (`open`).
        
    - Źródło: [LearnPython.org](https://www.learnpython.org/pl/).
        
    - Projekt: skrypt liczący sumy/średnie z pliku CSV.
        
- **Tydzień 6**
    
    - Nauka: `os`, `pathlib`, `shutil`, regex (`re`).
        
    - Projekt: automatyczny organizer plików wg rozszerzeń.
        
- **Tydzień 7**
    
    - Nauka: `json`, `requests`, `argparse`.
        
    - Projekt: pobieranie danych z API (np. kursy walut NBP), zapis do CSV.
        
- **Tydzień 8**
    
    - Nauka: moduł `logging`, wyjątki, podstawy testów (`pytest`).
        
    - Projekt: CLI narzędzie (`python script.py --input data.csv --report html`).
        

---

## 🔹 Etap 3: Bash + Python w DevOps (Tydzień 9–16)

**Cel:** łączyć oba języki, pisać skrypty przydatne w realnym środowisku.

- **Tydzień 9**
    
    - Nauka: `subprocess` w Pythonie.
        
    - Projekt: Python wywołuje Bash (`df -h`, `uptime`) i parsuje wynik.
        
- **Tydzień 10**
    
    - Nauka: logi systemowe (Bash: `tail -f`, Python: `re`).
        
    - Projekt: monitor logów aplikacji – alert przy „ERROR/FAILED TX”.
        
- **Tydzień 11**
    
    - Nauka: `rsync`, `scp`, `paramiko` (Python SSH).
        
    - Projekt: skrypt automatycznego backupu serwera (Bash + Python raport).
        
- **Tydzień 12**
    
    - Nauka: `systemctl`, obsługa usług Linux.
        
    - Projekt: skrypt restartujący usługę jeśli padnie (Python + Bash healthcheck).
        
- **Tydzień 13–14**
    
    - Nauka: `jq` (JSON w Bash), `pyyaml` (YAML w Pythonie).
        
    - Projekt: narzędzie do walidacji konfiguracji (np. sprawdza poprawność YAML/JSON).
        
- **Tydzień 15–16**
    
    - Nauka: podstawy Flask/FastAPI.
        
    - Projekt: mini-API DevOpsowe → endpoint `/health` zwracający status systemu.
        

---

## 🔹 Etap 4: Projekty fintech/DevOps (Tydzień 17–24)

**Cel:** portfolio + praktyczne narzędzia.

- **Tydzień 17–18**
    
    - Projekt: **Raport transakcji** – parser logów (Bash) + raport CSV (Python).
        
- **Tydzień 19–20**
    
    - Projekt: **Monitor certyfikatów SSL** – Bash sprawdza domeny, Python generuje raport + Slack alert.
        
- **Tydzień 21–22**
    
    - Projekt: **Pipeline CI/CD** – Bash: deploy + rollback, Python: testy przed wdrożeniem.
        
- **Tydzień 23**
    
    - Projekt: **Monitor usług** – Python odpytuje API/bazę, Bash restartuje usługę.
        
- **Tydzień 24**
    
    - Projekt końcowy (portfolio): **FinOps Toolkit**
        
        - Bash: skrypty do automatyzacji systemu (backup, monitoring).
            
        - Python: CLI + API do raportów (waluty, certyfikaty, status).
            
        - Wszystko w repozytorium GitHub.
            

---

# 📌 Jak pracować co tydzień

- **1–2h nauki teorii** (książka, tutorial, dokumentacja).
    
- **3–5h praktyki** (pisanie kodu, rozwiązywanie zadań, Codewars).
    
- **2–3h projekt** (budujesz skrypt, wrzucasz na GitHub).
    

---

👉 Po tej roadmapie masz:

- **20+ własnych projektów** (z czego 4–5 nadaje się do portfolio),
    
- umiejętność pisania skryptów Bash i Python na poziomie **production-ready**,
    
- narzędzia realnie przydatne w fintech DevOps (backup, monitoring, logi, CI/CD).
    

---
