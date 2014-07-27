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


def test_compile_one():
    doc_in = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "releases": [
            {
                "releaseMeta": {
                    "ocid": "foo id",
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
                    "totalValue": "",
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
            },
        ],
    }

    doc_out = {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "publishingMeta": dict(date='2014-07-26'),
        "records": [
            {
                "ocid": "foo id",
                "releases": [
                    {
                        "releaseMeta": {
                            "ocid": "foo id",
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
                            "totalValue": "",
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
                    },
                ],
            },
        ],
    }

    assert compile([doc_in]) == doc_out
