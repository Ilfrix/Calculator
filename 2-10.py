def convert_value(n):   #function for converting values from decimal to binary, return string
    new_n = ''
    for i in range(len(n)):
        tmp = bin(int(n[i]))[2:]
        if (len(tmp) != 4):
            tmp =(4 - len(tmp)) * '0' + tmp
        new_n += tmp
    return new_n

print("Enter two decimal numbers separated by a space \n\
the program will give you the answer in binary decimal form")
first, second = map(str, input().split())

first = convert_value(first)
second = convert_value(second)

#first number more or equel of length than second
if (len(first) < len(second)):
    first, second = second, first
second = (len(first) - len(second)) * '0' + second

#output start values
next_val = 0
new_val = ''
print("first value:\t", first)
print("second value:\t", second)

#summarize values
i = len(first) - 1
while i >= 0 or next_val > 0:
    if i >= 0:
        tmp = int(first[i]) + int(second[i]) + next_val
        i -= 1
    else:
        tmp = next_val
    next_val = tmp // 2
    new_val += str(tmp % 2)

#add zeroes if we have more digits, than after enter
new_val = new_val[::-1]
if (len(new_val) % 4 != 0):
    new_val = ((len(new_val) + 3) // 4 * 4 - len(new_val)) * '0' + new_val

#split our binary value into piece of 4
k = 0
tetr = ''
arr =[]
print("summ of values:\t", end = "")
for i in range(len(new_val)):
    if k % 4 == 0 and k > 1:
        print(' ', end="")
        arr.append(tetr)
        tetr = ''
    tetr += new_val[i]
    print(new_val[i], end ="")
    k += 1
if tetr != '':
    arr.append(tetr)


#delete values more 9(in decimal form) from answer
i = len(arr) - 1
next_val = 0
while i >= 0:
    tmp = int(arr[i],2) + next_val
    if (tmp > 9):
        tmp += 6
        next_val = tmp // 16
        tmp %= 16
    else:
        next_val = 0
    arr[i] = convert_value(str(tmp))
    i -= 1

#we has one more number digit
answer = []
if next_val > 0:
    answer.append(convert_value(str(next_val)))
answer = answer + arr

#output answer
print()
print("result is:\t", end="")
for i in range(len(answer)):
    print(answer[i], end=" ")


