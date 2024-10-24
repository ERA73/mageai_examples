if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    blocks_data = []
    blocks = []
    for index in range(5):
        blocks_data.append(dict(
            index=index, 
            data = {
                "col_1":[{"name":f"pepito_{turn}", "age":index**2} for turn in range(10000)],
                "col_2":[{"name":f"juanita_{turn}", "age":index**2} for turn in range(10000)],
                "col_3":[{"name":f"sultanito_{turn}", "age":index**2} for turn in range(10000)]
            }
        ))
        blocks.append(dict(block_uuid=f"block_{index}"))

    return [
        blocks_data,
        blocks
    ]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
