#### FAZA 0: Fundamenty i POC (Walidacja)

_Cel: Udowadniamy, że pomysł działa._

- [x] **(Wspólny Start)** Wszyscy członkowie zespołu mogą uruchomić `make setup` i mają identyczne środowisko deweloperskie.
    
- [x] **(Moment "Aha!")** Widzimy pierwszy wykres w Grafanie, który pokazuje **na żywo** status PING (up/down) wirtualnego urządzenia.
    

#### FAZA 1: MVP (Pierwsza Działająca Wersja)

_Cel: Zbudowaliśmy prawdziwą aplikację na Kubernetes._

- [ ] **(Magia DevOps)** Platforma (backend, frontend, baza) uruchamia się w lokalnym klastrze K3d za pomocą _jednej komendy_ `helm install`.
    
- [ ] **(Pierwsze UI)** Użytkownik może wejść na stronę `/devices` w przeglądarce i zobaczyć tabelę (nawet jeśli pustą).
    
- [ ] **(Pełen Obieg CRUD)** Użytkownik może Dodać, Edytować i Usunąć urządzenie przez interfejs użytkownika.
    
- [ ] **(Silnik Działa!)** Po dodaniu urządzenia, jego metryki PING (ICMP) są automatycznie zbierane i zapisywane w TimescaleDB co 30 sekund.
    
- [ ] **(Siatka Bezpieczeństwa)** Pierwszy pull request zostaje automatycznie zablokowany przez potok CI (`ci.yml`), bo nie przeszedł testów.
    

#### FAZA 2: Bezpieczeństwo i Monitoring (Wersja Pro)

_Cel: Aplikacja jest bezpieczna i zbiera wartościowe dane._

- [ ] **(Bramy Zamknięte)** Użytkownik może się **zarejestrować i zalogować** na platformę.
    
- [ ] **(Tylko dla Zalogowanych)** Nie można wejść na `/devices` bez bycia zalogowanym (Protected Routes).
    
- [ ] **(Poziom Enterprise)** Aplikacja uruchamia się **bez żadnych haseł** w `values.yaml` – wszystko jest dynamicznie wstrzykiwane z Vault.
    
- [ ] **(Głębokie Dane)** Zbieramy dane SNMPv3 (CPU, RAM, interfejsy) z urządzenia.
    
- [ ] **(Efekt "Wow" w UI)** Użytkownik widzi **wykresy na żywo** (CPU, RAM, ruch sieciowy) na stronie szczegółów urządzenia.
    
- [ ] **(Centrum Dowodzenia)** Mamy pierwszy, w pełni zautomatyzowany dashboard w Grafanie (`network-overview.json`), który pokazuje stan całej sieci.
    

#### FAZA 3: Obserwowalność i GitOps (Wersja Cloud-Native)

_Cel: Osiągamy pełną widoczność i automatyzację wdrożeń._

- [ ] **(Koniec z `kubectl logs`)** Możemy w Grafanie **przeszukiwać logi** (Loki) ze wszystkich podów SOTP.
    
- [ ] **(Rentgen Systemu)** Możemy zobaczyć **pełny ślad (trace)** w Tempo, który pokazuje: Kliknięcie w UI -> Wywołanie API -> Zadanie Celery -> Zapytanie do Bazy Danych.
    
- [ ] **(Supermoc Debugowania)** Z poziomu śladu w Tempo możemy jednym kliknięciem **przeskoczyć do powiązanych logów** w Loki.
    
- [ ] **(Święty Graal DevOps)** `git push` do gałęzi `main`...
    
- [ ] **(...Automatycznie Wdraża)** ...powoduje, że ArgoCD **wykrywa zmianę i wdraża nową wersję** na klastrze bez żadnej ręcznej interwencji.
    

#### FAZA 4: Funkcjonalność Produkcyjna (Pełen Pakiet)

_Cel: Dostarczamy kompletny zestaw funkcji biznesowych._

- [ ] **(Interaktywność)** Użytkownik może otworzyć zakładkę "Konsola" i **wykonać polecenie `show version`** na routerze, widząc sparsowany wynik JSON.
    
- [ ] **(Pełna Widoczność Logów)** Użytkownik widzi **logi Syslog** (np. z routera) bezpośrednio w UI platformy (przez Loki).
    
- [ ] **(Zgodność z Prawem)** Działanie administratora (np. "Usunięcie urządzenia") tworzy **wpis w Śladzie Audytowym** (Audit Log).
    
- [ ] **(Wartość Biznesowa)** Użytkownik może wejść na `/reports` i **wygenerować raport PDF** "Dostępność urządzeń w ostatnich 7 dniach".
    
- [ ] **(Spokojny Sen)** Mamy w pełni przetestowaną procedurę `Disaster Recovery` – potrafimy odtworzyć całą platformę z backupu w mniej niż 30 minut.
    

#### FAZA 5: Wizja (Funkcje Flagowe "Wow")

_Cel: Budujemy funkcje, które wyróżniają nas na rynku._

- [ ] **(Tarcza Zero-Trust)** Cała komunikacja między serwisami (API <-> Baza) jest **automatycznie szyfrowana przez mTLS** (Linkerd).
    
- [ ] **(Samonaprawiająca się Sieć)** Prezentacja **DEMO FLAGOWEGO:**
    
    1. Ręcznie wyłączamy interfejs na wirtualnym routerze (w Containerlab).
        
    2. Prometheus wykrywa problem i wysyła alert.
        
    3. SOTP (przez Celery + Netmiko) **automatycznie loguje się na router i włącza interfejs z powrotem**. (Automatyzacja w Zamkniętej Pętli!)
        
- [ ] **(Kryształowa Kula)** Widzimy na wykresie **prognozę (predykcję)** zużycia pasma na następne 24 godziny, wygenerowaną przez TimescaleDB.
    
- [ ] **(Git dla Sieci)** Konfiguracja routera jest codziennie backupowana do repozytorium Git. Możemy zrobić `git diff` i zobaczyć, co zmieniło się wczoraj.
    

#### FAZA 6: Ekspansja (Platforma Telemetryczna)

_Cel: Udowadniamy, że jesteśmy uniwersalną platformą, a nie tylko narzędziem sieciowym._

- [ ] **(Widoczność Ruchu)** Widzimy w Grafanie dashboard "Top 10 Talkers" pokazujący, **które adresy IP generują najwięcej ruchu** (dzięki analizie NetFlow/sFlow).
    
- [ ] **(Dowód: IoT)** Podłączamy symulator MQTT i widzimy **wykres temperatury** w SOTP obok wykresu CPU routera.
    
- [ ] **(Dowód: Serwery)** Monitorujemy metryki `node_exporter` z serwera Linux w tych samych dashboardach co sieć.
    
- [ ] **(Strażnik Polityki)** Widzimy w UI nowy raport: **"Raport Zgodności Konfiguracji"**, który pokazuje "90% zgodne" i listę błędów (np. "Włączony Telnet").
    
- [ ] **(Pełen Obraz)** Widzimy w Tempo ślady wygenerowane **bezpośrednio z przeglądarki użytkownika**, pokazujące realny czas ładowania strony (RUM).