import json
import sys
import argparse
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-S', type=float, default=1)
    parser.add_argument('-E0', type=float, default=0)
    parser.add_argument('-KM', type=float, default=1)
    parser.add_argument('-k', type=float, default=1)
    parser.add_argument('--savefile', type=str, default='default')

    args = parser.parse_args()
    v = args.k*args.E0*args.S/(args.KM+args.S)
    print(v)

result = {
    "v" : v,
    "S" : args.S,
    "E0" : args.E0,
    "KM": args.KM,
    "k": args.k
}

if args.savefile != 'default':
    with open(args.savefile, "w") as out:
        json.dump(result, out, indent=4, sort_keys=True)

#AttributeError: 'Namespace' object has no attribute 'save' выходит ошибка если использовать имя --save-file, тире воспринимается как служебный символ, поэтому использую имя --savefile без тире



