if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(data, *args, **kwargs):
    rows_count = data["count"]
    chunk_size = kwargs["chunk_size"]
    users = []
    metadata = []

    missing = 1 if rows_count % chunk_size else 0

    needed_chunks = (rows_count // chunk_size) + missing

    for i in range(needed_chunks):
        users.append(dict(id=i, offset=chunk_size*i))
        metadata.append(dict(block_uuid=f'for_user_{i}'))

    return [
        users,
        metadata, # optional
    ]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
