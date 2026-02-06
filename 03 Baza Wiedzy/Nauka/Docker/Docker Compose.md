# Co to ?

- To odpowiednik docker run ustrukturyzowany w  pliku [[.yml]] , służy do startu 
# Najczęściej używane opcje:

- `--detach`, `-d` - **Tryb odłączony**. Uruchamia kontener w tle, nie blokując terminala.
	
- `--entrypoint` - **Nadpisanie punktu wejścia**. Zmienia domyślną komendę uruchamianą, gdy kontener startuje, która została zdefiniowana w obrazie.
	
- `--env`, `-e`, `--env-file` - **Zmienne środowiskowe**. Pozwalają na ustawienie zmiennych środowiskowych wewnątrz kontenera, co jest kluczowe do konfiguracji aplikacji.
	
- `--init` - **System inicjalizacji**. Wprowadza system `init` do kontenera, który zarządza procesami, np. prawidłowo je kończąc po zakończeniu działania.
	
- `--interactive`, `-i`, `--tty`, `-t` - **Tryb interaktywny**. Te opcje są używane razem (`-it`) do stworzenia interaktywnego połączenia z kontenerem, co pozwala na dostęp do jego wnętrza i używanie shell'a.
	
- `--name` - **Nazwa kontenera**. Przypisuje unikalną, łatwą do zapamiętania nazwę do kontenera.
	
- `--network`, `--net` - **Sieć kontenera**. Pozwala na podłączenie kontenera do konkretnej zdefiniowanej sieci Dockera.
	
- `--platform` - **Platforma docelowa**. Określa architekturę, na której kontener ma zostać uruchomiony, na przykład `linux/amd64` lub `linux/arm64`.
	
- `--publish`, `-p` - **Mapowanie portów**. Łączy port na hoście (systemie, w którym uruchamiasz Dockera) z portem w kontenerze, aby umożliwić dostęp z zewnątrz.
	
- `--restart` - **Polityka restartu**. Określa, kiedy i czy kontener powinien być automatycznie restartowany po zatrzymaniu. Dostępne opcje to m.in. `unless-stopped`, `always`, `on-failure` i `no`.
	
- `--rm` - **Automatyczne usuwanie**. Powoduje automatyczne usunięcie kontenera po jego zatrzymaniu, co pomaga w utrzymaniu czystości w systemie.

# 3. Zaawansowane opcje:

- `--cap-add`, `--cap-drop` - Służą do dodawania lub usuwania uprawnień (tzw. capabilities) dla kontenera, co pozwala precyzyjnie kontrolować jego możliwości.
	
- `--cgroup-parent` - Umożliwia umieszczenie kontenera w specyficznej nadrzędnej grupie kontrolnej (cgroup), co ułatwia zarządzanie zasobami.
	
- `--cpu-shares` - Określa względny udział kontenera w zasobach procesora, co jest przydatne przy rywalizacji o CPU.
	
- `--cpuset-cpus` - Przypisuje kontener do konkretnych rdzeni procesora, co pozwala na izolację i optymalizację wydajności.
	
- `--device-cgroup-rule` - Dodaje regułę do białej listy urządzeń dla grupy kontrolnej, co definiuje, do jakich urządzeń kontener ma dostęp.
	
- `--device-read-bps`, `--device-read-iops`, `--device-write-bps`, `--device-write-iops` - Ograniczają szybkość odczytu i zapisu danych (w bajtach lub operacjach na sekundę) dla urządzeń wewnątrz kontenera.
	
- `--gpus` - Udostępnia karty graficzne NVIDIA kontenerowi, co jest niezbędne do uruchamiania aplikacji korzystających z GPU.
	
- `--health-cmd`, `--health-interval`, `--health-retries`, `--health-start-period`, `--health-timeout` - Pozwalają na konfigurację testów sprawdzających stan działania kontenera, aby Docker wiedział, czy jest on zdrowy.
	
- `--memory`, `-m` - Ustawia limit pamięci RAM, którą może zużyć kontener.
	
- `--pid`, `--pids-limit` - Kontrolują liczbę procesów, które mogą być uruchomione w kontenerze.
	
- `--privileged` - Nadaje kontenerowi wszystkie uprawnienia Linuxa, dając mu praktycznie nieograniczony dostęp do hosta.
	
- `--read-only` - Montuje system plików kontenera w trybie tylko do odczytu, co zapobiega modyfikacjom.
	
- `--security-opt` - Służy do ustawiania opcji bezpieczeństwa dla kontenera, takich jak profile SELinux czy AppArmor.
	
- `dockerd --userns-remap` - Włącza remapowanie przestrzeni nazw użytkownika (user namespace) w demonie Dockera, co zwiększa bezpieczeństwo poprzez izolację użytkownika `root` w kontenerze od użytkownika `root` na hoście.

# 4.  Komendy Docker Compose

Docker Compose to narzędzie, które ułatwia definiowanie i uruchamianie aplikacji składających się z wielu kontenerów. Konfigurację projektu zapisuje się w pliku `docker-compose.yml`.

