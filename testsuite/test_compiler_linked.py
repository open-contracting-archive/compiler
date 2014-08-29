import json
import pytest
from os import path
from ocds_compiler import compile_linked
from ocds_compiler import RECORDS_SCHEMA_URI


"""
{
    "publisher": {
        "name": "",
        "scheme": "",
        "uid": "",
        "uri": ""
    },
    "date": "2014-07-26",
    "packages": packages,
    "records": [
        {
            "ocid": "",
            "name": "",
            "releases": "",
            "compiledRecord": {
                "date": ""
            }
        }
    ]
}
"""


@pytest.fixture
def release_p1():
    return path.join(path.dirname(path.realpath(__file__)),
                     'release_package_1.json')


@pytest.fixture
def release_p2():
    return path.join(path.dirname(path.realpath(__file__)),
                     'release_package_2.json')


def test_compile_linked_inserts_packages(release_p1, release_p2):
    path_list = [release_p1, release_p2]
    uri_list = ['file://' + p for p in path_list]

    returned_record = compile_linked(uri_list)
    assert returned_record['packages'] == uri_list


def test_compile_linked_puts_release_id_from_file_in_record(release_p1):
    uri = "file://" + release_p1
    with open(release_p1, 'rb') as f:
        release_package = json.loads(f.read())
    expected_release_id = release_package['releases'][0]['releaseID']
    expected_ocid = release_package['releases'][0]['ocid']
    expected_record = {
        "$schema": RECORDS_SCHEMA_URI,
        "publisher": { "name": "", "scheme": "", "uid": "", "uri": "" },
        "date": "",
        "packages": [uri],
        "records": [
            {
                "ocid": expected_ocid,
                "releases": [
                    {
                        "name": "",
                        "scheme": "",
                        "uid": expected_release_id,  # nopep8
                        "uri": uri
                    }
                ],
            }
        ]
    }
    assert compile_linked([uri]) == expected_record


def test_puts_release_ids_from_file_in_same_record(release_p2):
    uri = "file://" + release_p2
    with open(release_p2, 'rb') as f:
        release_package = json.loads(f.read())

    release_1 = release_package['releases'][0]
    release_2 = release_package['releases'][1]

    assert release_1['ocid'] == release_2['ocid'], "Test data is not correct."

    expected_release_id_1 = release_1['releaseID']
    expected_release_id_2 = release_2['releaseID']
    expected_ocid = release_1['ocid']

    returned_record_package = compile_linked([uri])

    assert len(returned_record_package['records']) == 1

    returned_record = returned_record_package['records'][0]

    expected_releases = [
        {
            "name": "",
            "scheme": "",
            "uid": expected_release_id_1,
            "uri": uri
        },
        {
            "name": "",
            "scheme": "",
            "uid": expected_release_id_2,
            "uri": uri
        }
    ]

    assert returned_record['releases']


def test_assembles_multiple_ocids(release_p1, release_p2):
    filepath_list = [release_p1, release_p2]
    uri_list = ['file://' + p for p in filepath_list]

    returned_record_package = compile_linked(uri_list)

    returned_records = returned_record_package['records']

    assert returned_records[0]['ocid'] == 'OCID_1'
    assert len(returned_records[0]['releases']) == 1
    assert returned_records[1]['ocid'] == 'OCID_2'
    assert len(returned_records[1]['releases']) == 2


