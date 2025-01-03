n = int(input())
phone_numbers = [input() for _ in range(n)]

prefix = phone_numbers[0]
for number in phone_numbers[1:]:
    i = 0
    while i < len(prefix) and i < len(number) and prefix[i] == number[i]:
        i += 1
    prefix = prefix[:i]

print(len(prefix))
