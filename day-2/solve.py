total = 0
chall_input = open("./input.txt")
chall_input=chall_input.read().split(",")
clean_input = []
for element in chall_input:
    element=element.split("-")
    clean_input.append(element)
print(clean_input)

for sublist in clean_input:
    for number in range(int(sublist[0]), int(sublist[1])):
        if len(str(number)) % 2 == 0: # issue probably here
            number_string = str(number)
            length = len(number_string)
            half_point = length / 2
            half_point = int(half_point)
            check1 = number_string[:half_point]
            print("check1", check1)
            check2 = number_string[half_point: length]
            print("check2", check2)

            if check1 == check2:
                total += number
                print("good case, num added")



print(total)
