from compile import compile


def test_compile_empty():
    doc_in = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "releases": [],
    }

    doc_out = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "records": [],
    }

    assert compile([doc_in]) == doc_out
