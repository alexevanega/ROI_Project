class Item():
    def __init__(self, source, amt):
        self.source = source
        self.amount = amt
        self.next = None

class linkedItems():
    def __init__(self):
        self.start = None

    def addItem(self, source, amt):
        new_item = Item(source,amt)
        if self.start is None:
            self.start = new_item
        else:
            income = self.start
            while income.next:
                income = income.next
            income.next = new_item

    def listOffItems(self):
        temp = self.start
        while temp:
            print(f'{temp.source}: ${temp.amount}')
            temp = temp.next

    def removeItem(self, incomeitem):
        temp = self.start
        while temp.source is not incomeitem:
           prev = temp
           temp = temp.next
        if temp.next is not None:
            temp.source = temp.next.source
            temp.amount = temp.next.amount
            temp.next = temp.next.next
        else:
            prev.next = None

    def totalItem(self):
        temp = self.start
        total = 0
        while temp is not None:
            total += temp.amount
            temp = temp.next
        return total
