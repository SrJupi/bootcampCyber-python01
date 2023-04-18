# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 10:52:55 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/18 13:42:30 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
        acc_origin = self.get_account(origin)
        if not acc_origin:
            return False
        acc_dest = self.get_account(dest)
        if not acc_dest:
            return False
        if self.check_account(origin):
            return False
        if self.check_account(dest):
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
@name: str(name) of the account
@return True if success, False if an error occured
"""
        if isinstance(name, str):
            acc = self.get_account(name)
            if acc:
                errors = self.check_account(acc)
                self.fix_errors(acc, errors)
                return True
        return False

    def get_account(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

    def check_account(self, acc):
        acc_vars = vars(acc)
        print(acc_vars)
        errors = 0
        if len(acc_vars) % 2 == 0:
            print('even')
            errors |= 1
        if any(True if var[0] == 'b' else False for var in acc_vars):
            print('start b')
            errors |= 2
        if not any(True if var == 'addr' or var == 'zip' else False for var in acc_vars):
            print('not addr or zip')
            errors |= 4
        if sum(True if var == 'id' or var == 'name' or var == 'value' else False for var in acc_vars) != 3:
            print('not id or not name or not value')
            errors |= 8


        return errors



if __name__ == '__main__':
    bank = Bank()
    acc = Account("Lucas", btest='my_test')
    del(acc.value)
    print(bank.add("Teste"))
    print(bank.add(acc))
    print(bank.add(acc))
    print(bank.check_account(acc))
