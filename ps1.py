# ps1.py
# Solve 8-puzzle problems using A*
# Created for CSI 480 @ Champlain College
# Starter Code by David Kopec
# Completed by:
from __future__ import annotations
from generic_search import astar, node_to_path  # you need both of these
from copy import deepcopy  # for copying boards to avoid mutation


class EightPuzzleState:
    """
    The state of the 8-puzzle.
    """
    GOAL_BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def __init__(self, board: list[list[int]]):
        self.board = board
        # YOUR CODE HERE - if you would like additional initialization code

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))
    
    def __str__(self) -> str:
        """
        Return string representation of this EightPuzzleState nicely.
        """
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])
    
    def __repr__(self) -> str:
        """
        Return a string representation of this EightPuzzleState as a single line string with no spaces
        """
        return "".join([str(x) for row in self.board for x in row])

# YOUR CODE HERE — add additional methods or functions


def solution(puzzle_description: str) -> list[EightPuzzleState]:
    """
    Find the list of EightPuzzleStates that leads to a solution.
    puzzle_description: a string describing the puzzle to solve in the form 123450786 where 0 is the blank space, and it is assumed that each row is 3 characters long.
    """
    # YOUR CODE HERE


if __name__ == "__main__":
    # This is just an example puzzle with 1 move away;
    # There are more examples in the unit tests and of course
    # you can construct your own.
    # Feel free to change this __main__ area
    # You will be graded on the unit tests, not this
    sol = solution("123450786")
    for i, state in enumerate(sol):
        print(f"State {i}")
        print(state)
    print(f"{len(sol)} states in solution")