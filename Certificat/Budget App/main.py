class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withraw(self, amount, description=''):
        if self.check_founds:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    
    def transfer(self, amount, destination):
        if self.withraw(amount=amount, description=f'Transfer to {destination.name}'):
            destination.deposit(amount=amount, description=f'Transfer from {self.name}')
            return True
        return False
    
    def check_founds(self, amount):
        if amount > self.get_balance():
            return False
        True
        
    def __str__(self):
        x = (30 - len(self.name)) // 2
        string =  '*'*x + self.name.capitalize() + '*'*x
        for dico in self.ledger:    
            pass

    
def create_spend_chart(categories):
    pass
c1 = Category('madjid')
print(c1)