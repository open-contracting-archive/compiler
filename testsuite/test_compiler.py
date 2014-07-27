from compile import compile


def release(ocid, total_value=''):
    return {
        "releaseMeta": {
            "ocid": ocid,
            "releaseID": "",
            "releaseTag": "planning",
            "locale": "",
        },
        "buyer": {
            "id": {"name": "", "scheme": "", "uid": "", "uri": ""},
        },
        "planning": {},
        "formation": {
            "notice": "",
            "itemsToBeProcured": [],
            "totalValue": total_value,
            "method": "Open",
            "methodJustification": "",
            "selectionCriteria": "Lowest Cost",
            "selectionDetails": "",
            "submissionMethod": "Electronic Auction",
            "submissionDetails": "",
            "tenderPeriod": "",
            "clarificationPeriod": "",
            "clarifications": False,
            "awardPeriod": "",
            "numberOfBidders": 0,
            "numberOfBids": 0,
            "bidders": [],
            "procuringEntity": {
                "id": {"name": "", "scheme": "", "uid": "", "uri": ""},
            },
            "attachments": [],
        },
        "award": {},
        "contract": {},
        "performance": {},
    }


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


def test_compile_different_ocid():
    doc_in = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "releases": [
            release('foo id', total_value='1234'),
            release('bar id', total_value='5678'),
        ],
    }

    doc_out = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "records": [
            {
                "ocid": "bar id",
                "releases": [
                    release('bar id', total_value='5678'),
                ],
            },
            {
                "ocid": "foo id",
                "releases": [
                    release('foo id', total_value='1234'),
                ],
            },
        ],
    }

    assert compile([doc_in]) == doc_out


def test_compile_same_ocid():
    doc_in = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "releases": [
            release('foo id', total_value='1234'),
            release('foo id', total_value='5678'),
        ],
    }

    doc_out = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "records": [
            {
                "ocid": "foo id",
                "releases": [
                    release('foo id', total_value='1234'),
                    release('foo id', total_value='5678'),
                ],
            },
        ],
    }

    assert compile([doc_in]) == doc_out
