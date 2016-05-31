from __future__ import print_function
from sh import upsc 

import json
import sys
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')



def num(s):
    try:
        return float(s)
    except ValueError:
        return s


def main():
    if len(sys.argv) == 2:
        device = sys.argv[1]
    else:
        print("Usage: main.py <UPS device name (e.g 'apc-1500@localhost')>", file=sys.stderr)
        return

    data = {}
    status = upsc(device)

    for item in status:
        first, second = item.split(': ')
        t = data
        keys = first.split('.')
        second = second.strip()
        for index, key in enumerate(keys):
            if index == len(keys) - 1:
                t = t.setdefault(key, {'value': num(second)})
            else:
                t = t.setdefault(key, {})

    print(json.dumps(data))

if __name__ == "__main__":
    main()
