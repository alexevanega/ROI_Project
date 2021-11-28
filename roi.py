import linked_lists

def Validate(response):
    if response == "Quit":
        return 'kill code'
    elif response.isdigit():
        print(f'{response} is not a valid response.')
        return True
    else:
        return response


def getSourceofIncome():
    source = input('Enter Income Source\n(enter "stop" when you are finished): ').title()
    if source.isdigit():
        print(f'{source} is not a valid response.')
        return getSourceofIncome()
    else:
        return source


def getExpense():
    expense = input('Enter Expense\n(enter "stop" when you are finished): ').title()
    if expense.isdigit():
        print(f'{expense} is not a valid response.')
        return getExpense()
    else:
        return expense

def getInvestment():
    investment = input('Enter investment\n(enter "stop" when you are finished): ').title()
    if investment.isdigit():
        print(f'{investment} is not a valid response.')
        return getInvestment()
    else:
        return investment

def getSourceAmount(source):
    amt = input(f'Amount for {source}? $').lower()
    if amt == 'quit':
        return 'Quit'
    elif amt.isdigit():
        return int(amt)
    else:
        print(f'{amt} is not a valid response. Please enter a response in the form of a number.')
        return getSourceAmount(source)

def getCashFlow(income,expense):
    totalCashFlow = income - expense
    return totalCashFlow

def CalculateROI(cshflw,ttlinv):
    annlcshflw = cshflw *12
    if annlcshflw == 0:
        return f'Your calculated Return on Investment is {0}%'
    if ttlinv == 0:
        return f'Error: Cannot calculate Return on Investment when total investment is ${0}'
    ROI = annlcshflw/ttlinv
    ROI *= 100
    return f'Your calculated Return on Investment is {ROI}%'

def verify():
    ask = input('Would you like to recalculate?(Y/N) ').lower()
    if ask == 'y' or ask == 'n':
        return ask
    else:
        return verify()

def ROI():
    kill = 'Quit'
    income = linked_lists.linkedItems()
    expense = linked_lists.linkedItems()
    investement = linked_lists.linkedItems()
    start = input('Welcome to the Return on Investment simulation! Press Enter to continue\n'
    '(Enter "quit" at any point in the simulation to exit.)')
    if start.title() == kill:
        return
    else:
        while True:
            while True:      
                inc = getSourceofIncome()
                if inc == kill:
                    return kill
                elif inc == 'Stop':
                    break
                incamt = getSourceAmount(inc)
                if incamt == kill:
                    return kill
                income.addItem(inc,incamt)
            income.listOffItems()
            print(f'Your total income is ${income.totalItem()}')
        
            
            while True:
                exp = getExpense()
                if exp == kill:
                    return kill
                elif exp == 'Stop':
                    break
                expamt = getSourceAmount(exp)
                if expamt == kill:
                    return kill
                expense.addItem(exp,expamt)
            expense.listOffItems()
            print(f'Your total expense is ${expense.totalItem()}')

            while True:
                inv = getInvestment()
                if inv == kill:
                    return kill
                elif inv == 'Stop':
                    break
                invamt = getSourceAmount(inv)
                if invamt == kill:
                    return kill
                investement.addItem(inv,invamt)
            investement.listOffItems()
            print(f'Your total investment is ${investement.totalItem()}') 
        
            totalincome = income.totalItem()
            totalexpense = expense.totalItem()
            totalinvestment = investement.totalItem()

            cshflw = getCashFlow(totalincome,totalexpense)

            print(CalculateROI(cshflw,totalinvestment))
            if verify() == 'y':
                continue
            else:
                print(f'Thank you for using the Return on Investment tool! Goodbye')
                return kill

ROI()   



