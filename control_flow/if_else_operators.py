spam = 4
result = 2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2
print(result)

answer = 2 + 8 == spam or 2 + 1 == spam
print(answer)

# if else statement
username = "Mary"
password = "swordfish"
if username == "Mary":
    print("Hello, Mary")
else:
    print("Wrong name.")

# if elseif statement
def elseIfStatement():
    nameOne = "Alice"
    age = 33
    if nameOne == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    name = "Carol"
    age = 3000
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    elif age > 100:
        print("You are not Alice, grannie.")
    elif age > 2000:
        print("Unlike you, Alice is not an undead, immortal vampire.")

def elseInElifStatement():
    name = "Bob"
    if name == "Alice":
        print("Hi, Alice.")
    elif name == "John":
        print('Hi, John')
    else:
        print('No one is Bob')


elseIfStatement()
elseInElifStatement()
