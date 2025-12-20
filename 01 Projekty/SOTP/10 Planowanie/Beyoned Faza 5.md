### FAZA 6: Wizja Długoterminowa – Ewolucja w Uniwersalną Platformę Telemetryczną

**Cel:** Po zakończeniu Fazy 5, SOTP jest w pełni funkcjonalną, bezpieczną i obserwowalną platformą do monitorowania _infrastruktury sieciowej_. Faza 6 skupia się na strategicznej transformacji z wyspecjalizowanego "NMS" (Network Monitoring System) w prawdziwą, **agnostyczną platformę telemetrii**, zdolną do ingesji, korelacji i analizy _dowolnego_ typu danych szeregów czasowych, logów i śladów.

Architektura (Celery, TimescaleDB, Loki, FastAPI) została zaprojektowana z myślą o tej elastyczności. Kolektory są jedynie "wtyczkami" do potężnego silnika przetwarzania danych.

#### 6.1 Pogłębienie Obserwowalności Sieci (Analiza Ruchu)

Obecne fazy odpowiadają na pytanie "Czy urządzenie działa?". Ta faza odpowiada na pytanie: "**Co _dokładnie_ dzieje się w mojej sieci?**".

- **Funkcja:** Analiza Ruchu Sieciowego (NetFlow / sFlow / IPFIX).
    
- **Opis:** Zbieranie, agregowanie i analizowanie metadanych o przepływach sieciowych (Kto z kim rozmawia? Jaka aplikacja generuje ruch?).
    
- **Implementacja:**
    
    1. Wdrożenie w Kubernetes dedykowanego kolektora flow (np. `goflow` lub `pmacct`).
        
    2. Skonfigurowanie go jako usługa typu `NodePort` (UDP) do odbierania danych.
        
    3. Kolektor parsuje dane i eksportuje je w dwóch formach:
        
        - **Do Loki (Preferowane):** Jako wzbogacone logi JSON. Pozwala to na potężne zapytania LogQL typu `sum by (src_ip, app_protocol) (rate(flow_bytes[5m]))`.
            
        - **Do Prometheus:** Jako zagregowane metryki (mniej szczegółowe, ale szybsze).
            
    4. Konfiguracja routerów i przełączników, aby eksportowały dane flow do kolektora.
        
- **Wartość:** Zyskujemy wgląd w "warstwę 4-7", a nie tylko "warstwę 2-3". Kluczowe dla bezpieczeństwa (wykrywanie anomalii ruchu) i planowania pojemności.
    
- **Złożoność dodania:** **Wysoka**. Wymaga nowej, wyspecjalizowanej usługi kolektora i zmian konfiguracyjnych na wszystkich monitorowanych urządzeniach.
    

#### 6.2 AIOps – Inteligentna Korelacja i Audyt

Wykorzystanie zebranych danych do generowania _wiedzy_, a nie tylko _informacji_.

- **Funkcja:** Zaawansowana Korelacja Zdarzeń (Root Cause Analysis).
    
- **Opis:** Tłumienie "szumu" alertów. Jeśli padnie główny przełącznik, nie chcemy 100 alertów "device down", tylko jeden: "Core switch down (100 child devices affected)".
    
- **Implementacja:**
    
    1. Rozszerzenie modelu `Device` (w Postgres) o pole zależności (np. `parent_device_id` lub graf zależności).
        
    2. Stworzenie nowego mikroserwisu lub logiki w `AlertingService`, która przechwytuje webhooki z Alertmanagera.
        
    3. Serwis analizuje topologię zależności i jeśli wykryje awarię nadrzędną, automatycznie tłumi alerty podrzędne i grupuje je w jeden "super-alert".
        
- **Wartość:** Drastyczna redukcja MTTR (Mean Time To Resolution). Operatorzy natychmiast wiedzą, gdzie leży prawdziwa przyczyna problemu.
    
- **Złożoność dodania:** **Wysoka**. Wymaga modelowania topologii i złożonej logiki korelacji.
    

---

- **Funkcja:** Audyt Zgodności Konfiguracji (Network Compliance).
    
- **Opis:** Wykorzystanie bazy backupów (z Fazy 5.4) do aktywnego audytu.
    
- **Implementacja:**
    
    1. Stworzenie w UI edytora "Golden Configuration" (szablonów YAML/Jinja2 definiujących pożądany stan, np. "musi mieć serwer NTP", "nie może mieć włączonego telnetu").
        
    2. Nowe zadanie Celery (`tasks/compliance_tasks.py`) uruchamiane co noc.
        
    3. Zadanie pobiera backup z Git, porównuje go z "Golden Config" i generuje raport zgodności (np. "Urządzenie X: 95% zgodne. Błąd: Włączony Telnet").
        
    4. Nowy widok w UI: "Raport Zgodności".
        
- **Wartość:** Proaktywne zarządzanie bezpieczeństwem i politykami firmy.
    
- **Złożoność dodania:** **Średnia**. Fundament (backupy Git) już istnieje. Wymaga "tylko" logiki porównawczej i UI.
    

#### 6.3 Architektura Wtyczek (Plugin) – Ekspansja na Nowe Domeny

Formalne potraktowanie kolektorów jako wymiennych wtyczek.

- **Funkcja:** Monitoring **IoT / Urządzeń Domowych** (MQTT).
    
- **Opis:** Zbieranie danych z tysięcy lekkich czujników (temperatury, wilgotności, inteligentnych gniazdek).
    
