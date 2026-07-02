# Werdykt rekrutera

Twój profil jest naprawdę silny jak na studenta 3. roku — znacznie powyżej typowego stażysty, który wpisuje Dockera w CV, nie mając z nim poważnego kontaktu. Repozytorium pracy licencjackiej na temat Istio mTLS to zdecydowanie najbardziej imponujący element: pokazuje Kubernetes, service mesh, myślenie o bezpieczeństwie i metodologię benchmarkingu w jednym repozytorium. Projekt SOTP jest poważny pod względem architektury. Marka IBM działa zgodnie z oczekiwaniami. Luka polega na tym, że nic z tego nie jest jeszcze czytelne na pierwszy rzut oka — Twoje CV nadal wygląda jak profil developera backendu w Pythonie, a nie kandydata na stanowisko Cloud/DevOps/Security, przez co rekruter robiący 15-sekundowy skan pominie całkowicie Twoją pracę nad K8s i Istio. Popraw framing (ujęcie), a wskoczysz z poziomu "ciekawe" na "natychmiastowe zaproszenie na rozmowę".

### Wyniki profilu — jak widzi Cię senioralny rekruter

- **Głębokość konteneryzacji i Dockera:** 8/10
    
- **Kubernetes (poziom CKA):** 6/10
    
- **Postawa bezpieczeństwa (CKS/AppSec):** 5/10
    
- **CI/CD & GitOps:** 7/10
    
- **Podstawy AWS / Chmury:** 3/10
    
- **Observability (metryki/tracing/logi):** 7/10
    
- **IaC (Terraform / Helm / CDK):** 2/10
    
- **Czytelność CV / GitHub:** 5/10
    

## Część 1 — Mocne strony

- **Praca dyplomowa = główny wyróżnik:** Repozytorium z benchmarkingiem mTLS/Istio to metodologia niemal doktorancka jak na studenta studiów licencjackich. Wymuszone obniżenie wersji TLS przez EnvoyFilter, testy obciążeniowe K6, różnice w zużyciu CPU — to jest to, co robią starsi inżynierowie SRE. Prawie żaden junior nie ma takiego doświadczenia.
    
- **Architektura SOTP jest prawdziwa:** Dwie bazy danych (PostgreSQL + TimescaleDB), asynchroniczne workerzy Celery, sekrety w HashiCorp Vault, RBAC, scraping Prometheus — to projekt o standardzie produkcyjnym. 316 commitów i 31 śledzonych issue sygnalizuje prawdziwą dyscyplinę inżynierską.
    
- **Instynkt DevSecOps już widoczny:** Pre-commit hooki, Bandit + Safety w CI, JWT + RBAC od pierwszego dnia, sekrety w Vault, a nie w plikach env — zinternalizowałeś podejście "bezpieczeństwo przede wszystkim", zanim większość juniorów w ogóle poznała ten termin.
    
- **Marka IBM otwiera drzwi:** Niezależnie od głębokości wiedzy, "SRE Intern @ IBM" przejdzie przez filtry ATS i sprawi, że rekruter otworzy CV. To kupuje Ci 15 sekund potrzebnych na zaprezentowanie realnej zawartości.
    
- **Ścieżka CKS wyprzedza oczekiwania:** Nauka do CKS (nie tylko CKA) jako student sygnalizuje ambicję i prawdziwe zainteresowanie bezpieczeństwem. Prawie żaden junior DevOps nie ma ani nie jest w trakcie zdobywania CKS.
    
- **Jakość pliku README na GitHubie jest doskonała:** Twój README profilowy z tabelą stosu technologicznego, przypiętymi repozytoriami i aktywną narracją projektu jest lepszy niż u 90% pracujących inżynierów. Architektura w ASCII art w SOTP to miły akcent.
    

## Część 1 — Słabe strony i sygnały ostrzegawcze (red flags)

- **Krytyczny brak IaC:** Brak Terraform, brak Pulumi, brak AWS CDK — ani jednej linii kodu na GitHubie. Każda oferta pracy na Cloud/DevOps w 2025+ wymienia IaC jako wymaganie. To Twoja największa techniczna "ślepa plama" w rolach AWS.
    
- **Krytyczny brak dowodu pracy w AWS:** Certyfikat AWS Architect w trakcie nauki jest dobry, ale nie masz żadnego projektu wdrożonego w realnym AWS. Rekruterzy zapytają: "czy pracowałeś z EKS, ECS, Lambda lub IAM w praktyce?", a szczera odpowiedź brzmi obecnie "nie".
    
- **Luka: staż w IBM wydaje się pusty:** Sam to przyznałeś. W CV wygląda to w porządku, ale bystry rekruter dopyta: "co tam wdrożyłeś?". Jeśli szczera odpowiedź będzie niejasna, to jest to obciążenie. Musisz mieć silną, przygotowaną odpowiedź na to pytanie.
    
