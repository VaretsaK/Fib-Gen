from typing import Generator


def fibonacci_gen(n: int = 10) -> Generator[int, None, None]:
    """
    Generate Fibonacci sequence up to the nth number or up to a default value of 10.

    Args:
        n (int, optional): The number of Fibonacci numbers to generate. Defaults to 10.

    Yields:
        int: The next number in the Fibonacci sequence.

    Returns:
        Generator[int, None, None]: A generator object that yields Fibonacci numbers.
    """
    first_num, second_num = 0, 1
    counter: int = 0
    while counter <= n:
        counter += 1
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def main() -> None:
    """
    Main function to print Fibonacci numbers using fibonacci_gen generator.
    """
    for number in fibonacci_gen():
        print(number)


if __name__ == "__main__":
    main()
