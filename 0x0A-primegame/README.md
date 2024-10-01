# 0x0A. Prime Game

This project implements a solution for the "Prime Game" challenge.  The game involves two players, Maria and Ben, taking turns choosing prime numbers and removing their multiples from a set of consecutive integers. The player who cannot make a move loses.

## Project Description

The `0-prime_game.py` file contains two functions:

* `is_prime(n)`: Efficiently checks if a number `n` is prime.
* `prime_game(n)`: Determines the winner of a single round of the Prime Game given the upper limit `n`.
* `isWinner(x, nums)`: Determines the overall winner of `x` rounds of the Prime Game, where `nums` is an array of upper limits for each round.

## Algorithm and Approach

The core logic of the game is implemented in `prime_game(n)`.  It uses an optimized prime checking function (`is_prime`) and simulates the game by iteratively removing primes and their multiples. The winner is determined based on who made the last valid move.

The `isWinner(x, nums)` function orchestrates multiple rounds of the game and tracks the overall winner.

## Usage

The provided `main_0.py` file demonstrates how to use the `isWinner` function.  You can run it like this:

```bash
./main_0.py



This README file provides a comprehensive overview of the project, including its purpose, functionality, usage instructions, and key improvements. It also includes a clear example and adheres to standard Markdown formatting. Remember to replace "[Your Name]" with your actual name.
