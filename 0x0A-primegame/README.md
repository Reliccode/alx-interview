# Prime Game
</br>
<div align="center">
    <a href="#" style="background-color: #880808; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; margin-right: 10px;">Algorithm</a>
    <a href="#" style="background-color: #880808; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none;">Python</a>
</div>  
<br/><br/>




This project is a Python implementation of a competitive game scenario involving prime numbers and strategic decision-making. In this game, two players, Maria and Ben, take turns removing prime numbers and their multiples from a set of consecutive integers. The player who cannot make a move loses the game. The implementation allows for multiple rounds of the game, with different values of `n` for each round.

## Table of Contents

- [Overview](#overview)
- [Concepts](#concepts)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a Python function `isWinner(x, nums)` to determine the winner of each round of the prime game. The function takes the number of rounds `x` and an array of integers `nums`, where each integer represents the value of `n` for a round. It simulates the game, with Maria always going first and both players playing optimally. The function returns the name of the player who won the most rounds or `None` if the winner cannot be determined.

## Concepts

To understand and contribute to this project, familiarity with the following concepts is helpful:

- **Prime Numbers**: Understanding what prime numbers are and how to efficiently identify them within a range.
- **Sieve of Eratosthenes**: An efficient algorithm for finding all prime numbers up to a given limit, crucial for this task.
- **Game Theory**: Basic principles of competitive games, optimal play, win conditions, and strategies.
- **Dynamic Programming/Memoization**: Using previous results to make future calculations faster, potentially necessary for optimizing the solution.
- **Python Programming**: Proficiency in Python programming, including loops, conditional statements, arrays/lists, and adherence to PEP 8 style.

## Requirements

- Python 3.4.3 or later
- PEP 8 compliant style
- Ubuntu 20.04 LTS environment

## Usage

To use the `isWinner` function, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/alx-interview.git
    ```

2. Navigate to the project directory:

    ```bash
    cd alx-interview/0x0A-primegame
    ```

3. Execute the Python script containing the `isWinner` function:

    ```bash
    ./0-prime_game.py
    ```

## Example

Suppose we want to determine the winner of the prime game for 5 rounds with the following values of `n`: `[2, 5, 1, 4, 3]`. We can use the provided test script `main_0.py`:

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

Execute the script:

```bash
./main_0.py
```

Output:
```
Winner: Ben
```

## Contributing

Contributions to this project are welcome. If you have suggestions for improvements or would like to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Author

- **Your Name**
- GitHub: [Your GitHub Username](https://github.com/your_username)
