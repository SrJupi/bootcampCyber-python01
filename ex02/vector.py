# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:44:46 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/20 13:45:56 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.tracebacklimit=0

class Vector:
    def __init__ (self, value):
        self.value = None
        if isinstance(value,(int)):
            if value > 0:
                value = (0, value)
        if isinstance(value,tuple):
            if len(value) == 2:
                if value[0] < value[1]:
                    self.handle_tuple(value)
        if isinstance(value, list) and len(value) > 0:
            self.handle_list(value)
        if self.value == None:
            raise TypeError('Value not valid')
        self.shape = (len(self.value),len(self.value[0]))
        
    def handle_tuple(self, value):
        self.value = []
        for i in range (value[0], value[1]):
            self.value.append([float(i)])
    
    def handle_list(self, value):
        if len(value) == 1:
            if not all(isinstance(x, (float, int)) for x in value[0]):
                return
        else:
            if not all(len(x) == 1 and isinstance(x[0], (float, int)) for x in value):
                return
        '''
        inner_lst = value[0]
        print(value, '-', inner_lst)
        if not isinstance(inner_lst, list):
            return
        if len(inner_lst) == 0:
            return
        if isinstance(inner_lst[0], (float, int)):
            if not all(isinstance(x, (float, int)) for x in inner_lst):
                return
        if isinstance(inner_lst[0], list):
            if not all(len(x) == 1 and isinstance(x[0], (float, int)) for x in inner_list):
                return'''
        self.value = value

    def T(self):
        '''Return the transpose vector'''
        pass
    def dot(self, other):
        '''Return the dot product between two vectors of same shape'''
        pass
    
    ### Review add and mult... row should be [[1, 2, 3]] and it was coded to handle [1, 2, 3]
    def __radd__(self, other):
        return self.__add__(other)
        
    def __add__(self, other):
        '''Return the sum between two vectors of same shape'''
        if isinstance(other, Vector):
            if other.shape == self.shape:
                tmp = [x+y for x,y in zip(self.value, other.value)]
                if isinstance(tmp[0], list):
                    tmp = [[sum(item)] for item in tmp]
                return Vector(tmp)
            else:
                raise NotImplementedError('sum between Vectors of different shape not implemented')
        raise NotImplementedError(f'sum between {type(self).__name__} and {type(other).__name__} not implemented')
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __sub__(self, other):
        '''Return the difference between two vectors of same shape'''
        if isinstance(other, Vector):
            if other.shape == self.shape:
                #do the sub and return Vector
                pass
            else:
                raise NotImplementedError('subtraction between Vectors of different shape not implemented')
        raise NotImplementedError(f'subtraction between {type(self).__name__} and {type(other).__name__} not implemented')

    def __rmul__(self, other):
        return self.__mult__(other)
        
    def __mult__(self, other):
        ''''Return the multiplication between a scalar and a vector'''
        if isinstance(other, (float, int)):
            tmp = [x * other for x in self.value]
            if isinstance(tmp[0], list):
                tmp = [[sum(item)] for item in tmp]
            return Vector(tmp)
        raise NotImplementedError(f'multiplication between {type(self)} and {type(other)} not implemented')
    
    def __rtruediv__(self, other):
        raise NotImplementedError(f'division between {type(other)} and {type(self)} not implemented')

    def __truediv__(self, other):
        pass

    def __str__(self):
        txt = f'Vector({self.value})'
        return txt

    def __repr__(self):
        return self.__str__
        
if __name__ == '__main__':
    
    x = Vector([[1.], [2.], [3.]])
    print(x.shape)
    y = Vector([[2.], [4.], [6.]])
    print(y.shape)
    z = Vector([[1., 2, 3.]])
    print(z)
    print(z.shape)
    print(x + y)
    print(x + y)
    print(5 * y)
    print('x:',x.value)
    print('y:',y.value)
    
    
    a = Vector((1))
    print(a)
    print(a.shape)
