**Tytuł:** _"Adaptacyjna konfiguracja warstwy service mesh na potrzeby środowisk obliczeniowych o różnej wydajności"_

####  Scenariusz 1: Referencyjny (Baseline TLS 1.3)

- **Konfiguracja:** Domyślne Istio (TLS 1.3).
    
- **Badanie:**
    
    1. Mierzysz wydajność (Fortio).
        
    2. Sprawdzasz, który z 5 dostępnych szyfrów wybrał się sam. (To będzie Twój punkt odniesienia).
        

####  Scenariusz 2: Eksploracja TLS 1.3 (RFC Investigation)

- **Cel:** Sprawdzić, czy da się zmusić TLS 1.3 do wybrania innego szyfru z tej piątki (np. ChaCha20 zamiast AES).
    
- **Badanie:** Próbujesz to zmienić przez `EnvoyFilter`. Jeśli się uda -> mierzysz. Jeśli się nie uda (bo procesor wymusza AES) -> opisujesz to jako wniosek z analizy RFC (promotor napisał: _"Potem idziemy w RFC i czytamy na jakiej podstawie on dokonuje tego wyboru"_).
    

####  Scenariusz 3: IoT / Edge (TLS 1.2 + Słaby Szyfr)

- **Konfiguracja:** Wymuszasz globalnie TLS 1.2.
    
- **Badanie:** Wymuszasz konkretny, słabszy szyfr (np. CBC lub bez GCM).
    
- **Cel:** Wykazać spadek zużycia CPU (dla urządzeń IoT) kosztem bezpieczeństwa.
    

####  Scenariusz 4: Security (Strict Policies)

- **Konfiguracja:** Polityka `STRICT` (blokada wszystkiego, pozwolenie tylko na konkretną ścieżkę).
    
- **Cel:** Zmierzenie narzutu sprawdzania reguł dostępu.
    