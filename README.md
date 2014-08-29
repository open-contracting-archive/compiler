## Compiler

Take the open contracting list of releases and compile a snapshot contracting record


### Installation

Clone this repository, then run `pip install -r requirements.txt`.


### Command-line use

```bash

# compile multiple files into records.json with linked releases (much more
space efficient)
./compile.py linked file:///full/file/path/releases1.json file:///full/file/path/releases2.json > records.json
```

You can also compile with releases embedded, but this is currently out of date
with spec.
```bash
# compile multiple files into records.json with releases embedded
./compile.py full releases1.json releases2.json > records.json

# read from stdin and compile with releases embedded
cat releases.json | ./compile full - > records.json
```

### Tests

First install testing requirements (`pip install -r requirements-dev.txt`),
then invoke `pytest`.
