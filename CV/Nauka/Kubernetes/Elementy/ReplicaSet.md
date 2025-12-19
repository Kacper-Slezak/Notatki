
# Co to jest ?

1. Nowsza odmiana [[Replications-Controller]]
2. Pełni tą samą funkcje utrzymania liczby podów 
3. Jest procesem który monitoruje nasze pody opierając się na label określonych w metadata

# Jak stworzyć

1. apiVersion: apps/v1
2. kind: ReplicaSet
3. metadata: 
	1. name: 
	2. labels
4. spec:
	1. template:
		1. metada + spec poda
	2. replicas: ilość replik
	3. ==selector== tu jest różnica największa
		1. określa które pody sa poniżej tej replica set może zarządzać też nei stowrzonymi przez niego podów jesli zgadzają się
		2. matchLabels:
			1. type: przykłąd

# Jak robić scaling ?

1. Zmienić w pliku i dać create
2. Użyć scale --replicas=6 -f nawa pliku 
