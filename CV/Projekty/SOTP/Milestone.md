#### Milestone 1: "Centrum Dowodzenia" (SOTP 1.0)

_**Motto:** "Mamy obraz sytuacji. Platforma żyje."_

To jest fundament. Przechodzimy od zera do posiadania działającego pulpitu nawigacyjnego, który daje nam podstawową widoczność.

- [ ]  **ODBLOKOWANE:** Interfejs Webowy. Można wejść na stronę i się zalogować.
    
- [ ] **ODBLOKOWANE:** Inwentaryzacja. Można dodawać, edytować i usuwać urządzenia sieciowe z UI.
    
- [ ] **ODBLOKOWANE:** "Puls Sieci". Widzimy na żywo status PING (up/down) każdego urządzenia.
    
- [ ] **ODBLOKOWANE:** Pełna automatyzacja K8s. Nowy deweloper uruchamia całą platformę jedną komendą `helm install`.
    

#### Milestone 2: "Diagnostyka Głębinowa" (SOTP 1.5)

_**Motto:** "Wiemy nie tylko _CZY_ działa, ale _JAK_ działa."_

Przestajemy być prostym "pingerem". Stajemy się profesjonalnym narzędziem diagnostycznym, któremu można zaufać.

- [ ] **ODBLOKOWANE:** "Skaner Witalny". Widzimy **wykresy na żywo** dla CPU, RAM i ruchu na interfejsach.
    
- [ ] **ODBLOKOWANE:** "Twierdza Vault". Platforma nie przechowuje żadnych haseł w kodzie. Sekrety są bezpiecznie wstrzykiwane.
    
- [ ] **ODBLOKOWANE:** "Globalny Dashboard". Mamy jeden, główny pulpit w Grafanie, który pokazuje kondycję całej sieci na jednym ekranie.
    
- [ ] **ODBLOKOWANE:** Bezpieczeństwo Enterprise. Pełna obsługa ról (RBAC) i ochrona endpointów API.
    

#### Milestone 3: "Żyjąca Platforma" (SOTP 2.0)

_**Motto:** "Platforma sama się wdraża i sama siebie diagnozuje."_

To jest skok mentalny. Nasza platforma staje się w pełni "Cloud-Native". Staje się świadoma samej siebie i w pełni zautomatyzowana.

- [ ] **ODBLOKOWANE:** Wdrożenia "Zero Dotyku" (GitOps). `git push` do repozytorium **automatycznie wdraża nową wersję** na produkcji.
    
- [ ] **ODBLOKOWANE:** "Rentgen Systemu". Możemy prześledzić jedno kliknięcie użytkownika przez cały system – od frontendu, przez API, zadanie Celery, aż po bazę danych (Ślady OTel).
    
- [ ] **ODBLOKOWANE:** "Uniwersalna Wyszukiwarka Logów". Mamy jedno miejsce (Loki), aby przeszukać logi z _każdego_ komponentu naszej platformy.
    
- [ ] **ODBLOKOWANE (DEMO!):** Z poziomu śladu (Tempo) jednym kliknięciem przeskakujemy do powiązanych logów (Loki). Debugowanie staje się banalnie proste.
    

#### Milestone 4: "Interaktywna Analiza" (SOTP 2.5)

_**Motto:** "Przestajemy tylko patrzeć. Zaczynamy działać i rozumieć."_

Platforma staje się interaktywnym partnerem, a nie tylko pasywnym monitorem. Dostarcza odpowiedzi i pozwala na natychmiastową reakcję.

- [ ] **ODBLOKOWANE:** "Zdalna Konsola". Można uruchomić polecenie `show version` na routerze bezpośrednio z naszego UI.
    
- [ ] **ODBLOKOWANE:** "Tłumacz Sysloga". Surowe, techniczne logi z urządzeń są czytelnie prezentowane w interfejsie SOTP.
    
- [ ] **ODBLOKOWANE:** "Raporty dla Zarządu". Można wygenerować i pobrać **raport PDF** pokazujący dostępność sieci w ostatnim miesiącu.
    
- [ ] **ODBLOKOWANE:** "Wielki Brat". Mamy pełny ślad audytowy – wiemy, kto, co i kiedy kliknął w platformie.
    

#### Milestone 5: "Sieć Autonomiczna" (SOTP 3.0 - Edycja Flagowa)

_**Motto:** "Nasza platforma przewiduje przyszłość i sama naprawia błędy."_

To są funkcje, które robią efekt "WOW". Przechodzimy od monitoringu reaktywnego do proaktywnego i autonomicznego.

- [ ] **ODBLOKOWANE (DEMO DNIA!):** "Samonaprawianie". Celowo wyłączamy port w routerze. SOTP wykrywa alert i **automatycznie uruchamia port z powrotem**.
    
- [ ] **ODBLOKOWANE:** "Kryształowa Kula". Platforma pokazuje **prognozę (predykcję AI/ML)** zużycia pasma na najbliższe 24 godziny.
    
- [ ] **ODBLOKOWANE:** "Wehikuł Czasu dla Konfiguracji". Możemy zrobić `git diff` na konfiguracji routera i zobaczyć, co zmieniło się między wczoraj a dziś.
    
- [ ] **ODBLOKOWANE:** "Niewidzialna Tarcza". Cały ruch wewnętrzny między naszymi mikrousługami jest automatycznie szyfrowany (mTLS).
    

#### Milestone X: "Uniwersalna Platforma Telemetryczna" (SOTP-X)

_**Motto:** "Monitorujemy wszystko. Od routera, przez czujnik IoT, po chmurę."_

Udowadniamy, że SOTP to nie "narzędzie sieciowe". To uniwersalny silnik do przetwarzania danych, ograniczony tylko naszą wyobraźnią.

- [ ] **ODBLOKOWANE:** "GPS dla Danych". Widzimy dashboard "Top 10 Rozmówców" w sieci (dzięki NetFlow).
    
- [ ] **ODBLOKOWANE:** "Strażnik Zgodności". Mamy raport pokazujący, które routery **nie spełniają naszej "Złotej Konfiguracji"**.
    
- [ ] **ODBLOKOWANE (DOWÓD!):** Obok wykresu CPU routera widzimy **wykres temperatury z czujnika IoT** (dzięki obsłudze MQTT).
    
- [ ] **ODBLOKOWANE (DOWÓD!):** Obok wykresów sieciowych widzimy **metryki z serwera Linux** (node_exporter) i **bazy danych AWS RDS**.
    
	- [ ] **ODBLOKOWANE:** "Oczy Użytkownika". Wiemy, jak szybko platforma ładuje się w przeglądarce użytkownika (dzięki RUM).