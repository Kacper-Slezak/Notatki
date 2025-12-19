
**Temat:** Re: Analiza mechanizmów bezpieczeństwa w klastrze obliczeniowym Kubernetes – doprecyzowanie

**Panie Doktorze,**

Dziękuję za wskazówki. Ruszyłem już z budową środowiska laboratoryjnego i mam garść pierwszych wniosków.

1. Kwestia narzędzia

Postawiłem na narzędzie k3d. To w praktyce certyfikowany k3s, tylko zapakowany w kontenery Docker'a. Funkcjonalnie to to samo, a na laptopie pozwala mi to sprawnie stawiać i resetować klaster, więc uznałem, że na start będzie idealne. Nie wiem jak będzie to miało wpływ w prawdziwym badaniu, więc prosił bym o opinie 

2. Wnioski z analizy kryptograficznej (TLS 1.3)

Zrobiłem głębszy research standardu TLS 1.3 (domyślnego w Istio). Zgodnie ze specyfikacją (RFC 8446) ten protokół jest bardzo restrykcyjny – ma tylko 5 zestawów szyfrów i wyciął stare algorytmy. Próbowałem wymusić ręczną podmianę szyfru na inny, ale zgodnie z przewidywaniami – nie powiodło się to (system to ignoruje).
Zamiast walczyć ze standardem cofnąć się na klastrze do **TLS 1.2**  gdzie chyba można podmieniać algorytmy kryptograficzne, jednak to starszy standard.

3. Inne zagadnienia (Zero Trust)

Inną możliwością bezpieczeństwa są polityki autoryzacyjne. Które też można by było przebadać, na przykład ich narzut.
Możliwe, że są też inne możliwości o których nie pomyślałem. 

Z poważaniem,

Kacper Ślęzak