- **Luka: głębokość K8s vs szerokość:** Masz ekspercką wiedzę o Istio i bezpieczeństwie service mesh, ale Twoje CV i README wspominają o CKA/CKS jako "w trakcie". Rozbieżność między konfiguracją Envoy na poziomie pracy dyplomowej a "podstawowymi wdrożeniami" w CV jest myląca.
    
- **Luka: kryzys tożsamości w CV:** Twoje CV wymienia Pythona, Flask, FastAPI, Java, OCR — czyta się to jak backend developer z projektami pobocznymi DevOps. Nagłówek musi brzmieć "Cloud/DevOps", a nie być wywnioskowany z punktów dotyczących projektów.
    
- **Luka: brak GitOps lub ArgoCD w praktyce:** Plan rozwoju SOTP zakłada ArgoCD, ale jeszcze się tam nie pojawiło. GitOps jest domyślnym modelem dostarczania oprogramowania w firmach cloud-native. Bez tego Twoje twierdzenie "gotowy na Kubernetes" nie ma potwierdzenia.
    
- **Luka: praca dyplomowa nie ma angielskiego README:** Praca dyplomowa z mTLS jest napisana w całości po polsku. Każdy rekruter lub starszy inżynier spoza Polski natychmiast wyjdzie z repozytorium. To ukrywa Twój najlepszy projekt przed globalnym rynkiem.
    
- **Luka: nadmierne eksponowanie CCNA:** "CCNA w trakcie" w sekcji dodatkowej w CV DevOps/Cloud rozmywa przekaz. Podstawy sieci są ważne, ale wymienianie CCNA obok ścieżki CKS wygląda jak rozszerzanie zakresu na siłę (scope creep). Usuń to albo przenieś do osobnej sekcji "uczę się".
    

## Część 2 — Przepisanie CV: przed → po

|**Obecnie (problem)**|**Zalecana poprawka**|
|---|---|
|Brak sekcji nagłówek/podsumowanie — tożsamość niejasna|Dodaj 2-liniowy nagłówek: "Cloud & DevOps Engineer · SRE Intern @ IBM · Kubernetes|
|Lista umiejętności zaczyna się od Docker — chowa K8s, Istio|Zmień kolejność na Cloud-first: Kubernetes · Istio · Helm / Docker · Docker Compose / AWS (Solutions Architect w trakcie) / IaC: Terraform (dodaj pilnie).|
|SOTP opisane jako "zaprojektowane i wdrożone mikroserwisy" — ogólnikowe|Określ ilościowo i w kontekście chmurowym: "Zbudowano platformę obserwowalności gotową na Kubernetes: asynchroniczne mikroserwisy w Pythonie, workery Celery, TimescaleDB, Prometheus/Grafana, zarządzanie sekretami w Vault, CI/CD GitHub Actions (316 commitów)."|
|Praca dyplomowa całkowicie nieobecna w CV|Dodaj jako projekt: "Praca inżynierska — narzut mTLS w Istio: zbenchmarkowano wydajność TLS 1.2 vs 1.3 w service mesh Kubernetes poprzez wstrzykiwanie konfiguracji EnvoyFilter i testy obciążeniowe K6. Potwierdzono, że TLS 1.3 jest o 5,7% bardziej wydajny procesorowo."|
|IBM wymienione tylko jako "SRE Intern" bez punktów|Dodaj 2–3 punkty, nawet jeśli ogólne: użyte narzędzia, skala środowiska, jakakolwiek praca nad automatyzacją lub monitoringiem — nawet jeśli mała. "Współpraca przy narzędziach do obserwowalności w wielkoskalowym środowisku hybrydowym" brzmi uczciwie i jest dobrze odbierane.|
|"Certyfikat CCNA w trakcie" w Informacjach dodatkowych|Usuń lub zdemotywuj. Trzymaj "CKS — Certified Kubernetes Security Specialist (w trakcie)" wyraźnie w umiejętnościach. CCNA to szum na tym etapie kariery.|

## Część 2 — Priorytety porządkowania GitHuba

1. **Natychmiast przetłumacz README pracy dyplomowej na angielski.** To Twój najbardziej imponujący projekt i jest niewidoczny dla 95% rynku. Nawet maszynowe tłumaczenie z ręczną korektą jest nieskończenie lepsze niż sam polski.
    
2. **Przypnij (pin) 3 repozytoria, odepnij resztę:** SOTP, B.Sc.-Thesis-Istio, entry-system (biometryczne 2FA to świetna historia o bezpieczeństwie). Odepnij Life_Dashboard i SRF — nie wspierają narracji Cloud/Security.
    
