def main():
    numb = [1,4,6,123,2,3,3,65,3]
    myRes = mySum(numb)
    res = sum(numb)
    print(f"res: {res} \nmyres: {myRes}")

    recRes = recursiveSum(numb, 0)
    print(f"recrusiver res: {recRes}")


def mySum(numb):
    total = 0
    for n in numb:
        total += n
    return total

def recursiveSum(numb, i):
    if i >= len(numb):
        return 0
    return numb[i] + recursiveSum(numb, i + 1)

if __name__ == "__main__":
    main()