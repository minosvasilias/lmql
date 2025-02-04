import lmql
from lmql.tests.expr_test_utils import run_all_tests

m = lmql.model("facebook/opt-350m", inprocess=True)

@lmql.query
async def test_model_reference():
    '''lmql
    import lmql

    argmax(chunk_timeout=10.0)
        """Hello[WHO]"""
    from
        m
    where
        STOPS_AT(WHO, "\n") and len(TOKENS(WHO)) < 10
    '''

@lmql.query
async def test_local_string():
    '''lmql
    import lmql

    argmax(chunk_timeout=10.0)
        """Hello[WHO]"""
    from
        m
    where
        STOPS_AT(WHO, "\n") and len(TOKENS(WHO)) < 10
    '''

m2 = lmql.model("facebook/opt-350m", cuda=True, inprocess=True)

@lmql.query
async def test_model_reference_cuda():
    '''lmql
    import lmql

    argmax(chunk_timeout=10.0)
        """Hello[WHO]"""
    from
        m2
    where
        STOPS_AT(WHO, "\n") and len(TOKENS(WHO)) < 10
    '''

run_all_tests(locals())