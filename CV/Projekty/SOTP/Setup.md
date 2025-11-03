### 🐍 Dla dewelopera Collectorów (używającego PyCharm)

**Wymagania:** PyCharm Professional, Docker Desktop.

#### Krok 1: Skonfiguruj zdalny interpreter Python

1. Otwórz Ustawienia (`File` -> `Settings` lub `PyCharm` -> `Preferences`).
    
2. Przejdź do `Project: SOTP...` -> `Python Interpreter`.
    
3. Kliknij ikonę koła zębatego i wybierz `Add...`.
    
4. W nowym oknie wybierz **`Docker Compose`**.
    
5. **Configuration file(s):** Wskaż plik `infrastructure/docker/docker-compose.dev.yml`.
    
6. **Service:** Z listy rozwijanej wybierz usługę **`backend`**.
    
7. Kliknij **OK**. PyCharm połączy się z kontenerem i zindeksuje wszystkie pakiety.
    

#### Krok 2: Stwórz konfigurację uruchomieniową

1. W prawym górnym rogu kliknij `Add Configuration...`.
    
2. Kliknij `+` i wybierz `Python`.
    
3. **Name:** Nazwij ją `Run Backend (Docker)`.
    
4. **Script path:** Wpisz `/usr/local/bin/uvicorn`.
    
5. **Parameters:** Wpisz `app.main:app --host 0.0.0.0 --port 8000 --reload`.
    
6. **Working directory:** Ustaw na `/app`.
    
7. Kliknij **OK**.
    

Teraz możesz uruchamiać i debugować backend (w tym kod kolektorów) za pomocą zielonych przycisków `Play` i `Debug` w PyCharm. Terminal w IDE będzie połączony z kontenerem `backend`.

---

### ⚙️ Dla dewelopera Collectorów (używającego VS Code)

**Wymagania:** VS Code, rozszerzenie `Dev Containers`, Docker Desktop.

#### Krok 1: Przygotuj plik konfiguracyjny (jeśli nie istnieje)

1. W głównym katalogu projektu stwórz folder `.devcontainer`.
    
2. Wewnątrz niego stwórz plik `devcontainer.json` z poniższą zawartością:
    
    JSON
    
    ```
    {
        "name": "SOTP Backend Dev",
        "dockerComposeFile": ["../infrastructure/docker/docker-compose.dev.yml"],
        "service": "backend",
        "workspaceFolder": "/app",
        "customizations": {
            "vscode": {
                "extensions": [
                    "ms-python.python",
                    "ms-python.black-formatter",
                    "ms-python.isort"
                ]
            }
        },
        "postCreateCommand": "pip install -r requirements.txt"
    }
    ```
    

#### Krok 2: Uruchom środowisko

1. Otwórz projekt w VS Code.
    
2. Poczekaj na powiadomienie w prawym dolnym rogu i kliknij **`Reopen in Container`**.
    
3. Jeśli powiadomienie się nie pojawi, naciśnij `F1` i wpisz `Dev Containers: Reopen in Container`.
    

Po chwili VS Code przeładuje się i będziesz w pełni wewnątrz kontenera `backend`. Możesz edytować kod kolektorów, a serwer FastAPI automatycznie się przeładuje. Terminal w VS Code da Ci bezpośredni dostęp do powłoki kontenera.

---

### 🎨 Dla dewelopera Frontendu (używającego PyCharm)

Chociaż PyCharm jest głównie do Pythona, jego wersja **Professional** świetnie radzi sobie z developmentem webowym. Alternatywnie, te same kroki zadziałają w **WebStorm**, który jest dedykowanym IDE od JetBrains do JavaScript/TypeScript.

**Wymagania:** PyCharm Professional (z wtyczkami webowymi) lub WebStorm, Docker Desktop.

#### Krok 1: Skonfiguruj zdalny interpreter Node.js

1. Otwórz Ustawienia (`File` -> `Settings` lub `PyCharm` -> `Preferences`).
    
2. Przejdź do `Languages & Frameworks` -> `Node.js`.
    
3. Kliknij przycisk `...` obok pola `Node interpreter`.
    
4. W nowym oknie kliknij `+` i wybierz `Add Remote...`.
    
5. Wybierz opcję **`Docker Compose`**.
    
6. **Configuration file(s):** Wskaż plik `infrastructure/docker/docker-compose.dev.yml`.
    
7. **Service:** Z listy wybierz usługę **`frontend`**.
    
8. Kliknij **OK**.
    

#### Krok 2: Stwórz konfigurację uruchomieniową `npm`

1. W prawym górnym rogu kliknij `Add Configuration...`.
    
2. Kliknij `+` i wybierz z listy **`npm`**.
    
3. **Name:** Nazwij ją `Run Frontend (Docker)`.
    
4. **Node interpreter:** Upewnij się, że wybrany jest Twój nowo skonfigurowany, zdalny interpreter (z ikoną Dockera).
    
5. **Scripts:** Z listy rozwijanej wybierz **`dev`**.
    
6. Kliknij **OK**.
    

Teraz deweloper frontendu może uruchamiać serwer deweloperski Next.js bezpośrednio z PyCharm/WebStorm, klikając przycisk **`Play`**. Debugowanie i praca z terminalem również będą w pełni zintegrowane z kontenerem `frontend`.