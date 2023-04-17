# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:52:49 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/17 13:57:38 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(x, str) for x in words):
            return -1
        if not all(isinstance(x, (int, float)) for x in coefs):
            return -1
        value = 0
        for pair in zip (coefs, words):
            value += pair[0] * len(pair[1])
        return (value)
        
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(x, str) for x in words):
            return -1
        if not all(isinstance(x, (int, float)) for x in coefs):
            return -1
        value = 0
        for i, word in enumerate (words):
            value += coefs[i] * len(word)
        return (value)
