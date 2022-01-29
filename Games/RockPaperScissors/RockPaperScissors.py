from hand import Hand


def main():
    p1 = Hand(1)
    p2 = Hand(2)

    res1 = p1.rps()
    res2 = p2.rps()

    if res1 == res2:
        print("It's a draw!")
    elif res1 == 'rock':
        if res2 == 'scissors':
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif res1 == 'paper':
        if res2 == 'rock':
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif res1 == 'scissors':
        if res2 == 'paper':
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    else:
        print(f"What have you done?!?  {res1}  {res2}")


def credits():
    print("Made by Flo0205")
    print("Thanks to wynand1004 for the ASCII Art")
    print("https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe")
    print("---------------------------------------------------------------------\n")


if __name__ == "__main__":
    credits()
    main()
