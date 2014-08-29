from ocds_compiler import RECORDS_SCHEMA_URI

def release(ocid, total_value=''):
    return {
        "ocid": ocid,
        "releaseID": "",
        "releaseTag": "planning",
        "locale": "",
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


def releases_doc(*releases):
    return {
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "date": dict(date='2014-07-26'),
        "releases": list(releases),
    }


def records_doc(*records):
    # TODO This may be out of date given packages field
    return {
        "$schema": RECORDS_SCHEMA_URI,
        "publisher": dict(name='foo', scheme='sch', uid='the_uid', uri='uri'),
        "date": dict(date='2014-07-26'),
        "records": list(records),
    }
