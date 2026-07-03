---
typ: projekt
status: planowanie
priorytet: "5"
data_rozpoczecia: 2025-12-23
technologia:
  - Python
  - Linux
  - Ansible
  - Automation
---

#  Ops Automation – SRE Bootcamp

> [!abstract] Cel Projektu
> 
> Celem repozytorium jest udokumentowanie ścieżki rozwoju w obszarze SRE/DevOps. Projekt zawiera zbiór skryptów, konfiguracji i narzędzi automatyzujących codzienne zadania administracyjne w systemach Linux (RHEL/Debian) z wykorzystaniem Python, Bash oraz Ansible.
> 
> **Docelowe stanowisko:** SRE / Site Reliability Engineer (stack IBM/Red Hat).

---

##  Mapa Umiejętności (Roadmap)

###  1. Linux Automation (Shell & System)

Fundament pracy z systemem. Skrypty Bashowe i manipulacja strumieniami.

- [ ] **Strumienie i Przekierowania:**
    
    - [ ] STDOUT (1), STDERR (2), STDIN (0)
        
    - [ ] Operatory: `>` (nadpisz), `>>` (dopisz), `2>` (błędy), `2>&1`, `|` (pipe)
        
- [ ] **Text Processing (Text Fu):**
    
    - [ ] `grep` (wyszukiwanie wzorców, flagi -i, -v, -r, -E)
        
    - [ ] `awk` (wyciąganie kolumn, proste operacje matematyczne)
        
    - [ ] `sed` (edycja tekstu w locie, zamiana ciągów)
        
    - [ ] `sort`, `uniq`, `wc`, `head`, `tail -f`
        
- [ ] **Zarządzanie Systemem:**
    
    - [ ] Procesy: `ps aux`, `top`/`htop`, `kill` (sygnały), `pgrep`
        
    - [ ] Uprawnienia: `chmod` (octal), `chown`, `sudoers`, Sticky Bit, SUID
        
    - [ ] Systemd: tworzenie własnych plików `.service`, `systemctl`, `journalctl`
        
- [ ] **Harmonogramowanie:**
    
    - [ ] `cron` (składnia crontab) & `at`
        

###  2. Python for Ops

Logika automatyzacji, zastępująca skomplikowane skrypty Bash.

- [ ] **Interakcja z Systemem:**
    
    - [ ] `os` (zmienne środowiskowe, nawigacja po katalogach)
        
    - [ ] `shutil` (kopiowanie, przenoszenie plików, disk usage)
        
    - [ ] `sys` & `argparse` (obsługa argumentów CLI)
        
    - [ ] `subprocess` (wywoływanie komend Linuxowych z poziomu Pythona - **Kluczowe**)
        
- [ ] **Dane i Logowanie:**
    
    - [ ] `json` / `yaml` (parsowanie plików konfiguracyjnych)
        
    - [ ] `logging` (profesjonalne logowanie zdarzeń zamiast print)
        
    - [ ] `datetime` (operacje na czasie, rotacja logów)
        
- [ ] **Sieć i Stabilność:**
    
    - [ ] `requests` (sprawdzanie statusu HTTP usług)
        
    - [ ] Obsługa błędów: bloki `try / except / else / finally`
        

###  3. Ansible (Infrastructure as Code)

Zarządzanie konfiguracją w skali.

- [ ] **Podstawy:**
    
    - [ ] Inventory (hosts, groups, variables)
        
    - [ ] Konfiguracja `ansible.cfg`
        
- [ ] **Playbooks:**
    
    - [ ] Struktura YAML
        
    - [ ] Tasks & Modules (`yum/apt`, `copy`, `service`, `file`, `user`)
        
    - [ ] Handlers (reakcja na zmiany, np. restart usługi)
        
- [ ] **Zaawansowane:**
    
    - [ ] Templating (Jinja2) - podstawy
        

---

##  Katalog Zadań i Projektów

W tym repozytorium znajdują się trzy kategorie zadań. Każde zadanie powinno być osobnym skryptem/katalogiem.

###  Poziom 1: Mini-Skrypty (Drile)

