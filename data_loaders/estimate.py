from mage_ai.io.postgres import Postgres
from mage_ai.io.config import ConfigFileLoader
from utils.decorators import output_memory
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@output_memory
@data_loader
def load_data(*args, **kwargs):
    db_name, schema, table_name = kwargs["table_origin"].split(".")

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
        data = loader.load(f"SELECT count(1) FROM {db_name}.{schema}.{table_name}").to_dict('r')
        return data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
