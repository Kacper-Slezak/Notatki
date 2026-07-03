
###  FAZA 1: Rozruch i Baseline (Tydzień 1-2)

**Cel:** Masz działający lab i pierwszy rozdział pracy.

- ** Techniczne (Lab):**
    
    1. Postawić klaster `k3d` + zainstalować `Istio` (profil demo).
        
    2. Wdrożyć `httpbin` i `fortio`.
        
    3. **Realizacja Scenariusza 1 (Referencyjny):**
        
        - Zrobić zrzut ekranu z `openssl`, który pokazuje: "Protocol: TLSv1.3, Cipher: TLS_AES_...".
            
        - Przeprowadzić test wydajności Fortio (bez Keep-Alive).
            
        - Zapisać wyniki do Excela (Zakładka: Baseline).
            
- ** Pisanie (Tekst):**
    
    1. Stwórz plik (Word/LaTeX) i ustaw formatowanie zgodne z wymogami uczelni (marginesy, czcionka).
        
    2. **Napisz Wstęp (Introduction):**
        
        - O czym jest praca? (O problemie wydajność vs bezpieczeństwo).
            
        - Cel pracy: Porównanie TLS 1.3 vs 1.2 w kontekście IoT/Edge.
            
    3. **Zacznij Rozdział "Metodyka Badań":**
        
        - Opisz środowisko: "Do badań wykorzystano klaster k3d w wersji X, Istio w wersji Y...". To pisze się łatwo, bo właśnie to robisz.
            
- **🎓 Formalności:**
    
    - Wyślij maila do promotora: "Środowisko gotowe, mam wyniki referencyjne (Baseline)".
        

---

###  FAZA 2: Główne Badania - "Mięso" (Tydzień 3-4)

**Cel:** Wykonanie eksperymentów (Scenariusz 2 i 3).

- ** Techniczne (Lab):**
    
    1. **Scenariusz 2 (RFC/Eksploracja):**
        
        - Spróbuj wgrać `EnvoyFilter` wymuszający inny szyfr w TLS 1.3.
            
        - Zrób screena błędu lub braku zmiany (to jest wynik badawczy!).
            
    2. **Scenariusz 3 (IoT/Legacy - TLS 1.2):**
        
        - Zrób downgrade klastra do TLS 1.2 (komenda `istioctl install`).
            
        - Wymuś słaby szyfr (np. CBC).
            
        - Przeprowadź testy Fortio.
            
        - Zapisz wyniki do Excela (Zakładka: IoT_Legacy).
            
- ** Pisanie (Tekst):**
    
    1. **Pisz Rozdział Teoretyczny (w międzyczasie):**
        
        - Co to jest Kubernetes? Co to jest Service Mesh?
            
        - Różnica między TLS 1.2 a 1.3 (wklej wiedzę z RFC, o której czytałeś).
            
    2. Dopisuj do "Metodyki" kolejne kroki, które robisz w labie (żeby nie zapomnieć komend).
        

---

###  FAZA 3: Security & Analiza Danych (Tydzień 5-6)

**Cel:** Ostatni eksperyment i obróbka wyników.

- ** Techniczne (Lab):**
    
    1. **Scenariusz 4 (Zero Trust):**
        
        - Wróć do TLS 1.3.
            
        - Wgraj politykę `STRICT` / `AuthorizationPolicy`.
            
        - Zrób testy Fortio (narzut autoryzacji).
            
        - Zapisz wyniki do Excela.
            
- ** Analiza (Wykresy):**
    
    1. W Excelu zrób wykresy słupkowe porównujące Latency i CPU dla wszystkich 3 scenariuszy.
        
    2. Zrób ładne screenshoty z Grafany i Kiali (pokazujące topologię sieci).
        
- ** Pisanie (Tekst):**
    
    1. **Napisz Rozdział "Wyniki Badań":**
        
        - Wklejasz wykresy.
            
        - Opisujesz: _"Jak widać na wykresie 1, TLS 1.2 ma wyższe opóźnienie (latency) z powodu dłuższego handshake'u (2-RTT), ale zużycie CPU spadło o X% dzięki słabszemu szyfrowi."_
            

---

###  FAZA 4: Składanie i Wnioski (Tydzień 7-8)

**Cel:** Masz 90% brudnopisu pracy.

- ** Pisanie (Tekst):**
    
    1. **Napisz "Podsumowanie i Wnioski":**
        
        - Czy hipoteza się potwierdziła? (Tak, TLS 1.3 jest szybszy w sieci, TLS 1.2 lżejszy dla CPU).
            
        - Dla kogo co rekomendujesz? (Banki -> TLS 1.3, Czujniki IoT -> TLS 1.2).
            
    2. Uzupełnij Bibliografię (linki do RFC, dokumentacji Istio, książek).
        
    3. Napisz Streszczenie (Abstract) po polsku i angielsku.
        
- ** Formalności:**
    
    - **Wysyłka do Promotora:** Wyślij całość (lub poszczególne rozdziały) do sprawdzenia. "Panie Doktorze, przesyłam draft pracy do weryfikacji".
        

---

###  FAZA 5: Poprawki i Obrona (Tydzień 9-10)

**Cel:** "Pudrowanie" i oddanie.

- ** Pisanie (Tekst):**
    
    1. Wprowadź poprawki od promotora (zazwyczaj czepiają się opisów rysunków albo literówek).
        
    2. Formatowanie ostateczne (spis treści, numery stron).
        
- **🎓 Formalności:**
    
    1. Wgranie pracy do systemu antyplagiatowego (JSA).
        
    2. Złożenie pracy w dziekanacie.
        
    3. **Przygotowanie prezentacji:** 5-10 slajdów na obronę (Cel, Co zrobiłem, Najważniejszy Wykres, Wnioski).
        

---

### Struktura Twojej Pracy (Spis Treści)

Żebyś wiedział, co masz napisać, oto gotowy szkielet:

1. Wstęp

1.1. Wprowadzenie do tematyki mikroserwisów

1.2. Cel i zakres pracy

1.3. Uzasadnienie wyboru tematu (Bezpieczeństwo vs Wydajność)

2. Część Teoretyczna

2.1. Architektura Cloud-Native i Kubernetes

2.2. Koncepcja Service Mesh i narzędzie Istio

2.3. Protokoły kryptograficzne (TLS 1.2 vs 1.3 - analiza RFC 8446)

2.4. Modele bezpieczeństwa (Zero Trust)

3. Środowisko Badawcze i Metodyka (To opisujesz teraz!)

3.1. Architektura laboratorium (k3d, Docker)

3.2. Wykorzystane narzędzia (Fortio, Grafana, Kiali)

3.3. Zdefiniowane scenariusze testowe (Opisujesz te 3 scenariusze, które ustaliliśmy)

4. Analiza Wydajności i Bezpieczeństwa (Twoje wyniki)

4.1. Wyniki dla scenariusza referencyjnego (TLS 1.3)

4.2. Wyniki dla scenariusza IoT (TLS 1.2 - Downgrade)

4.3. Analiza narzutu polityk autoryzacji (Zero Trust)

4.4. Dyskusja wyników (Porównanie wykresów)

**5. Podsumowanie i Wnioski**

**Literatura**