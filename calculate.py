import math_lib
import argparse

def main():
    parser = argparse.ArgumentParser(
                                     description='Give division and sum of two variables',
                                     prog='bay')

    parser.add_argument('-a',
                        metavar='--varA',
                        type=int,
                        help='Variable a',
                        required=True)

    parser.add_argument('-b',
                        metavar='--varB',
                        type=int,
                        help='Variable b',
                        required=True)

    args = parser.parse_args()

    print(str(args.a) + ' plus ' + str(args.b) + ' equals ' + str(math_lib.add(args.a, args.b)))
    print(str(args.a) + ' divided by ' + str(args.b) + ' equals ' + str(math_lib.div(args.a, args.b)))

if __name__ == '__main__':
    main()

