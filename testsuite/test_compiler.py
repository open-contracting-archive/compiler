from ocds_compiler import compile_full
from .utils import release, releases_doc, records_doc


def test_compile_empty():
    assert compile_full([releases_doc()]) == records_doc()


def test_compile_different_ocid():
    doc_in = releases_doc(
        release('foo id', total_value='1234'),
        release('bar id', total_value='5678'),
    )

    doc_out = records_doc(
        dict(ocid='bar id', releases=[release('bar id', total_value='5678')]),
        dict(ocid='foo id', releases=[release('foo id', total_value='1234')]),
    )

    assert compile_full([doc_in]) == doc_out


def test_compile_same_ocid():
    doc_in = releases_doc(
        release('foo id', total_value='1234'),
        release('foo id', total_value='5678'),
    )

    doc_out = records_doc(
        dict(ocid='foo id', releases=[
            release('foo id', total_value='1234'),
            release('foo id', total_value='5678'),
        ]),
    )

    assert compile_full([doc_in]) == doc_out


def test_multiple_documents_same_ocid():
    doc_in_list = [
        releases_doc(release('foo id', total_value='1234')),
        releases_doc(release('foo id', total_value='5678')),
    ]

    doc_out = records_doc(
        dict(ocid='foo id', releases=[
            release('foo id', total_value='1234'),
            release('foo id', total_value='5678'),
        ]),
    )

    assert compile_full(doc_in_list) == doc_out
