## Podstawowe komendy:
- docker pull (image name) - pobiera obraz z repozytorium publicznego
- docker run (image name) - pobiera jeśli nie ma i buduje kontener, możliowści: -d (detached mode), -pX:Y (określa port), --name (określa nazwę) 
- docker stop (container ID or name) - zatrzymuje kontener
- docker start (container ID or name) - startuje zatrzymany kontener
- docker rm (container ID or name) - usuwa kontener
- docker attach (container ID or name) - wchodzi do maszyny
- docker build . - szuka Dockerfile i buduje obraz
	- -t (name:version) - nadaje nazwe
- 
## Dockerfile:
- komendy z CAPSLOCK a argumenty normalnie np dla node:
		![[dockerfile_node.png]]
- dla golang np:
		![[dockerfile_golang.png]]
- 