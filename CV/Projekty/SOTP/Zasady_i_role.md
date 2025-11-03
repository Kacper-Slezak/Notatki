## 📝 Zasady i Role SOTP (System Observability & Telemetry Platform)

Witajcie w naszym centrum operacyjnym! Ten serwer służy do usprawnienia komunikacji i przyspieszenia rozwoju projektu. Prosimy o przestrzeganie poniższych zasad i prawidłowe używanie ról.

### I. Główne Role Zespołu

Każdy z nas jest kluczowy. Tagi (wzmianki) pełnią funkcję "kierowania biletu" do odpowiedniej osoby.

| Rola | Odpowiedzialność | Kiedy Tagować? |
| :--- | :--- | :--- |
| **@DevOps** (Ty) | Infrastruktura, DB, CI/CD, Alerting, Security (Vault), Architektura. | Pytania o Docker Compose, Traefik, migracje bazy, błędy w pipeline. |
| **@Frontend** (Osoba 2) | Cały UI/UX, Next.js, komponenty React, Grafana (wizualizacja). | Pytania o design, błędy w interfejsie, wymagania dotyczące danych z API. |
| **@Collector** (Osoba 3) | Backend (FastAPI Core), Kolektory (SNMP, SSH, Syslog, ICMP), Celery, Parsowanie danych. | Pytania o logikę biznesową, API (CRUD), błędy w zbieraniu danych. |
| **@Admin** | Utrzymanie serwera, uprawnienia, kluczowe decyzje. | **Nie tagować bez potrzeby.** |

### II. Kluczowe Zasady Komunikacji

1.  **Tagowanie jest Kluczowe:** Zawsze **taguj** odpowiednią rolę lub osobę, jeśli Twoje pytanie dotyczy jej obszaru odpowiedzialności. **Nigdy nie taguj `@everyone`**.
2.  **Kontekst i Wątki:** Używaj **Wątków (Threads)** w kanałach, aby nie zaśmiecać głównego wątku. Jeśli zaczynasz nowy temat, stwórz wątek.
3.  **Bloker/Impediment:** Jeśli utknąłeś (masz **BLOKER**), opisz problem w odpowiednim kanale (np. `backend-fastapi`) i zawsze zakończ wiadomość:
> "BLOKER: Czekam na klucze SSH z HashiCorp Vault od **@DevOps**."
4.  **Kanały Automatyczne są Nietykalne:** Kanały `*-deploy` i `alerts-i-monitoring` służą do automatycznych komunikatów (Webhooks). **Nie pisz tam ręcznie!** Pytania i komentarze kieruj do `infra-devops` lub `ogólny`.

### III. Struktura i Cel Kanałów (Skrót)

| Kategoria/Kanał | Cel | Zezwolenie na Pisanie |
| :--- | :--- | :--- |
| `📢-ogloszenia` | Tylko komunikaty od `@Admin` i lidera. | Tylko `@Admin` |
| `🔗-linki-i-repo` | Linki do GitHuba, Grafany, Docs. | Tylko `@Admin` |
| `infra-devops` | Dyskusje i pytania o cały stack, bazy danych, Docker. | Głównie **@DevOps** i **@Collector** |
| `api-kontrakt` | Wspólne definiowanie schematów API (JSON, Pydantic). | **Wszyscy** (Ścisła współpraca) |
| `🐛-zgłaszanie-bugów` | Zgłaszanie problemów (jeśli nie używamy Jira/GitHub Issues). | **Wszyscy** |
| `🎙️ Główny Pokój Dev` | Miejsce na Stand-Up, Code Review, Pair Programming. | **Wszyscy** |

---