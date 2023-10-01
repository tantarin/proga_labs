import pytest

from sem_7.lab_1.main import integrate
from math import sin, pi


@pytest.mark.parametrize("n_iter", [10**4, 10**5, 10**6])
def test_integration_sin(n_iter):
    a = 0
    b = pi
    result = integrate(sin, a, b, n_iter)
    expected_result = 2.0  # Интеграл sin(x) от 0 до pi равен 2.0
    assert abs(result - expected_result) < 1e-6