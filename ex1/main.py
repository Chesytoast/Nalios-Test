def main():
    # fizzBuzz()
    # words = {'3': 'Fizz', '5' : 'Buzz',}
    # fizzBuzzBonus(words)
    fizzBuzzBonus({
            '4': 'Fizz',
            '9': 'Buzz',
            '12': 'Lazz'
        })

def fizzBuzz():
    for n in range(1,101):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

#Bonus made after the 2 hours

def fizzBuzzBonus(words):
    for n in range(1,101):
        output = ''
        for key,value in words.items():
            if n % int(key) == 0:
                output += value
        if not output:
            output = n
        print(output)

if __name__ == "__main__":
    main()