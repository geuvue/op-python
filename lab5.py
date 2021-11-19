from math import log10

def main():
    n = int(input("Enter n "))
    i = 1
    for i in range(n+1):
        ost = i % 10
        if ost == 5 or ost == 6 or ost == 1:
            i1 = i * i
            lg = int(1 + log10(i))
            biss = 10**lg
            diff = (i1 - i) % biss
            if (diff == 0):
                print(i, " ", i1)
        i = i + 1
        
main()
