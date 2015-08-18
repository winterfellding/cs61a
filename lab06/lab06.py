## Object-Oriented Programming ##

# Q2
class Person(object):
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat()       # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"
        self.speaking = 'I squirreled it away before it could catch on fire.'

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.speaking = stuff
        return stuff

    def ask(self, stuff):
        self.speaking = "Would you please " + stuff
        return self.say("Would you please " + stuff)

    def greet(self):
        self.speaking = "Hello, my name is " + self.name
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.speaking

# Q3
class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        "*** YOUR CODE HERE ***"
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"

        if amount > self.balance:
            return 'Insufficient funds'
        self.transactions.append(('withdraw', amount))
        self.balance = self.balance - amount
        return self.balance

# Q4
class BadBankAccount(Account):
    """ A subclass of bank account that allows an account holder to overdraw
    once, and then prevents them from withdrawing more money. You should also
    implement the property method overdrawn, which allows an account holder to
    check if they are overdrawn.

    >>> harold_account = BadBankAccount('Harold')
    >>> harold_account.deposit(100)   # depositing my paycheck for the week
    100
    >>> harold_account.withdraw(101)  # buying dinner
    -1
    >>> harold_account.overdrawn
    True
    >>> harold_account.withdraw(100000)
    You have overdrawn, please add more money!
    -1
    >>> harold_account.deposit(10)
    9
    >>> harold_account.overdrawn
    False
    """

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"
        if self.overdrawn:
            print('You have overdrawn, please add more money!')
            return self.balance
        else:
            self.balance = self.balance - amount
            if self.balance < 0:
                self.overdrawn = True
            return self.balance

    "*** YOUR CODE HERE ***"
    def __init__(self, holder):
        super(BadBankAccount, self).__init__(holder)
        self.overdrawn = False

    def deposit(self, amount):
        self.balance = super(BadBankAccount, self).deposit(amount)
        if self.balance > 0:
            self.overdrawn = False
        return self.balance
