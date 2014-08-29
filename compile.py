#!/usr/bin/env python
from ocds_compiler import compile_full, compile_linked

if __name__ == '__main__':
    import sys
    import simplejson as json

    compile_type = sys.argv[1]

    if compile_type == 'full':
        doc_in_list = []

        for filename in sys.argv[2:]:
            if filename == '-':
                doc_in_list.append(json.load(sys.stdin))

            else:
                with open(filename, 'rb') as f:
                    doc_in_list.append(json.load(f))

        doc_out = compile_full(doc_in_list)

    elif compile_type == 'linked':
        doc_out = compile_linked(sys.argv[2:])

    else:
        print 'compile type must be full or linked'
        sys.exit()

    json.dump(doc_out, sys.stdout, indent=2)
