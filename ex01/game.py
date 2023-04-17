# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:42:19 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/17 13:43:24 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    '''A class representing a Game of Thrones character'''
    
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    '''A class representing a Stark family member'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
        
    def die(self):
        self.is_alive = False

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
arya.die()
print(arya.__dict__)
print(arya.__doc__)
print(GotCharacter.__doc__)
