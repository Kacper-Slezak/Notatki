#### Faza 1: Przygotowanie "Robota" (Refaktoryzacja OCR)

**Cel:** Zrobienie z projektu OCR czystego mikroserwisu obliczeniowego.

1. **Czystka kodu:** Usuń z projektu OCR wszystko, co dotyczy frontendu (katalog `templates`, `static`), logowania użytkowników (`auth.py`), bazy danych użytkowników i powiadomień mailowych. Zostaw tylko to, co przetwarza obrazek.
    

2. **Stworzenie API:** Zostaw jeden główny endpoint (np. `POST /parse-receipt`), który przyjmuje plik graficzny, mieli go przez Tesseract i zwraca czysty JSON z listą produktów i cen.
    
3. **Docker:** Upewnij się, że Dockerfile dla OCR jest lekki i instaluje tylko Tesseract i niezbędne biblioteki Pythonowe.
    

#### Faza 2: Rozbudowa "Mózgu" (FastAPI Core)

**Cel:** Przejęcie logiki biznesowej przez główny serwis.

1. **Baza Danych:** W modelu FastAPI (`app/models/`) rozbuduj tabelę transakcji o szczegóły z paragonów (produkty, sklep). To tutaj będą lądować dane z OCR.
    

- **Integracja Serwisów:** Napisz w FastAPI funkcję (serwis), która po otrzymaniu uploadu od użytkownika, wysyła ten plik "w tle" do serwisu OCR (Faza 1), odbiera JSON i zapisuje wynik w bazie PostgreSQL.
    
- **Google Fit:** Upewnij się, że logika pobierania danych zdrowotnych działa i zapisuje dane do tej samej bazy PostgreSQL (żeby Grafana miała do nich dostęp).
    

#### Faza 3: Infrastruktura i Orkiestracja (DevOps Core)

**Cel:** Połączenie wszystkiego w jeden ekosystem.

1. **Docker Compose:** Stwórz jeden główny plik `docker-compose.yml`, który definiuje:
    
    - `db`: Baza PostgreSQL (wspólna dla danych).
        
    - `backend-core`: Twoje FastAPI.
        
    - `ocr-worker`: Twój okrojony Flask.
        
    - `gateway`: Serwer Nginx (lub Traefik), który kieruje ruch ze świata do FastAPI.
        
2. **Networking:** Skonfiguruj wewnętrzną sieć w Dockerze, tak aby FastAPI mogło łączyć się z OCR po nazwie serwisu (np. `http://ocr-worker:5000`), ale żeby nikt z zewnątrz nie miał dostępu do OCR bezpośrednio.
    

#### Faza 4: Obserwowalność (Twoje "Frontendowe" Wykresy)

**Cel:** Wizualizacja danych bez pisania kodu frontendu.

1. **Prometheus:** Dodaj kontener z Prometheusem do `docker-compose`. Skonfiguruj go, aby "zdejmował" metryki z Twojego FastAPI (`/metrics`).
    
2. **Grafana:** Dodaj kontener z Grafaną.
    
3. **Dashboardy w Grafanie:**
    
    - **Health Dashboard:** Podłącz Grafanę do bazy PostgreSQL i stwórz wykresy SQL (np. `SELECT steps FROM activity WHERE date = current_date`).
        
    - **Finance Dashboard:** Wykresy wydatków (np. `SELECT sum(amount) FROM transactions`).
        
    - **System Dashboard:** Wykresy z Prometheusa (czas odpowiedzi API, status serwisu OCR).
        

#### Faza 5: Szlify Końcowe (Pod CV)

1. **Dokumentacja:** Zaktualizuj README.md. Opisz architekturę, narysuj prosty schemat (nawet w ASCII), jak serwisy gadają ze sobą.
    
2. **CI/CD:** Stwórz prosty plik `.github/workflows`, który przy każdym pushu sprawdza, czy kod się buduje w Dockerze (lub uruchamia testy, jeśli masz jakieś napisane ).
	    

Dzięki temu podejściu, zamiast walczyć z CSS-em, będziesz konfigurował Grafanę i Dockera – a to są dokładnie te umiejętności, których szuka się u Junior DevOpsa.