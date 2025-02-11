def fibonacci_recursive(previous: int, current: int, upto: int, print_output: bool = True) -> int:
    """
    This function calculates the fibonacci sequence up to a certain number using recursion.

    Args:
        previous (int): The previous number in the sequence
        current (int): The current number in the sequence
        upto (int): The number to calculate the fibonacci sequence up to
        print_output (bool): Whether to print the output of the fibonacci sequence
    
    Returns:
        int: The last number in the fibonacci sequence that is more than or equal to upto
    """
    if print_output:
        print(previous, current)
    if current >= upto:
        return current
    return fibonacci_recursive(current, current + previous, upto, print_output)


def fibonacci_loop(upto: int, print_output: bool = True) -> int:
    """
    This function calculates the fibonacci sequence up to a certain number using loops.

    Args:
        upto (int): The number to calculate the fibonacci sequence up to
        print_output (bool): Whether to print the output of the fibonacci sequence
    
    Returns:
        int: The last number in the fibonacci sequence that is more than or equal to upto
    """
    current = 1
    previous = 0
    for _ in range(upto):
        temp_prev = previous
        if print_output:
            print(previous, current)
        if current >= upto:
            return current
        previous = current
        current = current + temp_prev
        

if __name__ == "__main__":
    print("Loop")
    print(fibonacci_loop(1000000, False))

    print("Recursive")
    print(fibonacci_recursive(1, 1, 1000000, False))