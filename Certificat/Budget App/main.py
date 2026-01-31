class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withraw(self, amount, description=''):
        if self.check_founds(amount=amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
        
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    
    def transfer(self, amount, destination):
        if self.check_founds(amount=amount):
            self.withraw(amount=amount, description=f'Transfer to {destination.name}')
            destination.deposit(amount=amount, description=f'Transfer from {self.name}')
            return True
        return False
    
    def check_founds(self, amount):
        if amount > self.get_balance():
            return False
        return True
        
    def __str__(self):
        x = (30 - len(self.name)) // 2
        text =  '*'*x + self.name.capitalize() + '*'*x
        for dico in self.ledger:
            txt_size = 25 - len(dico['description'])
            if txt_size > 0 :
                text += f"\n{dico['description']:25}{dico['amount']}"
            else:
                text += f"\n{dico['description']:25}{dico['amount']}"

        text += f"\nTotal: {self.get_balance()}"
        return text

    
def create_spend_chart(categories: list):
    title = 'Percentage spent by category'
    spendings = {}

    for categorie in categories:
        spendings[categorie.name] = 0
        for ledg in categorie.ledger:
            if ledg['amount'] < 0:
                spendings[categorie.name] += -ledg['amount']
    
    # -----debug--------
    print(f"{'first print: spending ->':35}{spendings}")
    
    total_spending = sum(spendings.values())
    # -----debug-------
    print(f"{'second print: total_spending -> ':35}{total_spending}")
    
    # ------spendings by total spending----
    for key in spendings.keys():
        val = int((spendings[key] / total_spending)*100)
        spendings.update([(key, val)])
 
    chart = title
    print(spendings.values())
    for i in range(100, -1, -10):
        chart += f"\n{i:3}| "
        for key, value in spendings.items():
            if value >= i:
                chart += '0 '
                
    chart += f"\n{'-'*(len(spendings)*2)}\n{' '*5}"
    
    max_len = len(max([name for name in spendings.keys()], key=len))
    
    for i in range(max_len):
        pass
        for name in spendings.keys():
            pass
    return chart

c1 = Category('madjid')
c2 = Category('yahia')
c1.deposit(1000, 'deposit')
c1.withraw(500, 'withraw')
c1.transfer(300, c2)
c1.withraw(300, 'rani tchumert lzmlu drahem tout de suite')

c2.deposit(2000, 'deposit')
c2.withraw(700, 'withraw')
c2.withraw(300, 'rani tchumert lzmlu drahem tout de suite')
print(create_spend_chart([c1,c2]))
#print(c1)