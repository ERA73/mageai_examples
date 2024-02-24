# ENVIRONMENT VARIABLES
Set up your enviroment variables as follows:
* MAGE_DATABASE_CONNECTION_URL allow you to use a DB for replase the default DB sqLite.
``` bash
MAGE_DATABASE_CONNECTION_URL=postgresql+psycopg2://admin:postgres@host.docker.internal:5430/postgres
```
* REDIS_URL allow you to create schedulers and orchestrate them 
``` bash
REDIS_URL=redis://redis:6379/0
```