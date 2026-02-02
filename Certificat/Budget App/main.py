class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=str()):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=str()):
        if self.check_funds(amount=amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    
    def transfer(self, amount, destination):
        if self.check_funds(amount=amount):
            self.withdraw(amount=amount, description=f'Transfer to {destination.name}')
            destination.deposit(amount=amount, description=f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
        
    def __str__(self):
        text = f"{self.name.title():*^30}\n"
        for dico in self.ledger:
            description = dico['description'][:23]
            amount = dico['amount']
            text += f"{description:<23}{amount:>7.2f}\n"    
        text += f"Total: {self.get_balance()}"
        return text


    
def create_spend_chart(categories: list):
    title = 'Percentage spent by category'
    spendings = {}

    for categorie in categories:
        spendings[categorie.name] = 0
        for ledg in categorie.ledger:
            if ledg['amount'] < 0:
                spendings[categorie.name] += -ledg['amount']

    total_spending = sum(spendings.values())

    # ------spendings by total spending----
    for key in spendings.keys():
        val = (spendings[key] / total_spending)*100
        spendings.update([(key, val)])
        
    chart = title
    for i in range(100, -1, -10):
        chart += f"\n{i:3}| "
        for key, value in spendings.items():
            if value >= round(i, -1):
                chart += 'o  '
            else:
                chart += '   '
                
    chart += f"\n{' '*4}{'-'*(len(spendings)*3+1)}"
    
    max_len = len(max([name for name in spendings.keys()], key=len))
    
    for i in range(max_len):
        chart += '\n'+ ' '*5
        for name in spendings.keys():
            if i <= len(name) - 1:
                chart += f"{name[i]:3}"
            else:
                chart += '   '
    return chart

c1 = Category('madjid')
c1.deposit(1000, 'deposit')
c1.withdraw(500.34, 'withdraw')
c1.withdraw(200.82, 'second withdraw')

c2 = Category('yahia')
c2.deposit(2000, 'deposit')
c2.withdraw(800.34, 'withdraw')
c2.withdraw(600.82, 'second withdraw')

print(c1)
print(create_spend_chart([c1, c2]))