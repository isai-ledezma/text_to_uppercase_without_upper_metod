def find_label(letra):
    abc = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['g', 'G'], ['h', 'H'], ['i', 'I'],
           ['j', 'J'], ['k', 'K'], ['l', 'L'], ['m', 'M'], ['n', 'N'], ['ñ', 'Ñ'], ['o', 'O'], ['p', 'P'], ['q', 'Q'],
           ['r', 'R'], ['s', 'S'], ['t', 'T'], ['u', 'U'], ['v', 'V'], ['w', 'W'], ['x', 'X'], ['y', 'Y'], ['z', 'Z']]
    for label in abc:
        if letra == label[0]:
            letra = label[1]
            return letra
    return letra


def mayus(str):
    up_str = ''
    for letra in str:
        up_str = up_str + find_label(letra)
   
    return up_str


def main():
    print(mayus(input('give me the text:')))


if __name__ == '__main__':
    main()
