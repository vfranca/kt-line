import sys
import kt_line


def cli():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(kt_line.line(a, b))


if __name__ == "__main__":
    cli()
