
## Podział na moduły:
1. Main - wywołanie wszystkiego 
	1. Klasa dla Random Forest dla uczenie 
	2. Klasa dla Random Forest dla online - na przyszłość
	3. Klasa dla CNN dla uczenia - na przyszłość
	4. Klasa dla CNN dla online  - na przyszłość
	5. Może MultiModal - na przyszłość
	6. UI - na przyszłość 
2. Sniffer - dla online klasyfikacji 
	1. Zbiera wszytsko z karty
	2. "Zapisuje do pcap" 
3. Sniffer per process - dla danych uczących
	1. Zbiera zgodnie z procesem
	2. Zapisuje do pcap 
4. Agregacja i liczenie cech:
	1. Dostawał "pcap"
	2. Agreguje zgodnie z 5 tuple 
	3. Liczy pożądane cechy ?? 
	4. Granularność ??
	5. Maskuje co trzeba ?? 
5. Moduł Random Forest - dla uczenia 
	1. Nauka 
	2. Ocena 
	3. Itp.
6. Moduł Random Forest - dla online klasyfikacji 

### Cechy:
1. Długość piakietów
	- Max 
	- Odchylonie standardowe
	- Mediana p 50
	- Median p  75
2. Payload
	- Mediana
3. IAT
	- Odchylenie
	- Percentyle 75 - Mediana
	- Percentyle 95 - Mediana
	- Koleracja std/mean
	- Mediana
### Granularność 
- 100
- 50
- 150