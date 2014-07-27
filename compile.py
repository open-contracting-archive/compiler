#!/usr/bin/env python

from collections import defaultdict


def compile(release_doc_list):
    release_by_ocid = defaultdict(list)
    for release_doc in release_doc_list:
        for release in release_doc['releases']:
            ocid = release['releaseMeta']['ocid']
            release_by_ocid[ocid].append(release)

    records = [
        dict(ocid=ocid, releases=releases)
        for (ocid, releases) in sorted(release_by_ocid.items())
    ]

    return {
        'publisher': release_doc['publisher'],
        'publishingMeta': release_doc['publishingMeta'],
        'records': records,
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
