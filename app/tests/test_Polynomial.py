from app.mod.Polynomial import Polynomial

class TestPolynomial:
    def test_mul_simple(self) -> None:
        # GIVEN
        polA: list[int] = [1, 2, 3]
        polB: list[int] = [2, 3]

        # WHEN
        result: list[int] = Polynomial.mul_simple(polA, polB)

        # THEN
        assert result == [2, 7, 12, 9]