3. **Zarchiwizuj lub ukryj tymczasowe repozytoria.** Repozytoria nazwane "Bash" czy "Life_Dashboard" bez opisu obniżają sygnał Twojego profilu. Zarchiwizuj je — pozostaną dostępne, ale nie będą zagracać głównego widoku.
    
4. **Dodaj tematy (GitHub Topics) do SOTP i repozytorium pracy dyplomowej:** kubernetes, istio, observability, devops, security, prometheus, fastapi — sprawiają, że Twoje repozytoria są możliwe do wyszukania i sygnalizują Twoje intencje czytelnikowi.
    
5. **Napraw plik "errors.txt" w głównym folderze SOTP.** Trzymanie surowego logu debugowania w głównym folderze wygląda nieprofesjonalnie. Przenieś go do `docs/` lub usuń. To samo dotyczy `issues.json` w głównym katalogu.
    
6. **Zaktualizuj sekcję "Currently learning" w pliku README swojego profilu.** Nadal jest tam napisane "CKA — going deeper", ale praca dyplomowa udowadnia, że jesteś daleko poza terytorium CKA. Zaktualizuj na CKS + AWS SA + Terraform, aby pokazać swoją prawdziwą trajektorię.
    

## Część 2 — Luki technologiczne do zamknięcia (kolejność priorytetów)

1. **Terraform — pilne.** 2 tygodnie na kursie Terraform na KodeKloud → zbuduj coś prawdziwego (nawet tylko klaster EKS + VPC przez Terraform). Każda oferta pracy Cloud/DevOps tego wymaga. Bez tego będziesz odrzucany z 60% ról, niezależnie od wszystkiego innego.
    
2. **AWS w praktyce.** Załóż konto w darmowej warstwie (free tier). Wdróż SOTP na EKS (nawet jednowęzłowy k3s na EC2 się liczy). Doświadcz ról IAM, grup bezpieczeństwa (security groups), EBS i ALB w praktyce. Certyfikat SA bez praktycznego doświadczenia jest kruchy pod presją rozmowy kwalifikacyjnej.
    
3. **ArgoCD / GitOps.** Twój plan rozwoju SOTP już zakłada ArgoCD. Priorytetyzuj to. Działająca konfiguracja ArgoCD synchronizująca manifesty Kubernetes z repozytorium Git dodaje "GitOps" do Twoich umiejętności w sposób uprawniony, co pojawia się w 70% ofert pracy DevOps.
    
4. **Wykresy Helm.** Napisz wykres (chart) Helm dla SOTP. To naturalny następny krok od Twoich manifestów `k8s/` i prawie zawsze pojawia się w ofertach pracy obok K8s. Pół dnia pracy, duży wzrost sygnału Twoich kompetencji.
    
5. **OpenTelemetry distributed tracing.** Twój SOTP ma już Prometheus + Grafana. Dodanie Tempo + instrumentacji OTel dopełnia "trzy filary" (metryki + logi + ślady) i stawia Cię przed 95% juniorów pod względem głębokości obserwowalności.
    
6. **Falco lub OPA/Kyverno dla bezpieczeństwa runtime.** Biorąc pod uwagę Twoją ścieżkę CKS, dodanie jednego narzędzia bezpieczeństwa runtime z prawdziwym przypadkiem użycia (np. reguły Falco wyłapujące eskalację uprawnień w SOTP) uczyniłoby historię o bezpieczeństwie konkretną i gotową na rozmowę kwalifikacyjną.
    

## Część 3 — Nieoczywiste, zaawansowane projekty

- **Projekt 1 — Platforma EKS multi-tenant sterowana przez GitOps z wymuszaniem bezpieczeństwa w czasie rzeczywistym**
    
    - _Obejmuje:_ AWS EKS · Terraform · ArgoCD · OPA/Kyverno · Falco · IAM IRSA · rozszerzenie SOTP
        
    - Provisionuj klaster EKS z wieloma najemcami (multi-tenant) na AWS przy użyciu Terraform (VPC, grupy węzłów, role IAM IRSA). Wdróż SOTP jako jednego z najemców. Użyj ArgoCD do dostarczania oprogramowania metodą GitOps. Wymuszaj izolację przestrzeni nazw (namespace) i limity zasobów za pomocą polityk przyjęcia (admission policies) Kyverno. Zainstaluj Falco z niestandardowymi regułami, które wyzwalają się przy eskalacji uprawnień lub nieoczekiwanych wywołaniach systemowych od workerów Celery. Wysyłaj wszystkie alerty Falco do własnego pipeline'u alertowania SOTP.
        
    - _Dlaczego to imponuje:_ To nie jest klastrowy tutorial — to produkcyjny model multi-tenant. Napotkasz prawdziwe problemy: łańcuchowanie ról IAM, polityki sieciowe między przestrzeniami nazw, RBAC w ArgoCD i dostrajanie reguł Falco. Fakt, że monitorujesz własną infrastrukturę za pomocą własnego narzędzia, to rekurencyjna historia, która zostaje w pamięci rekrutera. Terraform + EKS + GitOps + bezpieczeństwo runtime w jednym repozytorium = punkt w CV, który pokrywa 4 oddzielne kategorie umiejętności.
        
