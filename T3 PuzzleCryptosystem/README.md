# Task #3 - Puzzle Cryptosystem

## Problem Statement
You and your friend have come up with a cryptography puzzle game! Here’s how the game goes:

1. Your friend picks two numbers `4 < m <= 64` and `4 < n <= 64`, to be the number of rows and columns of a puzzle.
2. Your friend chooses a word or phrase of length `4 <= l < min(m, n)` such that it can be completely inscribed along a single row or a single column.
3. Your friend magically creates a puzzle board of size `m`-by-`n` with random pieces. Every piece follows four basic rules:
- Each puzzle piece has four sides
- Each side can be of type 0, 1, 2, 3, or 4
- Sides along the outside of the puzzle are all type 0
- Sides of type n can only pair with sides of type `4 - n`
4. Your friend writes the word they chose vertically or horizontally somewhere in the puzzle with one letter per puzzle piece.
5. Your friend writes a dashed line (`-`) on pieces that do not already have a letter.
6. Your friend scrambles all the puzzle pieces and hands them to you to put together.
7. Once you have put the puzzle together, you must find the word in the puzzle. This is the original message.

Write a program which, given the numbers `m` and `n` and a list of pieces with their inscribed character and each of their sides, outputs the hidden word or phrase.

## Input Format
```
m
n
character top right bottom left
```

The first line contains `m`. The second line contains `n`. Subsequent lines start with the character (either an alphanumeric character or a dash for empty pieces), then have the side type in the order of top, right, bottom, and left.

## Output Format
```
keyword
```

## Constraints
```
4 < m <= 64
4 < n <= 64
4 <= l < min(m, n)
```


