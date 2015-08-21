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
        "publishedDate": release_doc['publishedDate'],
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
            raise NotImplementedError, "URI must of type file:///"

        # Open the file and add the json
        file_path = split[1]
        with open(file_path, 'rb') as f:
            release_doc = json.loads(f.read())

        for release in release_doc['releases']:
            ocid = release['ocid']
            release_by_ocid[ocid].append({
                "name": release['id'],
                "scheme": None,
                "uid": release['id'],
                "uri": uri
            })

    records = assemble_records(release_by_ocid)

    return {
        "$schema": RECORDS_SCHEMA_URI,
        "publisher": {
            #"name": None,
            #"scheme": None,
            #"uid": None,
            #"uri": None
       },
        #"uri": None,
        #"publishedDate": None,
        "packages": uri_list,
        "records": records
    }
