import sys
import json
from collections import OrderedDict, defaultdict
from collections.abc import Sequence, Mapping
from io import StringIO
import pprint
from re import split
from textwrap import dedent
from traceback import format_exc


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()

    def read(self):
        return self._io.read() if self._io else sys.stdin.read()

    def readline(self, parse=str, is_array=False, delimiter=r'\s+'):
        return map(parse, split(delimiter, self._readline())) if is_array else parse(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else sys.stdin.readline().strip()


INPUT = dedent('''\
{  
  "class":{  
    "id":1,
    "subject":"Math",
    "students":[  
      {  
        "name":"Alice",
        "age":30
      },
      {  
        "name":"Bob",
        "age":40,
        "address":{  
          "country":"JP"
        }
      },
      {  
        "name":"Charlie",
        "age":20,
        "address":{  
          "country":"US",
          "state":"MA",
          "locality":"Boston"
        }
      }
    ]
  }
}
''')


def main():
    with UserInput(text=INPUT) as user_input:
#        d = json.loads(user_input.read(), object_hook=hook)
        d = json.loads(user_input.read())
#        pprint.pprint(f'test: {d["book1"]["year"]}, {len(d["book1"]["year"])}')
        pprint.pprint(d)
        print(retrieve(d, ['class', 'students', 1]))
        print(retrieve(d, ['classes', 'students', 1]))
        walk(d, lambda p, v: print(f'path: {p}, value: {v}'))


def factory():
    return defaultdict(factory)


def hook(d):
    return defaultdict(factory, d)


def retrieve(obj, path):
    try:
        head, *tails = path
        return retrieve(obj[head], tails)
    except ValueError:
        return obj
    except KeyError:
        return None


def walk(obj, callback, path=[]):
    if isinstance(obj, list):
        for i in range(len(obj)):
            walk(obj[i], callback, path + [i])
    elif isinstance(obj, dict):
        for k in obj.keys():
            walk(obj[k], callback, path + [k])
    else:
        callback(path, obj)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
