import argparse

from nmslib_viz import view


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nmslib_index', type=str, default='data/index.nmslib')
    parser.add_argument('--number_points', type=int, default=10000)
    return parser.parse_args()


def run(nmslib_index, number_points):
    view(nmslib_index, number_points)


if __name__ == '__main__':
    args = _parse_args()
    run(args.nmslib_index, args.number_points)
