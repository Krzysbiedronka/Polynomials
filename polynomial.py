class Polynomial:
    """
    Class polynomial. Contains polynomial coeficients and powers.
    :elements: pairs of powers and their coeficients
    :type elements: dictionary with powers as keys and coeficeints as values
                    (all the powers and coeficeints are ints)

    returns ValueError when:
    - given negative power
    - given coeficient equal to zero
    - given the same power couple times
    """
    def __init__(self, list_of_tups=None):
        self.set_polynomial(list_of_tups)

    """
    Defined setter and getter of the polynomial
    """

    def set_polynomial(self, list_of_tups):
        self._elements = {}
        if not list_of_tups:
            list_of_tups = []
        for tup in list_of_tups:
            power = int(tup[0])
            coefficient = int(tup[1])
            if coefficient == 0 or power < 0 or power in self._elements.keys():
                raise ValueError
            self._elements[power] = coefficient
        return self._elements

    def get_elements(self):
        return self._elements

    """
    Polynomial info returns polynomial as string easy to read for user
    """

    def info(self):
        list_of_powers = list(self._elements.keys())
        list_of_powers.sort()
        list_of_powers.reverse()
        polynomial_as_str = ''
        for each_power in list_of_powers:
            char = '+'
            if self._elements[each_power] < 0:
                char = ''
            x = 'x'
            if each_power == 0:
                x = ''
            after_x = ''
            if each_power > 0 and each_power != 1:
                after_x = f'^{each_power}'
            before_x = self._elements[each_power]
            if before_x == 1:
                before_x = ''
            if before_x == -1:
                before_x = '-'
            polynomial_as_str += f'{char}{before_x}{x}{after_x}'
        if self._elements[list_of_powers[0]] >= 0:
            final_polynomial = polynomial_as_str[1:]
            return final_polynomial
        return polynomial_as_str

    def __str__(self):
        return self.info()

    """
    Returns degree of the polynomial.
    """

    def degree(self):
        list_of_powers = list(self._elements.keys())
        return max(list_of_powers)

    """
    Returns coeficient of the given power.
    Returns 0 when asked about power which is not in the polynomial
    """

    def coefficeint(self, power):
        if power not in self._elements.keys():
            return 0
        return self._elements[power]

    """
    Returns value of the polynomial with given argument x
    """

    def value(self, x):
        final_value = 0
        list_of_powers = list(self._elements.keys())
        for each_power in list_of_powers:
            a = self._elements[each_power]
            final_value += a*(x**each_power)
        return final_value

    """
    Defines addition of two polynomials
    """

    def __add__(self, other: "Polynomial"):
        new_polynomial = []
        powers_in_first = set(self._elements.keys())
        powers_in_second = set(other._elements.keys())
        set_of_equal_powers = powers_in_first.intersection(powers_in_second)
        for each_power in set_of_equal_powers:
            value1 = self._elements[each_power]
            value2 = other._elements[each_power]
            if value1 + value2 != 0:
                new_polynomial.append((each_power, value1 + value2))
        for each_power in (set(powers_in_first) - set_of_equal_powers):
            new_polynomial.append((each_power, self._elements[each_power]))
        for each_power in (set(powers_in_second) - set_of_equal_powers):
            new_polynomial.append((each_power, other._elements[each_power]))
        return Polynomial(new_polynomial)

    """
    Defines substitution of two polynomials
    """

    def __sub__(self, other: "Polynomial"):
        new_polynomial = []
        powers_in_first = set(self._elements.keys())
        powers_in_second = set(other._elements.keys())
        set_of_equal_powers = powers_in_first.intersection(powers_in_second)
        for each_power in set_of_equal_powers:
            value1 = self._elements[each_power]
            value2 = other._elements[each_power]
            if value1 - value2 != 0:
                new_polynomial.append((each_power, value1 - value2))
        for each_power in (set(powers_in_first) - set_of_equal_powers):
            new_polynomial.append((each_power, self._elements[each_power]))
        for each_power in (set(powers_in_second) - set_of_equal_powers):
            new_polynomial.append((each_power, other._elements[each_power]*-1))
        return Polynomial(new_polynomial)
