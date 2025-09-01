#### 1. Co to ?
- To odpowiednik docker run ustrukturyzowany w  pliku [[.yml]] , służy do startu 
#### 2. Najczęściej używane opcje:
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
#### 3. Zaawansowane opcje:

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