- **Implementacja:**
    
    1. Dodanie do Helm charta zależności od brokera MQTT (np. `Mosquitto`).
        
    2. Stworzenie **jednego nowego pliku**: `backend/app/collectors/mqtt_collector.py`.
        
    3. Ten kolektor (używając `paho-mqtt`) łączy się z brokerem, subskrybuje tematy (`dom/salon/temperatura`) i zapisuje dane prosto do TimescaleDB.
        
- **Wartość:** Pokazuje, że SOTP to uniwersalna platforma TSDB.
    
- **Złożoność dodania:** **Niska**. Wymaga znajomości protokołu, ale idealnie pasuje do istniejącej architektury.
    

---

- **Funkcja:** Monitoring **Serwerów Linux/Windows**.
    
- **Opis:** Zbieranie metryk systemowych (CPU, RAM, Dysk, Procesy).
    
- **Implementacja:**
    
    1. SOTP nie potrzebuje nowego kolektora. Wykorzystujemy **Prometheusa**, którego już mamy.
        
    2. Wymagane jest wdrożenie agentów (`node_exporter` dla Linux, `windows_exporter` dla Windows) na docelowych serwerach.
        
    3. Konfiguracja `ServiceMonitor` w Kubernetes, aby Prometheus automatycznie wykrywał i scrapował tych agentów.
        
- **Wartość:** Ujednolicenie monitoringu sieci i serwerów w jednym dashboardzie (Grafana).
    
- **Złożoność dodania:** **Średnia**. Logika po stronie SOTP jest prosta (to tylko konfiguracja Prometheusa), ale logistyka wdrożenia tysięcy agentów na serwerach jest wyzwaniem operacyjnym.
    

---

- **Funkcja:** Monitoring **Chmury Publicznej (AWS/Azure/GCP)**.
    
- **Opis:** Zbieranie metryk z usług chmurowych (np. zużycie S3, instancje EC2, bazy danych RDS).
    
- **Implementacja:**
    
    1. Stworzenie nowych kolektorów (np. `aws_collector.py`) używających bibliotek `boto3` (AWS) lub `azure-sdk` (Azure).
        
    2. Kolektor uruchamiany jako zadanie Celery, odpytuje API CloudWatch/Azure Monitor, pobiera metryki i zapisuje do TimescaleDB.
        
    3. Klucze API do chmury są bezpiecznie przechowywane i wstrzykiwane przez **HashiCorp Vault**.
        
- **Wartość:** Pełny obraz środowiska hybrydowego (on-premise + chmura) w jednym miejscu.
    
- **Złożoność dodania:** **Średnia**. Wymaga znajomości API chmurowych, ale pasuje do modelu zadań Celery.
    

#### 6.4 Obserwowalność Samej Platformy (Meta-Monitoring)

SOTP staje się aplikacją krytyczną. Musimy monitorować _samego siebie_ z perspektywy użytkownika.

- **Funkcja:** Monitoring Syntetyczny i Real User Monitoring (RUM).
    
- **Opis:** Odpowiedź na pytanie "Czy platforma SOTP działa wolno dla moich użytkowników?".
    
- **Implementacja (Syntetyki):** Wdrożenie **Prometheus Blackbox Exporter**. Konfiguracja go, aby co 30 sekund "pingował" stronę logowania i kluczowe endpointy API. Mierzy czas odpowiedzi i dostępność z zewnątrz.
    
- **Implementacja (RUM):** Instrumentacja frontendu (Next.js) za pomocą **OpenTelemetry JS**. Przeglądarki użytkowników będą wysyłać ślady (traces) do **Tempo**, pokazując realny czas ładowania komponentów React i wywołań API.
    
- **Wartość:** Pełny wgląd w cykl życia żądania: od kliknięcia w przeglądarce (RUM), przez Ingress, po API (Tempo) i bazę danych. Zamykamy pętlę obserwowalności.
    
- **Złożoność dodania:** **Średnia**. Wymaga instrumentacji frontendu i wdrożenia nowego eksportera.
    

#### 6.5 Strategia Testowania E2E (Containerlab)

Jak zauważyłeś, testowanie kolektorów SNMP/SSH bez sprzętu jest kluczowym problemem.

- **Rozwiązanie:** Emulacja sieci za pomocą **Containerlab**.
    
- **Opis:** Containerlab to narzędzie do uruchamiania _prawdziwych obrazów systemów operacyjnych_ (np. Arista cEOS, Juniper cRPD) jako kontenerów i łączenia ich w wirtualne topologie.
    
- **Implementacja:**
    
    1. Stworzenie dedykowanego repozytorium `sotp-test-environment`.
        
    2. W repozytorium znajdują się pliki `topology.yml` (np. "dwa routery Arista połączone back-to-back").
        
    3. **Integracja z CI/CD (Faza 1-4):** Potok CI/CD (np. w `ci.yml`) na potrzeby testów E2E:
        
        - Uruchamia `containerlab deploy` na runnerze GitHub Actions.
            
        - Czeka na start wirtualnej sieci (kontenery-routery dostają adresy IP).
            
        - Uruchamia testy Pytest (`tests/e2e/test_flows.py`), które konfigurują SOTP (przez API), aby monitorował te wirtualne adresy IP.
            
        - Testy weryfikują, czy dane SNMP i SSH są poprawnie pobierane z _prawdziwego systemu operacyjnego routera_.
            
- **Wartość:** 100% realistyczne testowanie kolektorów bez kosztów sprzętowych. Gwarancja, że kod `pysnmp` i `netmiko` zadziała na produkcji.
    
- **Złożoność dodania:** **Średnia**. Wymaga skonfigurowania runnera CI z dostępem do Dockera i pobrania obrazów (np. cEOS).