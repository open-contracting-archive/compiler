#!/usr/bin/env python
import json
from collections import defaultdict

RECORDS_SCHEMA_URI = (
    'https://raw.githubusercontent.com/open-contracting/standard/'
    'master/standard/schema/record-schema.json')


def assemble_records(release_by_ocid):
    records = [
        dict(ocid=ocid, releases=releases)
        for (ocid, releases) in sorted(release_by_ocid.items())
    ]
    return records

def compile_full(release_doc_list):
    """
    Compiles releases into a record doing a full copy of the data.
    """
    release_by_ocid = defaultdict(list)
    for release_doc in release_doc_list:
        for release in release_doc['releases']:
            ocid = release['ocid']
            release_by_ocid[ocid].append(release)

    records = assemble_records(release_by_ocid)

    return {
        "$schema": RECORDS_SCHEMA_URI,
        "publisher": release_doc['publisher'],
        "date": release_doc['date'],
        #"packages": [],  # TODO Fix tests to meet latest spec
        'records': records,
    }


def compile_linked(uri_list):
    """
    Builds a record with linked release information
    """
    release_by_ocid = defaultdict(list)
    for uri in uri_list:
        split = uri.split('//')
        protocol = split[0]
        if protocol != 'file:':
            raise NotImplementedError

        # Open the file and add the json
        file_path = split[1]
        with open(file_path, 'rb') as f:
            release_doc = json.loads(f.read())

        for release in release_doc['releases']:
            ocid = release['ocid']
            release_by_ocid[ocid].append({
                "name": "",
                "scheme": "",
                "uid": release['releaseID'],
                "uri": uri
            })

    records = assemble_records(release_by_ocid)

    return {
        "$schema": RECORDS_SCHEMA_URI,
        "publisher": {
            "name": "",
            "scheme": "",
            "uid": "",
            "uri": ""
        },
        "date": "",
        "packages": uri_list,
        "records": records
    }


if __name__ == '__main__':
    import sys
    import simplejson as json

    doc_in_list = []

    for filename in sys.argv[1:]:
        if filename == '-':
            doc_in_list.append(json.load(sys.stdin))

        else:
            with open(filename, 'rb') as f:
                doc_in_list.append(json.load(f))

    doc_out = compile(doc_in_list)

    json.dump(doc_out, sys.stdout, indent=2)
