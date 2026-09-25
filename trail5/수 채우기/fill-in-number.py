n = int(input())

# Please write your code here.
money = n % 5
five = n // 5

if money % 2 == 0:
    print(five+money//2)
    exit(0)

else:
    while five > 0:
        money += 5
        five -= 1

        if money % 2 == 0:
            print(five+money//2)
            exit(0)
    else:
        print(-1)