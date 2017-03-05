# YAML to json

Converting YAML documents to JSON is a common task in style development and can be done with a couple of lines in most programming languages, but it's useful to have a script that gives useful error messages and nicer formatting.

## Requirements

- Python 2.7 or 3.4+
- pyyaml (`python-yaml` on Debian based systems)

## Usage

```sh
./yaml2json.py < input.yaml > output.json
```

It can also be used as part of more complicated command lines with pipes.