- `docker-compose build` - **Tworzenie obrazów**. Komenda ta buduje obrazy Docker na podstawie pliku `docker-compose.yml` i `Dockerfile` w projekcie. Jest to niezbędny krok, jeśli używasz niestandardowych obrazów lokalnych.
    
- `docker-compose up` - **Uruchamianie projektu**. Tworzy i uruchamia wszystkie kontenery zdefiniowane w pliku konfiguracyjnym. Może pracować w trybie `detached` (`-d`), aby działać w tle. Jeśli obrazy nie istnieją, `up` automatycznie je zbuduje.
    
- `docker-compose down` - **Zatrzymywanie i usuwanie**. Zatrzymuje i usuwa kontenery, sieci oraz wolumeny, które zostały utworzone przez `docker-compose up`. Jest to czysty sposób na zamknięcie całego środowiska.
    
- `docker-compose start` - **Uruchamianie zatrzymanych kontenerów**. Uruchamia ponownie kontenery, które zostały wcześniej zatrzymane. Przydatne, gdy nie chcesz tworzyć ich od nowa.
    
- `docker-compose stop` - **Zatrzymywanie kontenerów**. Zatrzymuje działające kontenery, ale ich nie usuwa.
    
- `docker-compose ps` - **Status kontenerów**. Wyświetla stan wszystkich kontenerów w projekcie.
    
- `docker-compose logs` - **Wyświetlanie logów**. Pokazuje logi ze wszystkich kontenerów w projekcie. Można użyć z opcją `-f` do śledzenia ich na bieżąco.
    
- `docker-compose exec [SERVICE] [COMMAND]` - **Wykonywanie komend**. Pozwala na wykonanie komendy wewnątrz już działającego kontenera. Na przykład, `docker-compose exec web bash` otworzy powłokę w kontenerze `web`.


# Tworzenie pliku `docker-compose.yml`

Plik `docker-compose.yml` jest sercem każdego projektu opartego na Docker Compose. Jest to plik tekstowy w formacie YAML, w którym definiuje się usługi (kontenery), sieci i wolumeny.

Podstawowa struktura pliku wygląda następująco:

```yml
version: '3.8'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  db:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=mysecretpassword
```

**Kluczowe sekcje:**

- `version`: Określa wersję składni pliku Compose. Wersja `3.8` jest najczęściej używana i wspiera najnowsze funkcje.
    
- `services`: Lista wszystkich kontenerów, które mają zostać uruchomione. Każdy wpis w tej sekcji to oddzielny serwis, który będzie uruchomiony jako kontener.
    
- `image`: Nazwa obrazu, który ma zostać użyty do stworzenia kontenera (np. `nginx`, `postgres`).
    
- `ports`: Mapowanie portów, analogiczne do opcji `-p` w `docker run`.
    
- `environment`: Zmienne środowiskowe, które zostaną przekazane do kontenera.
    

Więcej opcji, które można zdefiniować w `docker-compose.yml` to m.in.:

- `build`: Służy do budowania obrazu z lokalnego `Dockerfile`.
    
- `volumes`: Definiowanie wolumenów do przechowywania danych.
    
- `networks`: Tworzenie niestandardowych sieci dla kontenerów.

## Zaawansowana struktura:

```yaml
services:
  client-react-vite:
    image: client-react-vite
    build:
      context: ../05-example-web-application/client-react/
      dockerfile: ../../06-building-container-images/client-react/Dockerfile.3
    init: true
    volumes:
      - ./client-react/vite.config.js:/usr/src/app/vite.config.js
    networks:
      - frontend
    ports:
      - 5173:5173

  client-react-nginx:
    labels:
      shipyard.primary-route: true
      shipyard.route: '/'
    image: client-react-nginx
    build:
      context: ../05-example-web-application/client-react/
      dockerfile: ../../06-building-container-images/client-react/Dockerfile.5
    init: true
    networks:
      - frontend
    ports:
      - 80:8080
    restart: unless-stopped

  api-node:
    labels:
      shipyard.route: '/api/node/'
      shipyard.route.rewrite: true
    image: api-node
    build:
      context: ../05-example-web-application/api-node/
      dockerfile: ../../06-building-container-images/api-node/Dockerfile.7

    init: true
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://postgres:foobarbaz@db:5432/postgres

    networks:
      - frontend
      - backend

    ports:
      - 3000:3000
    restart: unless-stopped
    
  api-golang:
    labels:
      shipyard.route: '/api/golang/'
      shipyard.route.rewrite: true
    image: api-golang
    build:
      context: ../05-example-web-application/api-golang/
      dockerfile: ../../06-building-container-images/api-golang/Dockerfile.6
    init: true
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://postgres:foobarbaz@db:5432/postgres
    networks:
      - frontend
      - backend
    ports:
      - 8080:8080
    restart: unless-stopped
  
  db:
    image: postgres:15.1-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=foobarbaz
    networks:
      - backend
    ports:
      - 5432:5432
volumes:
  pgdata:
networks:
  frontend:
  backend:
```