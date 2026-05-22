class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
   
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
       
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': 0 - amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for l in self.ledger:
            self.balance += l['amount']
        return float(self.balance)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
   
    def __str__(self):
        full_string = ''
        stars = '*' * ((30 - len(self.name)) // 2)
        full_string += f'{stars}{self.name}{stars}\n'
   
        for entery in self.ledger:
            #print the description
            entry_description = len(entery['description']) if len(entery['description']) < 23 else 23
            entry_description_string = f"{entery['description'][:entry_description]}{' ' * (23 - entry_description)}"

            #print the amount
            amount = entery['amount']
            float_amount = f'{float(amount):.2f}'
            entry_amount = len(float_amount) if len(float_amount) < 7 else 7
            entry_amount_string = f"{' ' * (7 - entry_amount)}{float_amount[:entry_amount]}"
            full_string += f'{entry_description_string}{entry_amount_string}\n'
   
        full_string += f'Total: {self.get_balance():.2f}'
        return full_string
   
def create_spend_chart(categories):    
    total_spent = 0
    totals = {}
    percentages = {}
    for category in categories:
        totals[category.name] = 0
        for l in category.ledger:
            if l['amount'] < 0:
                total_spent += l['amount']
                totals[category.name] += l['amount']
   
    for name, amount in totals.items():
        percentages[name] = (amount / total_spent * 100) // 10 * 10

    numbers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    full_string = 'Percentage spent by category\n'
    for n in numbers:
        spaces = ' ' * (3 - len(str(n)))
        nstring = f"{spaces}{n}" if len(str(n)) <= 3 else str(n)
        full_string += f'{nstring}|'
        for name, percentage in percentages.items():
            if percentage >= n:
                full_string += ' o '
            else:
                full_string += '   '
        full_string += ' \n'


    names = [c.name for c in categories]
    max_length = len(max(names, key=len))
    names_with_spaces = []
    
    full_string += '    -'

    for c in categories:
         full_string += '-' * 3 

    for n in names:
        names_with_spaces.append(f'{n}{" " * (max_length - len(n))}')  

    full_string += "\n" 

    for index1 in range(max_length):
        for index2 in range(len(names_with_spaces)):
            if index2 == 0:
                full_string += '     '
            full_string += f'{names_with_spaces[index2][index1]}  '
        if index1 < max_length - 1:
            full_string += '\n'
    return full_string

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(10.15, 'gas')

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(1.15, 'groceries')
food.withdraw(10.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(20, 'shirt')

categories = [food, clothing, auto]

print(create_spend_chart(categories))