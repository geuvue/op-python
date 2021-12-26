from os import system

def list_sort(ss):
    for i in range (len(ss) - 1):
        for j in range (len(ss) - i - 1):
            if len(ss[j]) > len(ss[j + 1]):
                (ss[j], ss[j + 1]) = (ss[j + 1], ss[j])

def list_out(ss):
    for i in range (len(ss)):
        print(ss[i], "\t(", len(ss[i]), ")")
    print("\n")

def main():
    s = input("\nEnter some words: ")
    ss = s.split(" ")
    print("\nUnsorted list of words: ")
    list_out(ss)
    list_sort(ss)
    print("Sorted list of words: ")
    list_out(ss)

if __name__ == '__main__':
    main()
    system('pause')