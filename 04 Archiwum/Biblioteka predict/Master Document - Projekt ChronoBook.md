---
typ: projekt
status: zamrożony
technologia:
  - Python
  - ML
  - Prophet
priorytet: "2"
data_aktualizacji: 2025-12-20
---

#  Master Document - Projekt ChronoBook
## 1. Wprowadzenie i Cele Projektu

### 1.1. Nazwa Projektu

Projekt: **ChronoBook**

### 1.2. Wizja Projektu

Stworzenie w pełni funkcjonalnej aplikacji webowej ("ChronoBook") do śledzenia postępów w czytaniu książek i predykcji czasu ukończenia listy "Do Przeczytania" (TBR).

### 1.3. Cele Główne

- **Cel Technologiczny (Nadrzędny):** Aplikacja jest pretekstem do zaprojektowania, zbudowania i utrzymania nowoczesnej, skalowalnej i obserwowalnej platformy aplikacyjnej. Projekt służy jako **zaawansowany sandbox** do nauki i demonstracji umiejętności z zakresu **DevOps, Platform Engineering i SRE**.
    
- **Cel Biznesowy (Funkcjonalny):** Dostarczenie użytkownikowi wiarygodnej estymacji daty ukończenia listy TBR w oparciu o jego historyczne i kontekstowe tempo czytania.
    

### 1.4. Role Główne

- **Właściciel Projektu / Główny Deweloper:**  - Odpowiedzialny za wszystkie aspekty projektowania, implementacji, wdrożenia i utrzymania.
    
- **Użytkownik Końcowy:**  - Odbiorca funkcjonalności aplikacji.
    

### 1.5. Zakres Projektu (In/Out)

**W Zakresie (In Scope):**

- Pełna konteneryzacja aplikacji (Docker).
    
- Lokalna orkiestracja na K3d.
    
- Wdrożenia w pełni oparte o model GitOps (ArgoCD).
    
- Pełen stos obserwowalności (Prometheus, Loki, Tempo, Grafana).
    
- Implementacja Service Mesh (Istio) dla bezpieczeństwa (mTLS) i kontroli ruchu (canary).
    
- Pełen pipeline CI/CD (GitHub Actions).
    
- Prosty model predykcyjny ML (regresja) jako mikroserwis.
    

**Poza Zakresem (Out of Scope):**

- Wdrożenie na produkcyjnej, płatnej chmurze (AWS, GCP, Azure).
    
- Zaawansowane funkcje społecznościowe (np. listy znajomych, polecanie).
    
- Obsługa wielu języków (i18n) - projekt skupia się na wersji polskiej.
    
- Systemy płatności lub monetyzacja.
    

### 1.6. Założenia i Ograniczenia

- **Ograniczenie:** Projekt jest realizowany w 100% na lokalnej maszynie deweloperskiej.
    
- **Ograniczenie:** Wszystkie użyte narzędzia muszą być darmowe i Open Source.
    
- **Założenie:** Zewnętrzne API (Google Books API) jest dostępne i wystarczające do pobierania metadanych.
    
- **Założenie:** Deweloper posiada wystarczające zasoby sprzętowe (RAM, CPU) do uruchomienia lokalnego klastra K3d z pełnym stosem.
    

---

## 2. Architektura i Stos Technologiczny

Stos technologiczny pozostaje zgodny z poprzednią analizą. Najważniejsze elementy to **K3d, ArgoCD, Istio, Stos LGTM (Loki, Grafana, Tempo, Mimir/Prometheus), FastAPI i Next.js**.

### 2.1. Diagram Architektury Systemu (Poziom Kontenerów C4)

Poniższy diagram przedstawia architekturę docelową działającą wewnątrz klastra K3d.

Plaintext

