def compile(release_list):
    [release] = release_list
    return {
        'publisher': release['publisher'],
        'publishingMeta': release['publishingMeta'],
        'records': [],
    }
