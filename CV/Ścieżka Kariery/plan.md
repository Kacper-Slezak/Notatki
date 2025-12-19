# Szczegółowy Harmonogram Nauki: AGH + KodeKloud 

Założenie: Masz dostęp do KodeKloud Pro.

Cel: Przełamanie strachu przed pisaniem kodu "z głowy" (Imposter Syndrome) i przygotowanie praktyczne pod rekrutacje na staże (Szwajcaria/Polska) oraz do pracy inżynierskiej.

Rutyna: Codziennie min. 2h (skupionej pracy). W weekendy 4h (głębokie zanurzenie w temat).

## MIESIĄC 1: Fundamenty Linuxa & Pythona (Walka z "Pustką w Głowie")

Twoim głównym problemem nie jest brak wiedzy teoretycznej (masz ją ze studiów), tylko brak pamięci mięśniowej i pewności siebie w terminalu. Ten miesiąc ma to naprawić poprzez powtarzalność.

### Tydzień 1: Linux - Powrót do korzeni (Debugowanie i Scripting)

Nie ucz się komend na pamięć – flagi zawsze możesz sprawdzić w `man`. Ucz się **rozwiązywać problemy** i diagnozować system.

- **Kurs (KodeKloud):** _Linux System Administrator Learning Path_ (skup się na poziomach 1 i 2, szczególnie sekcje dotyczące uprawnień, procesów i sieci).
    
- **Zadanie "Bez Google" (Codzienna rozgrzewka):**
    
    - Codziennie rano otwórz czysty terminal.
        
    - Napisz skrypt w Bashu (od zera, bez szablonów), który wykonuje sekwencję:
        
        1. Sprawdza, czy proces `nginx` (lub inny, np. Twój `python app.py`) działa (używając `ps`, `pgrep` lub `systemctl`).
            
        2. Jeśli proces nie działa – podejmuje próbę jego uruchomienia.
            
        3. Sprawdza kod wyjścia (exit code) operacji uruchamiania.
            
        4. Wysyła sformatowany log (data + komunikat) do pliku `/var/log/my-app-monitor.log`.
            
    - **Cel:** Robisz to tak długo, aż będziesz w stanie napisać obsługę `if`, zmiennych i przekierowań strumieni (`>>`, `2>&1`) płynnie, bez patrzenia w dokumentację.
        

### Tydzień 2: Python for DevOps (Kluczowy tydzień!)

Tutaj leczymy kompleks programowania. W DevOps nie piszesz wielkich systemów od zera, ale musisz umieć pisać "klej" łączący usługi.

- **Kurs (KodeKloud):** _Python for DevOps_ (rekomendowany) lub _Python for Beginners_. Wersja DevOps skupia się bardziej na bibliotekach systemowych i sieciowych, co jest Ci teraz potrzebne.
    
- **Co musisz umieć napisać na kartce papieru (nie w IDE):**
    
    - **File I/O:** Otwarcie pliku konfiguracyjnego, bezpieczne przeczytanie go (`with open(...)`) i wyciągnięcie konkretnej wartości.
        
    - **Data Parsing:** Parsowanie JSON (z biblioteką `json`). To kluczowe, bo 99% API w chmurze zwraca JSON-y. Musisz umieć zamienić string na słownik i wyciągnąć z niego zagnieżdżone dane.
        
    - **API Interaction:** Wysłanie requestu HTTP (biblioteka `requests`), obsługa nagłówków (Headers) i – co najważniejsze – sprawdzenie `status_code` przed próbą odczytania treści.
        
- **Projekt (Shopping App):**
    
    - Weź plik `routes/auth.py` ze swojego projektu.
        
    - Usuń go całkowicie.
        
    - Napisz go od nowa, starając się nie patrzeć w oryginał. Skup się na dekoratorach Flaska (`@app.route`) i obsłudze błędów. Jak utkniesz – zajrzyj na chwilę, zamknij źródło i napisz kod z pamięci. To buduje pewność, że "rozumiesz, co piszesz".
        

### Tydzień 3: Shell Scripting & Automation

- **Kurs (KodeKloud):** _Shell Scripts for Beginners_. Zwróć uwagę na pętle `for`/`while` i instrukcje warunkowe `case`.
    
- **Zadanie (SOTP Backup):**
    
    - Napisz skrypt, który robi backup bazy danych Twojego projektu SOTP (zrzut `pg_dump` z kontenera PostgreSQL).
        
    - Skrypt musi pakować zrzut w archiwum `.tar.gz`.
        
    - **Wyzwanie:** Nazwa pliku musi zawierać aktualną datę (np. `backup_2023-10-27.tar.gz`).
        
    - Dodaj rotację: skrypt ma usuwać backupy starsze niż 7 dni (komenda `find`). To klasyczne zadanie rekrutacyjne.
        

### Tydzień 4: Git & Version Control

- **Kurs (KodeKloud):** _Git for Beginners_.
    
- **Ważne:**
    
    - Naucz się rozwiązywać _Merge Conflicts_ w terminalu, a nie w GUI IDE.
        
    - Zrozum różnicę między `git merge` a `git rebase`. O to bardzo często pytają na rozmowach technicznych ("Co zrobisz, żeby historia commitów była liniowa?").
        
    - Przećwicz używanie `.gitignore`, aby nie wrzucać śmieci (plików `.pyc`, `venv`, sekretów) do repozytorium.
        

## MIESIĄC 2: Konteneryzacja i Orkiestracja (Twoje Projekty)

