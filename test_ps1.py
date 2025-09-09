# test_ps1.py
# Test 8-Puzzle Solutions
# Created for CSI 480 @ Champlain College by David Kopec
import unittest
import ps1


class EightPuzzleTestCase(unittest.TestCase):
    def check_move(self, board1, board2):
        # find the zero in each
        for row in range(3):
            for col in range(3):
                if board1[row][col] == 0:
                    row1, col1 = row, col
                if board2[row][col] == 0:
                    row2, col2 = row, col
        # check that they are one move away
        self.assertEqual(abs(row1 - row2) + abs(col1 - col2), 1)
        # check that the rest of the boards, excluding the zero, is the same
        for row in range(3):
            for col in range(3):
                if not ((row == row1 and col == col1) or (row == row2 and col == col2)):
                    self.assertEqual(board1[row][col], board2[row][col])

    def check_solution(self, solution, start_state_board, expected_length):
        # Check solution is the minimum number of steps
        self.assertEqual(len(solution), expected_length)
        # Check starts with the right state
        self.assertEqual(solution[0].board, start_state_board)
        # Check each state is a legal successor of the previous state
        for i in range(1, len(solution)):
            self.check_move(solution[i - 1].board, solution[i].board)
        # Check ends in goal state board
        self.assertEqual(solution[-1].board, ps1.EightPuzzleState.GOAL_BOARD)

    def test_easy_puzzle1(self):
        puzzle = "123450786"
        start_state_board = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
        solution = ps1.solution(puzzle)
        self.check_solution(solution, start_state_board, 2)

    def test_easy_puzzle2(self):
        puzzle = "123406758"
        start_state_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        solution = ps1.solution(puzzle)
        self.check_solution(solution, start_state_board, 3)

    def test_medium_puzzle(self):
        puzzle = "150432786"
        start_state_board = [[1, 5, 0], [4, 3, 2], [7, 8, 6]]
        solution = ps1.solution(puzzle)
        self.check_solution(solution, start_state_board, 7)

    def test_hard_puzzle(self):
        puzzle = "430827615"
        start_state_board = [[4, 3, 0], [8, 2, 7], [6, 1, 5]]
        solution = ps1.solution(puzzle)
        self.check_solution(solution, start_state_board, 23)


if __name__ == "__main__":
    unittest.main()
