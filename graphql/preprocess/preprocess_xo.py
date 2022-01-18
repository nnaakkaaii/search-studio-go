import os
import argparse
from glob import glob


def preprocess_xo(model_path: str, models_dir: str) -> None:
    d = {}
    with open(model_path, 'r') as f:
        for line in f.readlines():
            d[line.strip().split(' ')[0]] = '*' in line
    paths = glob(os.path.join(models_dir, '*.go'))
    for path in paths:
        lines = []
        with open(path, 'r') as f:
            for line in f.readlines():
                nm = line.strip().split(' ')[0]
                if 'json' in line:
                    if nm in d and d[nm]:
                        line = line.replace(
                            'int ', '*int '
                        ).replace(
                            'float ', '*float '
                        ).replace(
                            'float64 ', '*float64 '
                        ).replace(
                            'string ', '*string '
                        ).replace(
                            'time.Time ', '*time.Time '
                        ).replace(
                            'bool ', '*bool '
                        )
                    else:
                        line = line.replace(
                            'int ', 'int  '
                        ).replace(
                            'float ', 'float  '
                        ).replace(
                            'float64 ', 'float64  '
                        ).replace(
                            'string ', 'string  '
                        ).replace(
                            'time.Time ', 'time.Time  '
                        ).replace(
                            'bool ', 'bool  '
                        )
                lines.append(line)
        with open(path, 'w') as f:
            f.writelines(lines)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_path',
        '-p',
        type=str,
        default=os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            '..',
            'graph',
            'model',
            'models_gen.go'
        )),
    )
    parser.add_argument(
        '--models_dir',
        '-d',
        type=str,
        default=os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            '..',
            'models',
        )),
    )
    args = parser.parse_args()
    preprocess_xo(
        args.model_path,
        args.models_dir,
    )