### Tydzień 5: Docker Deep Dive

- **Kurs (KodeKloud):** _Docker for the Absolute Beginner_. Hands-on Labs są tu genialne – rób je sumiennie.
    
- **Trening (Manualny Docker):**
    
    - Uruchom cały stack projektu SOTP (Baza + Backend + Redis) używając **tylko** komend `docker run`.
        
    - Nie używaj Compose! Musisz ręcznie stworzyć sieć (`docker network create`), podpiąć do niej kontenery i zamontować wolumeny (`-v`).
        
    - To ćwiczenie uczy, jak Docker rozwiązuje nazwy hostów (DNS) wewnątrz własnej sieci i dlaczego "localhost" w kontenerze nie działa tak, jak myślisz.
        

### Tydzień 6: Docker Compose & Networking

- **Praktyka:** Wróć do swojego projektu SOTP i zrefaktoryzuj plik `docker-compose.yml`.
    
- **Zadanie "Z Pamięci":**
    
    - Czy potrafisz napisać strukturę `docker-compose.yml` dla SOTP z głowy? Spróbuj.
        
    - Zdefiniuj serwis `db` (Postgres), `web` (FastAPI) i `worker` (Celery).
        
    - Użyj sekcji `depends_on`, aby upewnić się, że aplikacja nie wystartuje przed bazą danych.
        
    - Zdefiniuj zmienne środowiskowe w bloku `environment` bezpośrednio w pliku, a potem przenieść je do `.env`.
        

### Tydzień 7 i 8: Kubernetes (CKA) - Maraton

To jest najważniejszy punkt dla Twojej inżynierki (Service Mesh) i przyszłej pracy. Service Mesh nie istnieje bez solidnego zrozumienia K8s.

- **Kurs (KodeKloud):** _Certified Kubernetes Administrator (CKA) with Practice Tests_ (instruktor: Mumshad Mannambeth).
    
- **Metoda "Imperatywna":**
    
    - Nie oglądaj tylko wideo. Rób laby ("Lightning Labs") do upadłego.
        
    - Naucz się generować YAML komendami, zamiast pisać go ręcznie. Np. zamiast pisać definicję Poda od zera, wpisz: `kubectl run my-pod --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml`.
        
    - Na egzaminie i w pracy szybkość w terminalu jest kluczowa.
        

## MIESIĄC 3: Infrastructure as Code & Chmura

### Tydzień 9: Terraform

- **Kurs (KodeKloud):** _Terraform for Beginners_.
    
- **Cel:** Zrozumienie cyklu życia: `init` -> `plan` -> `apply` -> `destroy`. Zrozum, czym jest plik stanu (`terraform.tfstate`) i dlaczego nigdy nie wolno go edytować ręcznie.
    
- **Zadanie:**
    
    - Napisz konfigurację TF, która stawia kontener Dockera (provider `kreuzwerker/docker`) na lokalnym komputerze.
        
    - Zdefiniuj zmienne (variables) dla nazwy obrazu i portu, aby kod był wielokrotnego użytku.
        

### Tydzień 10: CI/CD (GitHub Actions)

- **Kurs (KodeKloud):** _GitHub Actions_.
    
- **Projekt (Shopping App):**
    
    - Zautomatyzuj deployment Shopping App. Stwórz pipeline (`.github/workflows/main.yml`).
        
    - **Kroki pipeline'u:**
        
        1. Checkout kodu.
            
        2. Linting kodu (pylint/flake8) – niech pipeline "wybuchnie", jeśli kod jest brzydki.
            
        3. Budowa obrazu Dockera.
            
        4. Logowanie do Docker Hub (z użyciem GitHub Secrets – nigdy nie wpisuj hasła w kodzie!).
            
        5. Push obrazu z tagiem (np. SHA commita).
            

### Tydzień 11 i 12: Szlifowanie pod Inżynierkę (Service Mesh)

- **Kurs (KodeKloud):** _Istio Service Mesh_.
    
- **Inżynierka:**
    
    - To jest moment, kiedy zaczynasz pisać praktyczną część inżynierki.
        
    - Zainstaluj Istio na lokalnym klastrze (Minikube/Kind).
        
    - Wdróż tam SOTP (backend i frontend jako oddzielne deploymenty).
        
    - Skonfiguruj **Traffic Splitting** (np. 50% ruchu do wersji v1, 50% do v2) lub **Circuit Breaking** (odcięcie usługi, gdy sypie błędami). To będzie "mięso" Twojej pracy dyplomowej.
        

## Jak się uczyć, żeby nie zapomnieć? (Metoda 3 kroków)

1. **Oglądasz (Teoria):** Wykład na KodeKloud daje Ci zrozumienie "co" i "dlaczego".
    
2. **Robisz Lab (Pamięć Mechaniczna):** Klikasz w ich terminalu. To buduje podstawową pamięć mięśniową.
    
3. **Psujesz u siebie (Głębokie Zrozumienie):** To najważniejszy krok.
    
    - Weź kod z labu (np. deployment K8s).
        
    - Wrzuć go do swojego klastra/projektu.
        
    - **Zmień jedną rzecz i popsuj:** Zmień port w serwisie, zrób literówkę w zmiennej środowiskowej, usuń uprawnienia.
        
    - Obserwuj błędy (`CrashLoopBackOff`, `Connection Refused`).
        
    - Napraw to.
        
    - Dopiero gdy naprawisz to samodzielnie, naprawdę to umiesz.