```
+-----------------------------------------------------------------------------------+
| Użytkownik (Przeglądarka Web)                                                     |
+--------------------------+--------------------------------------------------------+
                           | HTTPS (port 443)
+--------------------------v--------------------------------------------------------+
| Klaster K3d (Lokalna Maszyna)                                                     |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | Namespace: istio-system                                                     |  |
|  | +-----------------------+   +---------------------------------------------+ |  |
|  | | Istio Ingress Gateway |-->| Istio Control Plane (Istiod)                | |  |
|  | +-----------------------+   +---------------------------------------------+ |  |
|  +-----------------------------------------------------------------------------+  |
|                           | (Ruch kierowany przez VirtualService)                 |
	|  +--------------------------v---------------------------------------------------+  |
|  | Namespace: chronobook-app                                                   |  |
|  |                                                                             |  |
|  |  +--------------------------+     +-----------------------+                 |  |
|  |  | Pod: Frontend (Next.js)  |---->| Pod: Backend (FastAPI)|                 |  |
|  |  | [App + Istio-Proxy]      |     | [App + Istio-Proxy]   |                 |  |
|  |  +--------------------------+     +----------+------------+                 |  |
|  |                                              | (TCP)                        |  |
|  |                                  +-----------v-----------+                  |  |
|  |                                  | Pod: Baza Danych      |                  |  |
|  |                                  | (PostgreSQL)          |                  |  |
|  |                                  +-----------------------+                  |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | Namespace: monitoring                                                       |  |
|  | +------------------+ +-----------------+ +----------------+ +-------------+ |  |
|  | | Grafana          | | Prometheus      | | Loki           | | Tempo       | |  |
|  | +------------------+ +-----------------+ +----------------+ +-------------+ |  |
|  | (Zbiera dane z istio-system i chronobook-app)                               |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | Namespace: argocd                                                           |  |
|  | +------------------+                                                        |  |
|  | | ArgoCD Server    | (Obserwuje repo Git i wdraża do chronobook-app)         |  |
|  | +------------------+                                                        |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### 2.2. Model Danych (ERD)

Prosty schemat tabel w bazie PostgreSQL.

Plaintext

```
Tabela: Users
----------------
user_id (PK, UUID)
email (VARCHAR, UNIQUE)
hashed_password (VARCHAR)
created_at (TIMESTAMP)

Tabela: Books
----------------
book_id (PK, UUID)
google_book_id (VARCHAR, UNIQUE)
title (VARCHAR)
author (VARCHAR)
page_count (INTEGER)

Tabela: User_TBR_List
----------------
tbr_id (PK, UUID)
user_id (FK -> Users.user_id)
book_id (FK -> Books.book_id)
status (ENUM: 'TBR', 'Reading', 'Finished')
added_at (TIMESTAMP)

Tabela: Reading_Sessions
----------------
session_id (PK, UUID)
tbr_id (FK -> User_TBR_List.tbr_id)
user_id (FK -> Users.user_id)
start_time (TIMESTAMP)
end_time (TIMESTAMP)
pages_read (INTEGER)  -- Opcjonalne, dla 'Trybu Dokładnego'

Tabela: Reading_Log (Tryb Prosty)
----------------
log_id (PK, UUID)
tbr_id (FK -> User_TBR_List.tbr_id)
user_id (FK -> Users.user_id)
start_date (DATE)
end_date (DATE)
```

### 2.3. Diagram Przepływu Wdrożenia (CI/CD GitOps)

Diagram sekwencji opisujący proces od `git push` do wdrożenia.

Plaintext

```
    Deweloper        Repozytorium Aplikacji      GitHub Actions       Repozytorium Konfiguracji        ArgoCD             Klaster K3d
        |                   (main)                    |                     (main)                      |                     |
        |---(1) git push--->|                         |                         |                         |                     |
        |                   |---(2) Trigger----------->|                         |                         |                     |
        |                   |                         |---(3) Test & Build------|                         |                     |
        |                   |                         |---(4) Push Image (ghcr.io)|                         |                     |
        |                   |                         |---(5) Git Push (nowy tag)->|                         |                     |
        |                   |                         |                         |---(6) Trigger (Webhook)--->|                     |
        |                   |                         |                         |                         |---(7) Pull Changes--|
        |                   |                         |                         |                         |---(8) Sync----------|
        |                   |                         |                         |                         |                     |---(9) Aktualizacja Pod
        |                   |                         |                         |                         |                     |    (Nowa Wersja)
```

---

## 3. Szczegółowy Plan Rozwoju (Podział na Fazy)

Każda faza definiuje wyraźne cele i kryteria akceptacji.

#### Faza 0: Fundamenty (Lokalne Środowisko)

- **Cel:** Przygotowanie absolutnych podstaw środowiska deweloperskiego.
    
- **Zadania:**
    
    1. Instalacja wymaganego oprogramowania: Docker Desktop, `kubectl`, `helm`, `k3d`.
        
    2. Utworzenie klastra K3d: `k3d cluster create chronobook --port 8080:80@loadbalancer`.
        
    3. Utworzenie dwóch repozytoriów na GitHub: `chronobook-app` i `chronobook-k8s-config`.
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 0.1) Polecenie `kubectl get nodes` zwraca jeden węzeł w stanie `Ready`.
        
    - (AC 0.2) Oba repozytoria istnieją i są sklonowane lokalnie.
        

#### Faza 1: Monolit (Aplikacyjne MVP)

- **Cel:** Stworzenie działającej aplikacji (Frontend + Backend + Baza) uruchamianej za pomocą `docker-compose`, bez Kubernetesa.
    
- **Wymagania Funkcjonalne:** FR1, FR2, FR3, FR4 (tryb prosty: oznaczanie daty start/koniec).
    
- **Zadania:**
    
    1. Stworzenie projektu FastAPI (backend) z endpointami do logowania, dodawania książek i oznaczania jako przeczytane.
        
    2. Stworzenie projektu Next.js (frontend) z formularzami i listą.
        
    3. Stworzenie pliku `docker-compose.yml`, który uruchamia `frontend`, `backend` i `postgres`.
        
    4. Implementacja integracji z Google Books API.
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 1.1) Polecenie `docker-compose up -d` pomyślnie uruchamia wszystkie 3 serwisy.
        
    - (AC 1.2) Otworzenie `http://localhost:3000` w przeglądarce pokazuje UI aplikacji.
        
    - (AC 1.3) Użytkownik może pomyślnie ukończyć pełen cykl: Rejestracja -> Zalogowanie -> Wyszukanie książki -> Dodanie do TBR -> Oznaczenie jako "Skończona" (z datami).
        
    - (AC 1.4) Dane są trwale zapisane w wolumenie Postgres (przetrwają restart kontenera).
        

