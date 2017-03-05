#!/usr/bin/env python
# Copyright 2015-2017 Paul Norman
# Licensed under the MIT license

import sys, yaml, json
try:
    json.dump(yaml.safe_load(sys.stdin), sys.stdout, indent=2, separators=(',', ': '))
except yaml.YAMLError as e:
    sys.stderr.write("YAML error:\n%s\n" % e)
    sys.exit(1)
