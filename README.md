# Style utility scripts

Many stylesheets need scripts to do the same tasks as part of an install process. Instead of constantly writing slightly different scripts, this is a set of scripts to handle the tasks and reduce duplication of work.

## Install

Copy the scripts to your project and add them to your installation instructions.

## License

The scripts are licensed under [the MIT License](LICENSE)

## Requirements

The requirements vary by script, but as a general rule require

- Bash, sh, or Python 3.4+
- pyyaml for config file reading from python (`python3-yaml` on Debian-based systems)
- psycopg2 for database interaction (`python3-psycopg2` on Debian-based systems)

