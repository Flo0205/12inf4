from account import Account
from table import Table


def main():
    inString = input("How many players are playing? (1 - 4)  ")
    if inString.isnumeric():
        inNum = int(inString)
        if inNum > 0 and inNum < 5:
            # Spiel vorbereitung
            accounts = []
            for i in range(inNum):
                accounts.append(Account(i+1, 1000))
            gameover = False

            # Game loop
            while not gameover:
                acc: Account
                for acc in accounts:
                    acc.PayToPlay()

                table = Table(inNum)
                result = table.Play()
                for r in result:
                    acc = accounts[r-1]
                    acc.PayOut(result[r])
                
                for acc in accounts:
                    if acc.Balance == 0:
                        gameover = True
                
                printResult(accounts)

def printResult(accounts: list):
    acc: Account
    print("\n\n-----------------------")
    for acc in accounts:
        print(f"Player {acc.ID}: {acc.Balance}")
    print("-----------------------\n")

                

                


if __name__ == "__main__":
    main()