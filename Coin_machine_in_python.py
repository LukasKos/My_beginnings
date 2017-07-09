guess = int(raw_input("Select the amount of money: "))

def change(coin):
    print '50', guess / 50
    print '20', (guess % 50) / 20
    print '10', ((guess % 50) % 20) / 10
    print ' 5', (((guess % 50) % 20) % 10) / 5
    print ' 2', ((((guess % 50) % 20) % 10) % 5) / 2
    print ' 1', (((((guess % 50) % 20) % 10) % 5) % 2) / 1

change(guess)
