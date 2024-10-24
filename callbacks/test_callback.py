if 'callback' not in globals():
    from mage_ai.data_preparation.decorators import callback


@callback('success')
def success_callback(*parent_block_data, **kwargs):
    kwargs.get("pipeline_uuid")
    print("CALLBACK success")


@callback('failure')
def failure_callback(*parent_block_data, **kwargs):
    """
    The error that caused the block to fail is passed in as keyword
    argument __error.
    """
    kwargs.get("pipeline_uuid")
    print("CALLBACK failure")
