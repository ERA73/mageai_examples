from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    schema_name = 'public'  # Specify the name of the schema to export data to
    table_name = 'ejemplo'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    
    data = mapper.apply_types(data, datatypes_loaded)

    credentials = {
        'POSTGRES_DBNAME': 'postgres',
        'POSTGRES_USER': 'admin',
        'POSTGRES_PASSWORD': 'postgres',
        'POSTGRES_HOST': 'host.docker.internal',
        'POSTGRES_PORT': '5433',
        'POSTGRES_SCHEMA': 'public',
    }

    with Postgres.with_config(credentials) as loader:
        loader.export(
            data,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )


