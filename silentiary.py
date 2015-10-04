"""Silentiary.

Usage:
  silentiary.py list [path] [--recursive]
  silentiary.py insert <path> [--prop=p] <value>
  silentiary.py generate <path> [--prop=p] [--chars] [--length]
  silentiary.py read <path> [--prop=p]
  silentiary.py copy <path> [--prop=p]
  silentiary.py open <path> [--prop=p]
  silentiary.py type <path>
  silentiary.py delete <path> [--prop=p]

Options:
  -h --help     Show this screen.
  --version     Show version.
  --recursive   Recurse all child paths.
  --prop=<p>    Define property [default: password].
  --chars       Define character set used in generation.
  --length      Define length to generate.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Silentiary 1.0')
    print(arguments)
