# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:44:46 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 13:48:28 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, value):
        """Vector constructor
Args:
    value: value to initialize the Vector, must be:
        -> a list of a list of floats: Vector([[0., 1., 2., 3.]])
        -> a list of lists of single float: Vector([[0.], [1.], [2.], [3.]])
        -> a size: Vector(3)
        -> a range: Vector((10, 16))
Return:
    A Vector
    Raise TypeError if Vector could not be created"""
        self.values = None
        if isinstance(value, int):
            if value > 0:
                value = (0, value)
                self.handle_tuple(value)
            else:
                raise TypeError('Size of vector must be positive')
        elif isinstance(value, tuple):
            if len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] < value[1]:
                    self.handle_tuple(value)
                else:
                    raise TypeError('Range: first item must be smaller or equal than second item')
            else:
                raise TypeError('Range must have only two integers')
        elif isinstance(value, list) and len(value) > 0:
            self.handle_list(value)
        if self.values is None:
            raise TypeError('Value not valid. Check docstring.')
        self.shape = (len(self.values), len(self.values[0]))

    def handle_tuple(self, value):
        self.values = []
        for i in range(value[0], value[1]):
            self.values.append([float(i)])

    def handle_list(self, value):
        if len(value) == 1:
            for x in value[0]:
                if not isinstance(x, (float, int)):
                    raise TypeError('Row vector must contain only numbers')
        else:
            for x in value:
                if not isinstance(x, list) or len(x) != 1 or not isinstance(x[0], (float, int)):
                    raise TypeError('Column vector must contain only lists with a single number')
        self.values = value

    def T(self):
        """Return the transpose vector"""
        if self.shape[0] == 1:
            return Vector([[num] for num in self.values[0]])
        else:
            return Vector([[lst[0] for lst in self.values]])

    def dot(self, other):
        """Return the dot product between two vectors of same shape"""
        if isinstance(other, Vector):
            if other.shape == self.shape:
                if self.shape[0] == 1:
                    return sum([x * y for x, y in zip(self.values[0], other.values[0])])
                else:
                    return sum([item[0] * other.values[i][0] for i, item in enumerate(self.values)])
            else:
                raise NotImplementedError('dot product between Vectors of different shape not implemented')
        raise NotImplementedError(
            f'dot product between {type(self).__name__} and {type(other).__name__} not implemented')

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        """Return the sum between two vectors of same shape"""
        if isinstance(other, Vector):
            if other.shape == self.shape:
                if self.shape[0] == 1:
                    return Vector([[x + y for x, y in zip(self.values[0], other.values[0])]])
                else:
                    return Vector([[item[0] + other.values[i][0]] for i, item in enumerate(self.values)])
            else:
                raise NotImplementedError('sum between Vectors of different shape not implemented')
        raise NotImplementedError(f'sum between {type(self).__name__} and {type(other).__name__} not implemented')

    def __rsub__(self, other):
        return self - other

    def __sub__(self, other):
        """Return the difference between two vectors of same shape"""
        if isinstance(other, Vector):
            if other.shape == self.shape:
                return self + (other * -1)
            else:
                raise NotImplementedError('subtraction between Vectors of different shape not implemented')
        raise NotImplementedError(
            f'subtraction between {type(self).__name__} and {type(other).__name__} not implemented')

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        """'Return the multiplication between a scalar and a vector"""
        if isinstance(other, (float, int)):
            return Vector([[other * x for x in item] for item in self.values])
        raise NotImplementedError(
            f'multiplication between {type(self).__name__} and {type(other).__name__} not implemented')

    def __rtruediv__(self, other):
        raise NotImplementedError(f'division between {type(other).__name__} and {type(self).__name__} not implemented')

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return self * (1 / other)
        raise NotImplementedError(f'division between {type(self).__name__} and {type(other).__name__} not implemented')

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        return self.__str__()
