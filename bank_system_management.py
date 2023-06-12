
class DBBL:

    def __init__(self) -> None:
        self.name = 'Dutch Bangla Bank Limited'
        self.users = []
        self.admins = []
        self.total_amount = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)


class User(DBBL):

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.total_balance = 0
        self.history = {}
        super().__init__()

    def diposit(self, amount, bank):
        if amount > 0:
            self.total_balance += amount
            bank.total_amount += amount
            self.history['diposit'] = amount
        else:
            print('Please give me valid amount')

        
    def withdraw(self, amount, bank):
        if bank.total_amount >= amount:
            if self.total_balance >= amount > 0:
                self.total_balance -= amount
                bank.total_amount -= amount
                self.history['withdraw'] = amount
            else:
                print('Please give me valid amount')
        else:
            print('Bank is  bankrupt')

    def check_balance(self):
        return self.total_balance
    
    def transfer_amount(self, user, amount):
        if self.total_balance >= amount > 0:
            user.total_balance += amount
            self.total_balance -= amount
            self.history['transfer'] = amount
        else:
            print('There is not enough money in the account')

    def check_history(self):

        for key, value in self.history.items():
            print(f'{key} : {value}')

    def take_loan(self, bank):
        if bank.loan_feature == True:
            amount = self.total_balance * 2
            if bank.total_amount >= amount:
                self.total_balance += amount
                bank.total_amount -= amount
                bank.total_loan_amount += amount
            else:
                print('Bank do not have enough money to give you')
        else:
            print('Currently loan feature is off')
        

class Admin(DBBL):

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        super().__init__()
    

    def check_total_available_balance(self, bank):
        return bank.total_amount
    
    def check_loan_amount(slef, bank):
        return bank.total_loan_amount
    
    def loan_feature_on(self, bank):
        bank.loan_feature = True

    def loan_feature_off(self, bank):
        bank.loan_feature = False


bank = DBBL()
user1 = User('shaha@gmail.com', 'Shaha')
bank.add_user(user1)
user2 = User('newaz@gmail.com', 'Newaz')
bank.add_user(user2)

admin1 = Admin('admin1@gmail.com', 'Admin1')
admin2 = Admin('admin2@gmail.com', 'Admin2')
bank.add_admin(admin1)
bank.add_admin(admin2)

user1.diposit(1200, bank)

# print(user1.check_balance())

user1.withdraw(500, bank)

user1.transfer_amount(user2, 500)

# print(user1.check_balance())
# print(user2.check_balance())

# user1.check_history()

# print(bank.total_amount)
# print(user1.check_balance())
# print(user2.check_balance())

# user1.take_loan(bank)

# print(bank.total_amount)
# print(user1.check_balance())
# print(bank.total_loan_amount)

print(admin1.check_total_available_balance(bank))
print(admin1.check_loan_amount(bank))

admin1.loan_feature_off(bank)

user1.take_loan(bank)

print(bank.total_amount)
print(user1.check_balance())
print(bank.total_loan_amount)





