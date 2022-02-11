import random
from copy import copy

class PuzzlePiece():
    def __init__(self, _character, _position, _is_message, _sides):
        self.character = _character
        self.position = _position
        self.is_message = _is_message
        self.sides = _sides

        self.top = _sides["top"]
        self.right = _sides["right"]
        self.bottom = _sides["bottom"]
        self.left = _sides["left"]

def main():
    generator()

def generator():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    test_case_max_count = 1024

    for test_case_counter in range(test_case_max_count):
        m = random.randrange(5, 64)
        n = random.randrange(5, 64)

        message = ""

        message_len = random.randrange(4, min(m, n))

        for i in range(message_len):
            message += alphabet[random.randint(0, 25)]

        puzzle = [[None for _ in range(n)] for _ in range(m)]

        puzzle_pieces = []

        orientation = random.randrange(0, 2)
        orientation_dimension_max = [m, n][orientation]

        initial_position = [0, 0]
        initial_position[orientation] = random.randrange(0, orientation_dimension_max - message_len + 2)
        initial_position[1 - orientation] = random.randrange(0, [m, n][1 - orientation])

        message_positions = [[0,0] for c in range(message_len)]

        for c in range(message_len):
            message_positions[c][orientation] = initial_position[orientation] + c
            message_positions[c][1 - orientation] = initial_position[1 - orientation]

        for i in range(m):
            for j in range(n):
                position = [i, j]

                character = message[position[orientation] - initial_position[orientation]]\
                    if position in message_positions else "-"

                sides = {
                    "top": 0,
                    "right": 0,
                    "bottom": 0,
                    "left": 0
                }

                if i == 0:
                    sides["left"] = 0

                    sides["right"] = random.randrange(1, 4)
                elif i == (m - 1):
                    sides["right"] = 0

                    sides["left"] = random.randrange(1, 4)
                else:
                    side_pair_left = puzzle[i - 1][j].right
                    sides["left"] = 4 - side_pair_left

                    try:
                        side_pair_right = puzzle[i + 1][j].left
                        sides["right"] = 4 - side_pair_right
                    except AttributeError:
                        sides["right"] = random.randrange(1, 4)

                if j == 0:
                    sides["top"] = 0

                    sides["bottom"] = random.randrange(1, 4)
                elif j == (n - 1):
                    sides["bottom"] = 0

                    sides["top"] = random.randrange(1, 4)
                else:
                    side_pair_top = puzzle[i][j - 1].bottom
                    sides["top"] = 4 - side_pair_top

                    try:
                        side_pair_bottom = puzzle[i][j + 1].top
                        sides["bottom"] = 4 - side_pair_bottom
                    except AttributeError:
                        sides["bottom"] = random.randrange(1, 4)

                puzzle_piece = PuzzlePiece(character, position, position in message_positions, sides)

                puzzle[i][j] = puzzle_piece

                puzzle_pieces.append(puzzle_piece)

        random.shuffle(puzzle_pieces)

        test_case_number = str(test_case_counter).zfill(4)

        input_file = open("../Puzzles/puzzlecryptosystem_test_cases/input/input{}.txt".format(test_case_number), "w")

        puzzle_piece_strings = [str(m), str(n)] + ["{} {} {} {} {}".format(piece.character, piece.top, piece.right, piece.bottom, piece.left) for piece in puzzle_pieces]

        input_file.writelines("\n".join(puzzle_piece_strings))

        output_file = open("../Puzzles/puzzlecryptosystem_test_cases/output/output{}.txt".format(test_case_number), "w")

        output_file.writelines(message)

        test_case_counter += 1

        print("{}/{} test cases generated".format(test_case_counter, test_case_max_count))

    return

def generator_mass():
    return

def generator_cmd():
    return

main()