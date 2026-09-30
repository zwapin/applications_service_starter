# applications_service (starter)

Starter del technical assessment Klaaryo. Il testo dell'assessment ti è stato inviato a parte: qui trovi
come è fatto il repo, come avviarlo e i token di prova.

Il servizio è costruito sul **`mini_kit`**, un piccolo pacchetto Python installato come dipendenza
(`requirements.txt`). Riproduce in forma ridotta il modo in cui scriviamo i nostri servizi. Il sorgente
e la documentazione sono su https://github.com/zwapin/mini_kit: leggerlo è parte dell'assessment.

Per iniziare crea il tuo repository da questo template: su
https://github.com/zwapin/applications_service_starter usa **Use this template → Create a new repository**.
Puoi farlo anche privato: in quel caso aggiungi come collaboratori le persone indicate nel testo
dell'assessment. Non fare un fork: i fork di un repository pubblico sono pubblici.

## Cosa c'è già

- Configurazione Django pronta per PostgreSQL (`config/settings.py`).
- Un **modulo di esempio funzionante**, i punti vendita (`Store`), che attraversa tutti i layer:
  modello e fixture, core manager, REST manager, serializer, view, url, e un test per ogni layer.
  Usalo come riferimento per le convenzioni (vedi [Struttura](#struttura)).

Il Docker non c'è: fa parte di quello che ti chiediamo.

## Avvio in locale (senza Docker)

Serve Python 3.12, `git` (per installare `mini_kit` da GitHub) e un PostgreSQL raggiungibile.
La connessione si configura con le variabili d'ambiente elencate in `.env.example`, che sono anche i
default di `config/settings.py`: il file `.env` non viene caricato in automatico, esporta le variabili
che vuoi cambiare.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata stores
python manage.py runserver
```

```bash
curl -H "Authorization: Token <token del team 1>" http://localhost:8000/api/v1/stores
```

## Token di prova

Ogni richiesta porta l'header `Authorization: Token <jwt>`. Il kit risolve il token nell'utente e nel
team che stanno chiamando. Questi token sono firmati con il `MINI_KIT_JWT_SECRET` di default di
`config/settings.py` e non scadono.

| Utente | Team | Token |
|---|---|---|
| 10 | 1 | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxMCwidGVhbV9wayI6MSwiaWF0IjoxNzkwNzcwMzgwfQ.asIocz6jwSEOr4xbyPvPC6HILM-s1iaj4EqVcSpr1YE` |
| 20 | 2 | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoyMCwidGVhbV9wayI6MiwiaWF0IjoxNzkwNzcwMzgxfQ.fkEWN0sq1L8sYBKFs5UyBLwjKGE_EypMRuuQwG-9zyA` |
| 30 | 3 | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjozMCwidGVhbV9wayI6MywiaWF0IjoxNzkwNzcwMzgxfQ.upqOi5O3hLG6YhH6hK9uLKGUdCcf_6bCWOIsmqyQp-4` |

Se cambi `MINI_KIT_JWT_SECRET`, questi token smettono di funzionare.

Per generarne altri:

```bash
python manage.py issue_token --user-pk 40 --team-pk 1
```

## Struttura

```
config/                 settings e urls del progetto (monta rest_apis su /api/v1/)
django_db_models/
    models/             un file per modello (store.py), esportati in models/__init__.py
    migrations/
    fixtures/
managers/               core manager: la logica di dominio, a scatola nera da dati a risultati
rest_apis/
    managers/           REST manager: validano l'input API e delegano ai core manager
    serializers/        serializer di input e di output
    views/              view sottili: una chiamata al REST manager, una risposta
    urls.py
utils/                  funzioni di supporto senza dipendenze dai modelli
tests/
    db_models/          test dei modelli
    managers/           test dei core manager, senza HTTP
    rest_apis/          test delle API
```

Ogni package (`django_db_models/models/`, `managers/`, `rest_apis/managers/`, `rest_apis/serializers/`,
`rest_apis/views/`)
espone nel proprio `__init__.py` quello che gestisce: si importa dal package, non dal file.

Come passa una richiesta:

```
view (rest_apis/views)  →  REST manager (rest_apis/managers)  →  core manager (managers/)  →  modelli
      ↑ risposta JSON            ↑ valida il payload                ↑ regole di dominio,
        con i serializer           con i serializer di input          query filtrate per team
```

Il core manager non sa nulla di HTTP: riceve dati Python (id, stringhe, date), restituisce modelli
o queryset, e se qualcosa non va solleva un errore del kit. Per questo si testa senza API.

Regola di import:

```
rest_apis/views/     → rest_apis/managers/, rest_apis/serializers/
rest_apis/managers/  → managers/ (core), rest_apis/serializers/
managers/            → django_db_models/ (via apps.get_model), utils/
```

Nessun file sotto `rest_apis/` importa da `django_db_models/`, e nessuna regola di dominio sta sotto
`rest_apis/`. Dove serve la classe del modello (nei core manager e nel `Meta` dei serializer di
output) la si ottiene con `apps.get_model("django_db_models", "XModel")`, mai con un import.

## Test

```bash
python manage.py test
```

## Licenza

MIT, vedi [LICENSE](LICENSE).
