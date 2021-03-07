# Calcula linha de tendencia e linha de canal


def line(a, b):
    """ Calcula o proximo ponto da linha."""
    gap = a - b
    c = b - gap
    return c


if __name__ == "__main__":
    print(line(2, 3))