_Krótkie, jednofunkcyjne narzędzia do nauki konkretnej biblioteki._

1. **`log_filter.sh`** (Bash): Jednolinijkowiec, który z pliku logów wyciąga tylko błędy 500, sortuje je po IP i zapisuje do nowego pliku.
    
    - _Użyte:_ `grep`, `awk`, `sort`, `uniq`.
        
2. **`backup_rotator.py`** (Python `os` + `shutil`): Skrypt, który pakuje wskazany folder do `.zip`, dodaje datę do nazwy i usuwa backupy starsze niż 7 dni.
    
3. **`process_killer.py`** (Python `subprocess`): Skrypt, który szuka procesu po nazwie i go zabija, jeśli zużywa za dużo RAMu (symulacja).
    
4. **`json_converter.py`** (Python `json`): Skrypt zamieniający surowy plik tekstowy (np. lista userów: `imie,nazwisko,wiek`) na poprawny plik JSON.
    

###  Poziom 2: Użytkowe Narzędzia Ops

_Skrypty, które realnie mogłyby działać na produkcji._

1. **`health_check_cli.py`**
    
    - **Opis:** Narzędzie CLI (użyj `argparse`), które przyjmuje adres URL i port.
        
    - **Działanie:** Sprawdza czy usługa odpowiada (HTTP 200). Sprawdza ping. Loguje wynik do pliku używając modułu `logging`. W przypadku błędu wysyła "alert" (np. print na czerwono do STDERR).
        
2. **`user_onboarding.sh` + Ansible**
    
    - **Opis:** Automatyzacja tworzenia użytkownika.
        
    - **Działanie:** Skrypt przyjmuje nazwę usera -> generuje mu hasło -> tworzy go w systemie -> dodaje do grupy docker -> wymusza zmianę hasła przy logowaniu.
        

###  Poziom 3: Projekty Integrujące (Capstone)

_Duże zadania łączące Linuxa, Pythona i Ansible._

#### Projekt A: "The Watchdog Service"

Stworzenie własnej usługi systemowej monitorującej zasoby.

1. **Python:** Skrypt `watchdog.py`, który w pętli sprawdza `disk_usage` i status serwera Nginx.
    
2. **Linux:** Skonfigurowanie tego skryptu jako usługi **Systemd** (`watchdog.service`), która wstaje automatycznie po restarcie systemu i ma skonfigurowany autostart.
    
3. **Logika:** Jeśli dysk > 90%, skrypt czyści katalog `/tmp`. Jeśli Nginx leży, próbuje go podnieść komendą `systemctl restart nginx`.
    

#### Projekt B: "Environment Bootstrapper"

Jeden komenda, która stawia środowisko developerskie od zera.

1. **Ansible:** Playbook, który instaluje pakiety (vim, git, python3, docker), kopiuje pliki konfiguracyjne (`.bashrc`), tworzy strukturę katalogów.
    
2. **Python Wrapper:** Skrypt `bootstrap.py`, który pyta użytkownika o konfigurację (np. "Czy instalować Docker? T/N"), generuje dynamicznie plik `inventory` lub zmienne dla Ansible i uruchamia playbooka przez `subprocess`.
    

---

##  Tech Stack & Environment

|**Kategoria**|**Narzędzia**|
|---|---|
|**OS**|Linux (Ubuntu/Debian lub CentOS/RHEL - uruchamiane na VM lub WSL2)|
|**Języki**|Python 3.10+, Bash|
|**Automatyzacja**|Ansible Core|
|**Kontrola Wersji**|Git, GitHub|
|**Edytor**|VS Code / Vim (do edycji na serwerze)|

---

##  Zasoby i Linki

- [[Linux MOC]] - moje prywatne notatki z komend.
    
- [Python Module of the Week](https://pymotw.com/3/) - Biblia modułów standardowych.
    
- [Linux Journey](https://linuxjourney.com/) - Najlepsze źródło podstaw Linuxa.
    
- [Ansible Documentation](https://docs.ansible.com/)
    
- [ExplainShell.com](https://explainshell.com/) - Do analizy trudnych komend bashowych.