- **Projekt 2 — Skaner bezpieczeństwa łańcucha dostaw zintegrowany z prawdziwym pipeline'em CI/CD**
    
    - _Obejmuje:_ Domenę CKS supply chain · SBOM · Sigstore/Cosign · Trivy · SLSA Level 2 · atestacje OCI
        
    - Rozszerz istniejący pipeline GitHub Actions projektu SOTP (który już ma Bandit + Safety) do pełnego pipeline'u bezpieczeństwa łańcucha dostaw. Dla każdego budowania obrazu: wygeneruj SBOM za pomocą Syft, podpisz obraz za pomocą Cosign (keyless, Sigstore), dołącz SBOM jako atestację OCI, zeskanuj za pomocą Trivy i przerywaj budowanie przy krytycznych CVE (CRITICAL), a następnie weryfikuj podpisy w webhooku admission Kubernetes (Connaisseur lub polityka weryfikacji obrazu Kyverno), zanim jakikolwiek obraz będzie mógł zostać wdrożony do klastra.
        
    - _Dlaczego to imponuje:_ Bezpieczeństwo łańcucha dostaw (SLSA, SBOM, sigstore) to najgorętszy temat w DevSecOps obecnie i bezpośrednio odnosi się do domeny egzaminacyjnej CKS. To nie jest "dodanie Trivy do CI" z tutoriala — to kompletny łańcuch dowodowy od kodu do działającego poda. Połączenie podpisywania keyless Cosign + weryfikacji admission Kyverno to coś, czego większość pracujących inżynierów nie wdrożyła. Jedno repozytorium, dwie domeny egzaminacyjne CKS i umiejętność, która jest w 30% ofert dla seniorów Cloud/Security w 2025 roku.
        
- **Projekt 3 — Poligon doświadczalny inżynierii chaosu dla odporności Kubernetes z automatycznym alertowaniem o spalaniu budżetu błędów (SLO burn)**
    
    - _Obejmuje:_ AWS · Chaos Mesh / Litmus · Prometheus SLOs · Alerty burn rate budżetu błędów · OpenTelemetry
        
    - Wdróż docelową aplikację na EKS (API SOTP sprawdzi się idealnie). Zdefiniuj SLO w Prometheus (np. 99,5% sukcesu, p95 latencji < 200ms). Uruchom ustrukturyzowane eksperymenty chaosu za pomocą Chaos Mesh: wstrzykiwanie opóźnień sieciowych między usługami, awaria poda podczas okien zbierania SNMP, ograniczanie CPU dla workerów Celery. Dla każdego eksperymentu zautomatyzuj pomiar szybkości spalania budżetu błędów (SLO burn rate) za pomocą reguł alertowania wielookienkowego Prometheusa. Zbuduj dashboard w Grafanie, który pokazuje pozostały budżet błędów obok aktywnych eksperymentów chaosu. Napisz raport po eksperymencie w repozytorium dla każdego scenariusza.
        
    - _Dlaczego to imponuje:_ Inżynieria chaosu jest jednym z najjaśniejszych sygnałów dojrzałości SRE. Połączenie ustrukturyzowanego eksperymentu → pomiaru wpływu na SLO → raportu o budżecie błędów to dokładnie sposób, w jaki działają zespoły SRE w Google/Netflix. Raporty po eksperymentach demonstrują analityczne myślenie, które oddziela prawdziwego SRE od kogoś, kto tylko wdrożył Prometheusa. To także rozszerza Twoją istniejącą pracę nad obserwowalnością SOTP zamiast zaczynania od zera — dodając głębi projektowi, który już masz, co wygląda jak prawdziwa ewolucja inżynierska, a nie sprint portfolio.
        

### Podsumowanie w jednym zdaniu dla pokoju rekrutacyjnego

Jesteś silnym juniorskim kandydatem na stanowisko Cloud/DevOps z ukrytym asem — pracą dyplomową o Istio — której nie ma większość kandydatów na Twoim poziomie. Praca, którą musisz wykonać, to nie więcej projektów. To Terraform w dłoni, jedno realne wdrożenie na AWS, angielski README do pracy dyplomowej i CV, które prowadzi Cloud/K8s zamiast Pythona. Zrób te cztery rzeczy, a staniesz się szczerze konkurencyjny na stanowiska mid-level w firmach cloud-native.