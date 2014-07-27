## Compiler

Take the open contracting list of releases and compile a snapshot contracting record


### Installation

Clone this repository, then run `pip install -r requirements.txt`.


### Command-line use

```bash
# compile multiple files
./compile releases1.json releases2.json > records.json

# read from stdin
./compile - > records.json
```


### Tests

First install testing requirements (`pip install -r requirements-dev.txt`),
then invoke `pytest`.