### Faza 2: Konteneryzacja i Pierwsze Wdrożenie (K8s)

- **Cel:** Migracja aplikacji z `docker-compose` do działania na klastrze K3d. Wdrożenie jest na tym etapie _ręczne_.
    
- **Wymagania Funkcjonalne:** FR5, FR6 (prosta predykcja: (Total_Stron_TBR / Średnia_Stron_Na_Dzień)).
    
- **Zadania:**
    
    1. Napisanie `Dockerfile` dla `frontend` i `backend`.
        
    2. Napisanie manifestów YAML dla K8s: `Deployment`, `Service`, `ConfigMap`, `Secret`.
        
    3. Napisanie manifestu `Ingress` (korzystając z domyślnego Traefika w K3d).
        
    4. Instalacja PostgreSQL na klastrze (za pomocą `StatefulSet` lub prostego Helm charta).
        
    5. Zaimplementowanie prostej logiki predykcji w backendzie.
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 2.1) `docker-compose` nie jest już używany.
        
    - (AC 2.2) Polecenie `kubectl apply -f .` (na plikach manifestów) pomyślnie wdraża aplikację.
        
    - (AC 2.3) Aplikacja jest dostępna z zewnątrz klastra (np. `http://chronobook.localhost` po skonfigurowaniu `/etc/hosts`).
        
    - (AC 2.4) Wszystkie funkcjonalności z Fazy 1 działają na K8s.
        
    - (AC 2.5) Na dashboardzie wyświetla się prosta data ukończenia TBR (FR6).
        

### Faza 3: Automatyzacja (GitOps & CI)

- **Cel:** Zautomatyzowanie procesu wdrożenia (CI/CD) przy użyciu podejścia GitOps.
    
- **Wymagania Niefunkcjonalne:** NFR2, NFR3.
    
- **Zadania:**
    
    1. Przeniesienie wszystkich manifestów YAML z Fazy 2 do repozytorium `chronobook-k8s-config`.
        
    2. Instalacja **ArgoCD** na klastrze K3d (za pomocą Helma).
        
    3. Skonfigurowanie ArgoCD, aby obserwowało repo `chronobook-k8s-config`.
        
    4. Konfiguracja **GitHub Actions** w repo `chronobook-app` (budowanie, testowanie, push do `ghcr.io`).
        
    5. Konfiguracja ostatniego kroku w GitHub Actions, który automatycznie aktualizuje tag obrazu w repo `chronobook-k8s-config` (np. przez `kustomize` lub `sed`).
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 3.1) Ręczne użycie `kubectl apply` jest _zakazane_ dla aplikacji.
        
    - (AC 3.2) UI ArgoCD jest dostępne i pokazuje aplikację `chronobook` jako `Synced` i `Healthy`.
        
    - (AC 3.3) `git push` do gałęzi `main` repozytorium `chronobook-app` wyzwala pipeline CI.
        
    - (AC 3.4) Po zakończeniu pipeline'u, ArgoCD automatycznie wykrywa zmianę i wdraża nowy obraz na K3d bez ręcznej interwencji.
        

### Faza 4: Obserwowalność (SRE - Trzy Filary)

- **Cel:** Zbudowanie pełnego stosu obserwowalności (Metrics, Logs, Traces).
    
- **Wymagania Niefunkcjonalne:** NFR1.
    
