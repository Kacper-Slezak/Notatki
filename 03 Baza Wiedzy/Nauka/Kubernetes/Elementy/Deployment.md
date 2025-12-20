---
typ: nauka
technologia: kubernetes
status: do-powtórki # lub opanowane
data: 2024-12-20
---
# Co to jest ?

1. Warstwa abstrakcji ponad [[ReplicaSet]] i [[Pod]]
2. Zapewnia możliwości automatycznego ulepszania obrazów w momencie przyjścia nowego z  [[Docker Registry]] 
3. Zarządza wieloma instancjami web serwera 
4. Ulepszenie obrazów jest selektywnie jedno po drugim aby nie odciąć użytkowników od wszystkich web serwerów
5. Można cofać wprowadzone zmiany 


# Jak tworzymy ?

1. Bardzo podobnie wręcz tak samo ja [[ReplicaSet]] jedyna róznica to kind