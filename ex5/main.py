def main():
    numb = [1,4,6,123,2,3,3,65,3]
    myRes = mySum(numb)
    res = sum(numb)
    print(f"res: {res} \n myres: {myRes}")

def mySum(numb):
    total = 0
    for n in numb:
        total += n
    return total

if __name__ == "__main__":
    main()