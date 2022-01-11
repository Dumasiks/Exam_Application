# write your code here
import random, operator


def check():  
    while ValueError:
        try:
            answ = int(input())
        except ValueError:
            print("Incorrect format.")
        else:
            return answ


def finals():
    yes = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.\n")
    if yes in ["yes", "y", "YES", "Yes"]:
        name = input("What is your name?\n")
        my_file = open("results.txt", "a")
        description = one if level == "1" else two
        my_file.writelines("\n" + f"{name}: {mark}/5 in level {level} ({description})")
        my_file.close()
        print("The results are saved in \"results.txt\"")


tasks = 5
mark = 0
one = "simple operations with numbers 2-9"
two = "integral squares of 11-29"
level = input("Which level do you want? Enter a number:"
              "1 - simple operations with numbers 2-9"
              "2 - integral squares of 11-29\n")
if level == "1":
    while tasks != 0:
        n1 = random.randint(2, 9)
        n2 = random.randint(2, 9)
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }
        ops_key = list(ops.keys())
        ops_values = list(ops.values())
        chosen = random.choice(ops_values)
        print(f"{n1} {ops_key[ops_values.index(chosen)]} {n2}")
        result = chosen(n1, n2)
        answer = check()
        if answer == result:
            print("Right!")
            mark += 1
            tasks -= 1
        else:
            print("Wrong!")
            tasks -= 1
elif level == "2":
    while tasks != 0:
        n = random.randint(11, 29)
        result = n ** 2
        print(n)
        answer = check()
        if answer == result:
            print("Right!")
            mark += 1
            tasks -= 1
        else:
            print("Wrong!")
            tasks -= 1
else:
    print("Incorrect format.")

finals()
