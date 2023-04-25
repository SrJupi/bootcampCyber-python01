# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:42:19 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 11:29:26 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    '''A class representing a Game of Thrones character'''
    
    def __init__(self, first_name='Faceless Men', is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    '''A class representing a Stark family member'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = self.__class__.__name__
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
        
    def die(self):
        self.is_alive = False
