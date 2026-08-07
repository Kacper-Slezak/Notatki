

#### 1. Zachowanie domyślne i optymalizacja w mTLS 1.3

- [ ] **Odkrycie (Auto-tuning):** Mimo że dokumentacja często wskazuje szyfry 256-bitowe jako najsilniejsze/domyślne, mTLS 1.3 w Istio automatycznie negocjuje lżejszy algorytm `TLS_AES_128_GCM_SHA256`. Dowodzi to, że protokół samodzielnie optymalizuje stosunek bezpieczeństwa do wydajności (przepustowości) bez ingerencji administratora.
    
      
    
- [ ] **Problem weryfikacji:** Envoy nie tworzy metryk dla szyfrów (np. `ssl.ciphers`) przy samym starcie poda. Liczniki pojawiają się w pamięci dopiero po przetworzeniu **pierwszego żądania** (zakończony TLS Handshake).
    
      
    

#### 2. Pułapka operacji MERGE i "Downgrade Attack" w mTLS 1.2

- [ ] **Problem (Iluzja wymuszenia):** Nałożenie pliku `EnvoyFilter` z operacją `MERGE` na gniazdo serwera (`DownstreamTlsContext`) i podaniem jednego szyfru (np. ChaCha20) **nie zastępuje** domyślnej listy Istio. Zgodnie z mechaniką protobuf, operacja ta jedynie **dopisuje (append)** nowy szyfr na koniec domyślnej listy.
    
      
    
- [ ] **Wniosek (Ochrona siatki):** Ponieważ klient (`k6`) wciąż używa domyślnych ustawień (gdzie AES-256 jest na szczycie priorytetów), negocjacja TLS (ClientHello) zawsze wybiera najsilniejszy wspólny mianownik (AES-256). Mechanizmy Istio skutecznie bronią się przed celowym osłabieniem kryptografii po stronie samego serwera.
    
      
    

#### 3. Blokada API przez Zero Trust (DestinationRule)

- [ ] **Problem (Strict Decoding Error):** Próba użycia standardowego zasobu Istio, czyli `DestinationRule`, do zdefiniowania parametru `cipherSuites` po stronie klienta kończy się błędem Kubernetes API.
    
      
    
- [ ] **Wniosek:** Dokumentacja Istio pozwala na definiowanie `cipherSuites` głównie dla ruchu brzegowego (Gateways) lub na zewnątrz (`SIMPLE`, `MUTUAL`). Z powodów bezpieczeństwa, tryb wewnętrzny siatki (`ISTIO_MUTUAL` / sidecar-to-sidecar) celowo blokuje tę opcję w standardowym API.
    
      
    

#### 4. Kwestia Certyfikatów (RSA vs ECDSA)

- [ ] **Problem (Cichy fallback):** Wymuszanie szyfrów opartych na kluczach eliptycznych (np. `ECDHE-ECDSA-CHACHA20-POLY1305`) w środowisku, gdzie Istiod domyślnie wystawia podom certyfikaty **RSA**, skutkuje zignorowaniem algorytmu przez Envoya i powrotem do domyślnego szyfru wspierającego RSA. Szyfr musi być kryptograficznie zgodny z typem certyfikatu.
    
      
    

#### 5. Utrata statystyk i metryk

- [ ] **Problem z Prometheusem (Same zera):** Występuje, gdy skrypt analityczny traci połączenie z port-forwardingiem lub gdy występuje konflikt stref czasowych (skrypt pyta w UTC, a logi są w CEST/UTC+2).
    
      
    
- [ ] **Problem z brakiem logów kryptograficznych:** Istio domyślnie wycina ze statystyk Envoya metryki TLS/SSL w celu oszczędzania RAM-u. Aby to badać, należy użyć adnotacji `sidecar.istio.io/statsInclusionRegexps: ".*ssl.*,.*tls.*"` na deploymentach.
    
      