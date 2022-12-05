from polynomial import Polynomial
from pytest import raises, approx


def test_create_polynomial_typical():
    polynomial = Polynomial([(0, -8)])
    assert polynomial.get_elements() == {0: -8}


def test_create_polynomial_more_than_one_element():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.get_elements() == {1: 5, 3: 2, 5: -1}


def test_create_polynomial_empty():
    polynomial = Polynomial()
    assert polynomial.get_elements() == {}


def test_create_polynomial_coeficient_equals_0():
    with raises(ValueError):
        Polynomial([(1, 5), (3, 2), (5, 0)])


def test_create_polynomial_negative_power():
    with raises(ValueError):
        Polynomial([(1, 5), (-3, 2), (5, 1)])


def test_set_polynomial_typical():
    polynomial = Polynomial([(0, -8)])
    polynomial.set_polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.get_elements() == {1: 5, 3: 2, 5: -1}


def test_set_empty_polynomial():
    polynomial = Polynomial([(0, -8)])
    polynomial.set_polynomial([])
    assert polynomial.get_elements() == {}


def test_create_polynomial_same_power_couple_times():
    with raises(ValueError):
        Polynomial([(1, 5), (1, 2), (5, 1)])


def test_polynomial_info_typical():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert str(polynomial) == "-x^5+2x^3+5x"


def test_polynomial_info_single_element():
    polynomial = Polynomial([(0, -8)])
    assert str(polynomial) == "-8"


def test_polynomial_info_single_element_first_power():
    polynomial = Polynomial([(1, 5)])
    assert str(polynomial) == "5x"


def test_polynomial_info_different_input():
    polynomial = Polynomial([(0, -7), (100, 3), (1, -2), (3, -2)])
    assert str(polynomial) == "3x^100-2x^3-2x-7"


def test_degree_typical():
    polynomial = Polynomial([(0, -7), (8, 3), (1, -2), (3, -2)])
    assert polynomial.degree() == 8


def test_degree_typical_max_power_0():
    polynomial = Polynomial([(0, -7)])
    assert polynomial.degree() == 0


def test_coefficient_typical():
    polynomial = Polynomial([(0, -7), (8, 3), (1, -2), (3, -2)])
    assert polynomial.coefficeint(0) == -7


def test_coefficient_power_not_in_polynomial():
    polynomial = Polynomial([(0, -7), (8, 3), (1, -2), (3, -2)])
    assert polynomial.coefficeint(5) == 0


def test_coefficient_empty_polynomial():
    polynomial = Polynomial()
    assert polynomial.coefficeint(5) == 0


def test_value_x_as_int():
    polynomial = Polynomial([(2, 3), (3, 3), (1, -2), (0, 11)])
    assert polynomial.value(2) == 43


def test_value_polynomial_of_zero_degree():
    polynomial = Polynomial([(0, -8)])
    assert polynomial.value(2) == -8


def test_value_argument_equals_zero():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.value(0) == 0


def test_value_argument_as_float():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.value(2.1) == approx(-11.82, 0.01)


def test_add_typical_polynomials():
    polynomial1 = Polynomial([(1, 5), (2, -2)])
    polynomial2 = Polynomial([(1, 5), (2, 2), (3, 3)])
    polynomial3 = polynomial1 + polynomial2
    assert polynomial3.info() == '3x^3+10x'


def test_add_typical_polynomials_different_input():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (3, -3)])
    polynomial3 = polynomial1 + polynomial2
    assert polynomial3.info() == '2x^7+3x^5+3x^2-5'


def test_add_empty_polynomial():
    polynomial1 = Polynomial()
    polynomial2 = Polynomial([(1, 7), (5, 2), (0, 3)])
    polynomial3 = polynomial1 + polynomial2
    assert polynomial3.info() == '2x^5+7x+3'


def test_sub_typical_polynomials():
    polynomial1 = Polynomial([(1, 5), (2, -2)])
    polynomial2 = Polynomial([(1, 5), (2, 2), (3, 3)])
    polynomial3 = polynomial1 - polynomial2
    assert polynomial3.info() == '-3x^3-4x^2'


def test_sub_typical_polynomials_different_input():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (3, -3)])
    polynomial3 = polynomial1 - polynomial2
    assert polynomial3.info() == '2x^7-3x^5+6x^3+3x^2-5'


def test_sub_empty_polynomial():
    polynomial1 = Polynomial()
    polynomial2 = Polynomial([(5, 3), (3, -3)])
    polynomial3 = polynomial1 - polynomial2
    assert str(polynomial3) == '-3x^5+3x^3'
