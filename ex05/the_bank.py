# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 11:47:08 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 12:43:24 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
from random import randint

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
            
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
@new_account: Account() new account to append
@return True if success, False if an error occured
"""
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            return False
        for acc in self.accounts:
            if new_account.name == acc.name:
                return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
@origin: str(name) of the first account
@dest: str(name) of the destination account
@amount: float(amount) amount to transfer
@return True if success, False if an error occured
"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        acc_origin = self.get_account(origin)
        if not acc_origin:
            return False
        acc_dest = self.get_account(dest)
        if not acc_dest:
            return False
        if self.check_account(acc_origin):
            return False
        if self.check_account(acc_dest):
            return False
        if amount > acc_origin.value:
            return False
        if acc_origin.name != acc_dest.name:
            acc_origin.transfer(-amount)
            acc_dest.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
@name: str(name) of the account
@return True if success, False if an error occured
"""
        acc = self.get_account(name)
        if acc:
            errors = self.check_account(acc)
            self.fix_errors(acc, errors)
            return True
        return False

    def get_account(self, name):
        for acc in self.accounts:
            try:
                if acc.name == name:
                    return acc
            except:
                pass
        return None

    def fix_errors(self, acc, errors):
        while(errors > 0):
            if errors & 32:
                setattr(acc, 'value', 0)
            if errors & 16:
                setattr(acc, 'id', Account.ID_COUNT)
                Account.ID_COUNT += 1
            if errors & 8:
                new_name = "NAME NOT AVAIABLE FOR ID " + {self.id}
                setattr(acc, 'name', new_name)
            if errors & 4:
                setattr(acc, 'zip', "NO ZIP CODE")
            if errors & 2:
                for item in vars(acc):
                    if item[0] == 'b':
                        delattr(acc, item)
                        break
            if errors & 1:
                i = 0
                while True:
                    var = 'var_' + str(i)
                    if var not in vars(acc):
                        setattr(acc, var, 0)
                        break
                    i += 1
            errors = self.check_account(acc)
    
    def check_account(self, acc):
        acc_vars = vars(acc)
        errors = 0
        if len(acc_vars) % 2 == 0:
            errors |= 1
        if any(True if var[0] == 'b' else False for var in acc_vars):
            errors |= 2
        if not any(True if var == 'addr' or var == 'zip' else False for var in acc_vars):
            errors |= 4
        if 'name' not in acc_vars or not isinstance(acc_vars['name'], str):
            errors |= 8
        if 'id' not in acc_vars or not isinstance(acc_vars['id'], int):
            errors |= 16
        if 'value' not in acc_vars or not isinstance(acc_vars['value'], (int, float)):
            errors |= 32
        return errors



if __name__ == '__main__':
    print("Exemple 1:")
    bank = Bank()
    acc = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.add(acc)
    acc =Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    )
    bank.add(acc)

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')


    print("\nExemple 2:")

    bank = Bank()
    acc1 = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31')
    bank.add(acc1)
    acc2 = Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None)
    bank.add(acc2)
    print(acc1.name, acc1.value)
    print(acc2.name, acc2.value)

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
        print(acc1.name, acc1.value)
        print(acc2.name, acc2.value)
