## Podstawowe komendy:
- docker pull (image name) - pobiera obraz z repozytorium publicznego
- docker run (image name) - pobiera jeśli nie ma i buduje kontener, możliowści: -d (detached mode), -pX:Y (określa port), --name (określa nazwę) 
- docker stop (container ID or name) - zatrzymuje kontener
- docker start (container ID or name) - startuje zatrzymany kontener
- docker rm (container ID or name) - usuwa kontener
- docker attach (container ID or name) - wchodzi do maszyny
- docker build . - szuka Dockerfile i buduje obraz
	- -t (name:version) - nadaje nazwę
- docker tag (container registry tag)
- docker push (docker hub )
- docker container inspect (name or ID)
- docker logs (name or ID)
## Dockerfile:
- komendy z CAPSLOCK a argumenty normalnie np dla node:
		![[dockerfile_node.png]]
- dla golang np:
		![[dockerfile_golang.png]]

####  Ogólne zasady dla Docker'a
##### **1. Pinuj konkretne wersje**

- **Wersje obrazów bazowych**: Używaj konkretnych wersji obrazów bazowych (np. `python:3.9-slim-buster`) zamiast ogólnych (np. `python:latest`). To zapobiega nieoczekiwanym błędom, gdy nowa wersja zostanie wydana. Możesz używać wersji w formacie `major.minor` lub konkretnego hasha SHA256.
    
- **Zależności systemowe i aplikacyjne**: Zawsze pinuj wersje zależności w plikach konfiguracyjnych, takich jak `requirements.txt` (dla Pythona) czy `package.json` (dla Node.js). Dzięki temu zawsze instalujesz te same, przetestowane wersje.
    

##### **2. Używaj małych i bezpiecznych obrazów bazowych**

Wybieraj obrazy bazowe, które zawierają tylko niezbędne komponenty. Obrazy takie jak `alpine` czy `slim` są mniejsze i mają mniej potencjalnych luk w zabezpieczeniach. To przyspiesza budowanie i zmniejsza końcowy rozmiar obrazu.

#### **3. Chroń pamięć podręczną warstw**

Docker buduje obrazy warstwa po warstwie i wykorzystuje pamięć podręczną (cache). Optymalne ułożenie instrukcji może znacznie przyspieszyć ten proces.

- **Uporządkuj polecenia według częstotliwości zmian**: Umieszczaj instrukcje, które rzadziej się zmieniają (np. instalacja zależności), na początku pliku. Częściej zmieniające się (np. kopiowanie kodu źródłowego) umieszczaj na końcu.
    
- **Oddziel kopiowanie zależności od kodu źródłowego**: Zawsze najpierw skopiuj tylko pliki zawierające listę zależności (np. `requirements.txt`), zainstaluj je, a dopiero potem skopiuj resztę kodu źródłowego. Dzięki temu, jeśli zmienisz tylko kod aplikacji, Docker nie będzie musiał ponownie pobierać i instalować zależności.
    
- **Używaj `cache mounts`**: W bardziej zaawansowanych przypadkach możesz użyć argumentu `--mount=type=cache` w instrukcji `RUN`. Pozwala to na dzielenie pamięci podręcznej między różnymi kompilacjami, co jest szczególnie przydatne przy instalowaniu zależności.
    
- **Używaj `COPY --link`**: Jest to nowsza opcja, która tworzy „miękkie” linki do plików w warstwach. Dzięki temu Docker może tworzyć nowe warstwy bez fizycznego kopiowania plików, co przyspiesza proces i oszczędza miejsce.
    
- **Łącz powiązane kroki**: Używaj operatora `&&` lub `heredocs` (dokumenty wbudowane) do łączenia kilku poleceń `RUN` w jedną instrukcję. Zmniejsza to liczbę warstw, co przekłada się na mniejszy rozmiar końcowego obrazu.