- **Zadania:**
    
    1. Instalacja stosu **LGTM** (Loki, Grafana, Tempo) oraz **Prometheus** (za pomocą Helm, np. przez `kube-prometheus-stack`).
        
    2. Integracja FastAPI z `starlette-prometheus` (Metrics).
        
    3. Integracja FastAPI i Next.js z **OpenTelemetry** (Traces).
        
    4. Konfiguracja Promtail (dla Loki) do zbierania logów ze wszystkich podów.
        
    5. Zbudowanie w Grafanie dashboardu "SRE Golden Signals" (Latencja, Ruch, Błędy).
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 4.1) UI Grafany jest dostępne.
        
    - (AC 4.2) W Grafanie (w trybie "Explore") mogę pomyślnie odpytać Prometheusa i zobaczyć metryki (np. `http_requests_total`).
        
    - (AC 4.3) Mogę odpytać Loki i zobaczyć logi z kontenera `backend-api`.
        
    - (AC 4.4) Mogę odpytać Tempo (po `traceID`) i zobaczyć pełen ślad żądania.
        
    - (AC 4.5) Dashboard "Golden Signals" poprawnie wyświetla dane na żywo.
        

### Faza 5: Service Mesh (Istio)

- **Cel:** Wdrożenie Istio w celu nauki bezpieczeństwa (mTLS) i zaawansowanej kontroli ruchu.
    
- **Wymagania Niefunkcjonalne:** NFR4, NFR5, NFR6.
    
- **Zadania:**
    
    1. Instalacja **Istio** na klastrze K3d (za pomocą `istioctl` lub Helma).
        
    2. Instalacja dodatków Istio (Kiali, Jaeger/Tempo, Prometheus).
        
    3. Włączenie automatycznego wstrzykiwania "sidecar" (`istio-proxy`) do namespace `chronobook-app`.
        
    4. Konfiguracja `Istio Ingress Gateway` (zastąpienie Traefika).
        
    5. Zastosowanie polityki `PeerAuthentication` w trybie `STRICT` (mTLS).
        
    6. Zdefiniowanie `VirtualService` i `DestinationRule` do testów canary.
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 5.1) Pody aplikacji (`frontend`, `backend`) pokazują status `2/2 Containers` w `kubectl get pods`.
        
    - (AC 5.2) UI **Kiali** jest dostępne i poprawnie rysuje graf połączeń między serwisami.
        
    - (AC 5.3) Kiali pokazuje "kłódki" na połączeniach, potwierdzając działanie mTLS (NFR4).
        
    - (AC 5.4) Stworzenie drugiej wersji backendu (v2) i skonfigurowanie `VirtualService` do wysyłania 10% ruchu do v2 (NFR6) działa poprawnie.
        

### Faza 6: Inteligentny Model ML

- **Cel:** Ulepszenie funkcjonalności aplikacji o "mądrzejszy" model predykcyjny.
    
- **Wymagania Funkcjonalne:** FR7, FR8 (tryb dokładny), FR9 (kontekstowy).
    
- **Zadania:**
    
    1. Dodanie w UI "Trybu Dokładnego" (FR7) - logowanie sesji (timer lub wpis ręczny).
        
    2. Modyfikacja backendu, aby obliczał predykcję w oparciu o "Prędkość" (Strony/Godzinę) i "Nawyk" (Godziny/Tydzień) (FR8).
        
    3. (Opcjonalnie) Rozpoczęcie prac nad FR9: Analiza danych historycznych (`Reading_Sessions`) pod kątem wzorców (np. weekend vs dni robocze) i uwzględnienie ich w predykcji.
        
- **Kryteria Akceptacji (AC):**
    
    - (AC 6.1) Użytkownik może włączyć timer, który śledzi sesję czytania.
        
    - (AC 6.2) Po zakończeniu sesji, dane (`start_time`, `end_time`) są zapisywane w `Reading_Sessions`.
        
    - (AC 6.3) Jeśli użytkownik ma co najmniej jedną sesję, predykcja (FR8) automatycznie przełącza się na model "mądrzejszy", co skutkuje inną (dokładniejszą) datą ukończenia.
        
    - (AC 6.4 - dla FR9) Predykcja obliczona w poniedziałek dla "następnego tygodnia" różni się od tej obliczonej w piątek.
        

---

## 4. Potencjalne Wyzwania i Ryzyka

1. **Zasoby Sprzętowe:** Uruchomienie K3d + ArgoCD + Stos LGTM + Istio + Aplikacja na jednej maszynie jest **bardzo zasobożerne** (szczególnie RAM). Może być konieczne selektywne uruchamianie komponentów.
    
2. **Złożoność Istio:** Istio jest uznawane za jeden z najbardziej złożonych elementów ekosystemu CNCF. Debugowanie problemów z siecią i sidecarami będzie wyzwaniem.
    
3. **Konfiguracja CI/CD:** Poprawne skonfigurowanie GitHub Actions do automatycznej aktualizacji repozytorium konfiguracyjnego (z zachowaniem bezpieczeństwa i dobrych praktyk) jest nietrywialne.
    
4. **Zarządzanie Stanem:** Trwałość danych PostgreSQL w lokalnym klastrze K3d. Awaria klastra lub `k3d cluster delete` może spowodować utratę danych, jeśli wolumeny nie są poprawnie zarządzane.