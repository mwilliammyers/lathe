import argparse
import random
import numpy as np

def percent(value):
    value = float(value)
    if not 0 < value <= 100:
        raise argparse.ArgumentError()
    if value > 1:
        value /= 100.0
    return value


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Toolkit for BYU CS 478",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='increase verbosity')
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE',
        required=True,
        help='path to ARFF file to load')
    parser.add_argument(
        '-l',
        '--layers',
        metavar='LAYER',
        nargs='+',
        type=int,
        required=True,
        help='layer sizes: <input> <hidden>... <output>')
    parser.add_argument(
        '-c',
        '--checkpoint',
        metavar='FILE',
        help='checkpoint file to save/load weights, biases etc. from')
    parser.add_argument(
        '-t',
        '--training',
        type=percent,
        default=.75,
        metavar='PERCENT',
        help='percentage of entire dataset for the training set size')
    parser.add_argument(
        '-r', '--learning-rate', type=float, default=.1, help='learning rate')
    parser.add_argument('-s', '--seed', help='random seed')
    return parser


def parse_args(parser=_parse_args):
    args, _ = parser().parse_known_args()
    if args.seed:
        # Use a seed for deterministic results
        random.seed(int(args.seed))
        np.random.seed(int(args.seed))
    return args