# Co to jest? 

1. Jest częścią narzędzi Kube Controller Manager 
2. Służy do monitorowania stanu Nodeów
3. Podejmuej akcje aby apliakcja działała
4. Node wysyła hearthbeat co 5 sekund do [[kube-apiserver]]
5. Node Controller przestanie słyszeć bicie serca uzna Node za nie osiągalny 
6. Czeka 40 sekund przed uznaniem tego stanu
7. Po uznaniu za nie osiągalny czeka 5 minut aby sam wstał
8. Przenosi Pody do diząłjacego Noda 