# Show on the screen the list of all even numbers from 0 to 100.
# ==============================================================

def even_numbers(start : int, end : int) -> int:
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

if __name__ == '__main__':
    for number in even_numbers(0, 100):
        print(number)