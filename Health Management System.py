def getdate():
    import datetime
    return datetime.datetime.now()


def take(k):
    if k==1:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c==1:
            value = input("type here\n")
            with open("Priya ex.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + f"{value} \n")
            print("successfully written")
        elif c==2:
            value = input("type here\n")
            with open("Priya-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + f"{value} \n")
            print("successfully written")
    elif k==2:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c == 1:
            value = input("type here\n")
            with open("Mohit-ex.txt") as f:
                f.write(str([str(getdate())]) + ": " + f"{value} \n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Mohit-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + f"{value} \n")
            print("successfully written")
    elif k==3:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c == 1:
            value = input("type here\n")
            with open("Ashutosh-ex.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + f"{value} \n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Ashutosh-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid number")
def retrieve(k):
    if k==1:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c == 1:
            with open("Priya ex.txt") as f:
                for i in f:
                    print(i, end=" ")

        elif c == 2:
            with open("Priya-food.txt", "a") as f:
                for i in f:
                    print(i, end=" ")

    if k==2:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c == 1:
            with open("Mohit-ex.txt") as f:
                for i in f:
                    print(i, end=" ")

        elif c == 2:
            with open("Mohit-food.txt") as f:
                for i in f:
                    print(i, end=" ")

    if k==3:
        c = int(input("enter 1 for excercise and 2 for food: "))
        if c == 1:
            with open("Ashutosh-ex.txt") as f:
                for i in f:
                    print(i, end=" ")

        elif c == 2:
            with open("Ashutosh-food.txt") as f:
                for i in f:
                    print(i, end=" ")



print("Health Management System")
a = int(input("enter 1 for log the value and 2 for retrieve the value: "))
if a==1:
    b = int(input("enter 1 for Priya, 2 for Mohit and 3 for Ashutosh: "))
    take(b)
elif a==2:
    b = int(input("enter 1 for Priya, 2 for Mohit and 3 for Ashutosh: "))
    retrieve(b)

else:
    print("plz enter valid number")
