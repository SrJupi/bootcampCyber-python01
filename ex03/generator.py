# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:45:57 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 12:03:55 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def do_my_shuffle(lst):
    for i in range(len(lst)-1,0,-1):
        # Pick a random index from 0 to i
        j = randint(0,i)
 
        # Swap arr[i] with the element at random index
        lst[i],lst[j] = lst[j],lst[i]

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    '''
    valid_options = ['shuffle', 'unique', 'ordered', None]
    if not isinstance(text,str) or option not in valid_options:
        yield 'ERROR'
    else:
        try:
            text = text.split(sep)
        except:
            text = text.split()
        if option == 'shuffle':
            do_my_shuffle(text)
        elif option == 'unique':
            text = set(text)
        elif option == 'ordered':
            text.sort()
        for word in text:
            yield word
