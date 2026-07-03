---
typ: projekt
status: planowanie
priorytet: "5"
data_rozpoczecia: 2026-07-03
technologia:
  - Automation
  - Kubernetes 
  - Istio
  - K6
---
# Macierz Scenariuszy Testowych (Narzędzie K6)

> [!abstract] Cel Metodyczny
> Izolacja poszczególnych zmiennych sieciowych (rozmiar ładunku, współbieżność, narzut negocjacji kluczy), aby precyzyjnie zmierzyć ich indywidualny wpływ na zużycie procesora (CPU) i pamięci (RAM) przez proxy Envoy w architekturze Istio.

##  Zmienne Badawcze

Do testów zdefiniowano 3 główne, kontrolowane zmienne. W każdym ze scenariuszy zmieniany jest **tylko jeden** parametr naraz (zasada *ceteris paribus*).

1. **Zarządzanie połączeniem:** - `Keep-Alive` (utrzymywane) vs `No Keep-Alive` (ciągle zrywane, wymusza nowy Handshake TLS co zapytanie).
2. **Payload (Ładunek danych):** - `Mały` (~100 Bajtów) vs `Duży` (~50 KB).
3. **Współbieżność (VUs - Virtual Users):** - `Niska` (10 równoległych użytkowników) vs `Wysoka` (100 równoległych użytkowników).

---

##  Tabela Zbiorcza Scenariuszy

| ID | Grupa Badawcza | Nazwa Testu | Połączenie | Payload | VUs | Mierzony Aspekt (Zasób) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **1** | Narzut Symetryczny | Baza IoT | Keep-Alive | 100 B | 10 | Punkt odniesienia (Baseline). |
| **2** | Narzut Symetryczny | Skala IoT | Keep-Alive | 100 B | 100 | Koszt samej obsługi wielu wątków. |
| **3** | Narzut Rozmiaru | Pobieranie pliku | Keep-Alive | 50 KB | 10 | Koszt szyfrowania (AES/ChaCha) dużych danych. |
| **4** | Narzut Rozmiaru | Stres Przepustowości | Keep-Alive | 50 KB | 100 | Saturacja proxy (łącze i szyfrowanie masowe). |
| **5** | Narzut Asymetryczny | Handshake Baza | **No Keep-Alive** | 100 B | 10 | Czysty koszt TLS Handshake (operacje asymetryczne). |
| **6** | Narzut Asymetryczny | **Post-Quantum Stress** | **No Keep-Alive** | 100 B | 100 | Burza połączeń (wymiana ciężkich kluczy PQC). |

---

##  Szczegółowy Opis Grup Badawczych

### Grupa 1: Izolacja Narzutu Symetrycznego (Czysty ruch)
W tej grupie połączenia są zestawiane raz i utrzymywane (`Keep-Alive`). Badamy, jak utrzymanie szyfrowanego tunelu obciąża procesor w zależności od liczby wątków.

- **Test 1 (Baza IoT):** Absolutne minimum klastra. Referencja dla wszystkich innych testów, symulująca rzadkie i lekkie pakiety telemetryczne.
- **Test 2 (Skala IoT):** Zmieniamy *tylko* liczbę użytkowników względem Testu 1. Pozwala to wyizolować wartość zużycia CPU wynikającą z konieczności utrzymywania w pamięci proxy 100 aktywnych, bezpiecznych sesji jednocześnie.

### Grupa 2: Izolacja Narzutu Rozmiaru Danych (Bulk Transfer)
Połączenia są utrzymywane, ale drastycznie zwiększamy rozmiar pakietów. Skupiamy się na przepustowości algorytmów symetrycznych.

- **Test 3 (Pobieranie pliku):** Różnica w CPU między Testem 1 a Testem 3 pokaże nam dokładnie, ile procesora kosztuje zaszyfrowanie i przepchnięcie dodatkowych 50 KB danych. Zmierzy to również wielkość buforów w pamięci RAM.
- **Test 4 (Stres Przepustowości):** Ekstremalne obciążenie algorytmu symetrycznego. Sprawdzamy punkt dławienia się proxy (tzw. bottleneck), gdy serwer musi zaszyfrować ogromne porcje danych dla wielu użytkowników naraz.

### Grupa 3: Izolacja Narzutu Asymetrycznego (Handshake & PQC)
> [!warning] Kluczowy etap dla badań Post-Quantum Cryptography (PQC)
> Wprowadzamy zrywanie połączeń (`No Keep-Alive`). Zmusza to Envoy'a do wykonywania ciężkich operacji matematycznych (wymiana certyfikatów, weryfikacja tożsamości) dla **każdego** zapytania.

- **Test 5 (Handshake Baza):** Odejmując wyniki Testu 1 od Testu 5, uzyskujemy czystą, matematycznie wyizolowaną wartość CPU dla samej operacji *TLS Handshake*. To najważniejsza statystyka pozwalająca porównać klasyczne krzywe eliptyczne z algorytmami postkwantowymi (KEM).
- **Test 6 (Post-Quantum Stress):** Symulacja najcięższego scenariusza awaryjnego (Connection Storm). Bada zachowanie procesora, gdy z powodu restartu systemu 100 urządzeń na raz próbuje wynegocjować od zera gigantyczne klucze i podpisy postkwantowe.

---

> [!success] Uzasadnienie Inżynierskie
> Zastosowanie struktury macierzowej (*ceteris paribus*) całkowicie eliminuje problem nakładania się na siebie narzutów z różnych warstw (np. mylenie narzutu autoryzacji z narzutem przesyłu dużych plików). Każdy wzrost użycia procesora można bezpośrednio przypisać do konkretnego mechanizmu kryptograficznego.