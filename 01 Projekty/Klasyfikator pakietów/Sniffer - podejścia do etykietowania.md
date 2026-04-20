## Możliwe podejścia do automatycznego etykietowania
1. Podejście procesowe:
	- Przepytujemy komputer o procesy odpalona na nim
	- Dopsowujemy porty lokalne do procesów
	- Scrapujemy pakiety i poszukujemy w porcie źródłowym lub docelowym naszych portów przypisanych do procesów aplikacji która nas interesuje
	- Zapisujemy pakiety do pliku
2. Podejście przeglądarkowe:
	1. SNI
		- Przy każdym połączeniu TLS przeglądarka wysyła niezaszyfrowaną nazwę domeny 
		- SNI - Server name indentifcator jest wyciągany przez Scapy z wiadomości
		- Działa dla HTTPS, ale nie dla QUIC bo tam jest zaszyfrowany 
	2. DNS
		- Łapiemy dns zapisujemy ip i nazwe domeny
		- Kiedy pakiet idzie z tego ip lub do niego etykietujemy pod domenie
		- Uzupełnienie do SNI dla QUIC
		- Niektóe CDN Akamai obsługują bardzo dużo domen pod jednym IP