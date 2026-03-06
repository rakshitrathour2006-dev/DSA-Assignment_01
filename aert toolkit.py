# Part A: Stack ADT

class StackADT:

    def __init__(self):
        self.stack = []   # storage for stack elements

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def run_stack_test():

    print("Part A: Stack Test")

    s = StackADT()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack size:", s.size())
    print("Top element:", s.peek())

    print("Pop:", s.pop())
    print("Pop:", s.pop())

    print("Stack size after pops:", s.size())
    print("Is stack empty?", s.is_empty())


# Part B: Factorial

def factorial(n):

    if n < 0:
        return "Invalid input"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Fibonacci naive

naive_counter = 0

def fib_naive(n):

    global naive_counter
    naive_counter += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


# Fibonacci with memoization

memo_counter = 0

def fib_memo(n, memo=None):

    global memo_counter
    memo_counter += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


def run_part_b_tests():

    print("\nPart B: Factorial Tests")

    numbers = [0, 1, 5, 10]

    for num in numbers:
        print("factorial(", num, ") =", factorial(num))

    print("\nPart B: Fibonacci Tests")

    fib_values = [5, 10, 20, 30]

    for n in fib_values:

        global naive_counter, memo_counter

        naive_counter = 0
        naive_result = fib_naive(n)

        memo_counter = 0
        memo_result = fib_memo(n, {})

        print("\nFibonacci n =", n)
        print("Naive result:", naive_result, "Calls:", naive_counter)
        print("Memo result:", memo_result, "Calls:", memo_counter)


# Part C: Tower of Hanoi

def hanoi(n, source, helper, target, move_stack):

    if n == 1:
        step = "Move disk 1 from " + source + " to " + target
        print(step)
        move_stack.push(step)
        return

    hanoi(n - 1, source, target, helper, move_stack)

    step = "Move disk " + str(n) + " from " + source + " to " + target
    print(step)
    move_stack.push(step)

    hanoi(n - 1, helper, source, target, move_stack)


def run_part_c():

    print("\nPart C: Tower of Hanoi (N = 3)")

    moves = StackADT()

    hanoi(3, "A", "B", "C", moves)

    print("Total moves:", moves.size())


# Part D: Recursive Binary Search

def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    if key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    return binary_search(arr, key, mid + 1, high)


def run_part_d():

    print("\nPart D: Binary Search Tests")

    data = [1, 3, 5, 7, 9, 11, 13]

    values = [7, 1, 13, 2]

    for val in values:
        idx = binary_search(data, val, 0, len(data) - 1)
        print("Search", val, "→ Index:", idx)

    empty_arr = []
    result = binary_search(empty_arr, 5, 0, len(empty_arr) - 1)

    print("Search in empty array → Index:", result)


# Main Program

if __name__ == "__main__":

    run_stack_test()   # Part A
    run_part_b_tests() # Part B
    run_part_c()       # Part C
    run_part_d()       # Part D
