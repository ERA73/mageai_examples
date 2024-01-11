from os import path
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from utils.data_type_manager import TableMapper

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    db_name = 'postgres'
    schema = 'public'
    table_name = 'ejemplo'
    mapper = TableMapper()

    credentials = ConfigFileLoader(config=
        {'POSTGRES_DBNAME': db_name,
        'POSTGRES_USER': 'admin',
        'POSTGRES_PASSWORD': 'postgres',
        'POSTGRES_HOST': 'host.docker.internal',
        'POSTGRES_PORT': '5433',
        'POSTGRES_SCHEMA': schema,}
    )


    with Postgres.with_config(credentials) as loader:
        full_table_name = f"{db_name}.{schema}.{table_name}"
        output = f"{db_name}.{schema}.{table_name}_2"
        datatypes_loaded = mapper.get_table_types(loader, schema, table_name)
        data = loader.load(f"SELECT * FROM {db_name}.{schema}.{table_name}")
        print("###################################################################")
        print(datatypes_loaded)
        print("###################################################################")
        print(data.dtypes)
        print("###################################################################")
        print("###################################################################")
        print(datatypes_loaded)
        print("###################################################################")
        result = {'table_name':output, 'data':data.to_dict('r'), 'types':datatypes_loaded}
        return result


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'