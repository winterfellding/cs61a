def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"

    attempts = []
    def account(amount, the_pass):
        nonlocal balance
        if len(attempts) == 3:
            return "Your account is locked. Attempts: {0}".format(attempts)
        elif the_pass != password:
            attempts.append(the_pass)
            return "Incorrect password"
        elif amount > balance:
            return "Insufficient funds"
        else:
            balance -= amount
            return balance
    return account

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    pwd_verify = withdraw(0, old_password)
    if type(pwd_verify) not in [float, int]:
        return pwd_verify
    def joint_inner(the_money, pwd):
        if new_password == pwd:
            pwd = old_password
        return withdraw(the_money, pwd)
    return joint_inner

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balance = 0
        self.stocks = 0

    def vend(self):
        if self.stocks == 0:
            if self.balance == 0:
                return 'Machine is out of stock.'
            else:
                return 'Machine is out of stock. Here is your ${0}.'.format(self.balance)
        if self.price > self.balance:
            return 'You must deposit ${0} more.'.format(self.price - self.balance)
        else:
            self.stocks -= 1
            self.balance -= self.price
            if self.balance == 0:
                return 'Here is your {0}.'.format(self.name)
            else:
                balance = self.balance
                self.balance = 0
                return 'Here is your {0} and ${1} change.'.format(self.name, balance)

    def restock(self, number):
        self.stocks += number
        return 'Current {0} stock: {1}'.format(self.name, self.stocks)

    def deposit(self, money):
        self.balance += money
        if self.stocks == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(self.balance)
        return 'Current balance: ${0}'.format(self.balance)

    def restock(self, stocks):
        self.stocks += stocks
        return 'Current {0} stock: {1}'.format(self.name, self.stocks)

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, vendMachine):
        self.vendMachine = vendMachine

    def ask(self, message, *args):
        if "please" in message:
            call = message[7:]
            if hasattr(self.vendMachine, call):
                return getattr(self.vendMachine, call)(*args)
            else:
                return "Thanks for asking, but I know not how to {0}".format(call)
        else:
            return "You must learn to say please first."

