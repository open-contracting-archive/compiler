from collections import defaultdict


def compile(release_doc_list):
    [release_doc] = release_doc_list
    release_by_ocid = defaultdict(list)

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
