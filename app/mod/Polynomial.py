class Polynomial:
    def __init__(self) -> None:
        pass

    @staticmethod
    def mul_simple(polA: list[int], polB: list[int]) -> list[int]:
        """ Simple polynomial multiplication """

        degreeA: int = len(polA) - 1
        degreeB: int = len(polB) - 1
        final_degree: int = degreeA + degreeB
        result: list[int] = [0] * (final_degree + 1)

        for i in range(degreeA + 1):
            for j in range(degreeB + 1):
                result[i + j] += polA[i] * polB[j]

        return result
