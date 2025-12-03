
MAX_DIAL = 99
MIN_DIAL = 0
DIAL_RANGE = 100
FILE_PATH = "input.txt"


def main():
    zero_counter = 0
    current_pos = 50

    with open(FILE_PATH, "r") as file:
        for line in file:
            line = line.strip()
            print(line)

            if isinstance(current_pos, int):
                current_pos = move(current_pos, line)
            elif isinstance(current_pos, tuple):
                current_pos = move(current_pos[1], line)
            print(type(current_pos))
            print(current_pos)
            if isinstance(current_pos, (tuple)):
                if current_pos[1] == True :
                    zero_counter += 1
            elif isinstance(current_pos, int):
                if current_pos == 0:
                    zero_counter += 1

    print("count", zero_counter)


def move(pos: int, instruction: str) -> int | tuple:
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction == "L":
        if pos - distance < 0:
            value = (pos - distance) % DIAL_RANGE
            return value, True
        else:
            return (pos - distance) % DIAL_RANGE
    elif direction == "R":
        if pos - distance > 99:
            value = (pos + distance) % DIAL_RANGE
            return value, True
        return (pos + distance) % DIAL_RANGE
    else:
        raise ValueError("Invalid direction")


main()
