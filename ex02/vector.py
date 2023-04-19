# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:44:46 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/19 12:54:12 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
        if isinstance(value,list):
            ### CHECK LIST INPUT
            self.value = value
        if self.value == None:
            raise TypeError('Value not valid')
        self.shape= (len(self.value),len(self.value[0]))
        
    def handle_tuple(self, value):
        self.value = []
        for i in range (value[0], value[1]):
            self.value.append([float(i)])

        
    
    ### Review add and mult... row should be [[1, 2, 3]] and it was coded to handle [1, 2, 3]
    def __radd__(self, other):
        return self.__add__(other)
        
    def __add__(self, other):
        if isinstance(other, Vector):
            if other.shape == self.shape:
                tmp = [x+y for x,y in zip(self.value, other.value)]
                if isinstance(tmp[0], list):
                    tmp = [[sum(item)] for item in tmp]
                return Vector(tmp)
            else:
                return ('Not same Shape')
        return None
    
    def __rmul__(self,other):
        return self.__mult__(other)
        
    def __mult__(self, other):
        if isinstance(other, (float, int)):
            tmp = [x * other for x in self.value]
            if isinstance(tmp[0], list):
                tmp = [[sum(item)] for item in tmp]
            return Vector(tmp)
        return None
        
    def __str__(self):
        txt = f'Vector({self.value})'
        return txt
        
if __name__ == '__main__':
    
    x = Vector([[1.], [2.], [3.]])
    print(x.shape)
    y = Vector([[2.], [4.], [6.]])
    print(y.shape)
    z = Vector([[1., 2., 3.]])
    print(z.shape)
    print(x + z)
    print(x + y)
    print(5 * y)
    print('x:',x.value)
    print('y:',y.value)
    
    
    a = Vector((1))
    print(a)
    print(a.shape)
