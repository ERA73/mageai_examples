from os import path
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from utils.data_type_manager import TableMapper

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    table_name = data['table_name']
    mapper = TableMapper()

    credentials = ConfigFileLoader(config=
        {'POSTGRES_DBNAME': 'postgres',
        'POSTGRES_USER': 'admin',
        'POSTGRES_PASSWORD': 'postgres',
        'POSTGRES_HOST': 'host.docker.internal',
        'POSTGRES_PORT': '5433',
        'POSTGRES_SCHEMA': 'public',}
    )

    query = mapper.generate_create_table_postgres(table_name, data['types'])

    print(query)
    data_types = mapper.resume_data_types(data['types'])

    print(data_types)

    queries = mapper.generate_insert_queries_postgres(table_name, data['data'], data_types)

    print(queries)

    with Postgres.with_config(credentials) as loader:
        loader.execute(f"drop table {table_name}")
        loader.execute(query)
        loader.execute("commit")
        
    with Postgres.with_config(credentials) as loader:
        for insert_query in queries:
            loader.execute(insert_query)
            loader.execute("commit")

