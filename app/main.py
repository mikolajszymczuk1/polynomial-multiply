from mod.Polynomial import Polynomial

def main() -> None:
    polA: list[int] = [1, 2, 3]
    polB: list[int] = [2, 3]
    print(Polynomial.mul_simple(polA, polB))


if __name__ == "__main__":
    main()
