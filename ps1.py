# ps1.py
# Solve 8-puzzle problems using A*
# Created for CSI 480 @ Champlain College
# Starter Code by David Kopec
# Completed by: Your Name

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

    # --- Additional methods for A* ---
    def is_goal(self) -> bool:
        """
        Returns True if this state is the goal state.
        """
        return self.board == self.GOAL_BOARD

    def successors(self) -> list[EightPuzzleState]:
        """
        Return a list of all valid successor states from the current state.
        """
        succs = []
        # Find the blank space
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    blank_r, blank_c = r, c
                    break

        # Possible moves: up, down, left, right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            new_r, new_c = blank_r + dr, blank_c + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_board = deepcopy(self.board)
                # Swap blank with adjacent tile
                new_board[blank_r][blank_c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[blank_r][blank_c]
                succs.append(EightPuzzleState(new_board))
        return succs

    def manhattan_distance(self) -> int:
        """
        Compute sum of Manhattan distances for all tiles (ignoring the blank).
        """
        total = 0
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0:
                    goal_r, goal_c = divmod(val - 1, 3)
                    total += abs(r - goal_r) + abs(c - goal_c)
        return total


def solution(puzzle_description: str) -> list[EightPuzzleState]:
    """
    Find the list of EightPuzzleStates that leads to a solution.
    puzzle_description: a string describing the puzzle to solve in the form 123450786 where 0 is the blank space.
    """
    # Convert string to 2D list
    board = [[int(puzzle_description[r * 3 + c]) for c in range(3)] for r in range(3)]
    start_state = EightPuzzleState(board)

    # Call astar from generic_search.py
    goal_node = astar(
        start_state,
        goal_test=lambda s: s.is_goal(),
        successors=lambda s: s.successors(),
        heuristic=lambda s: s.manhattan_distance()
    )

    # Convert Node path to list of states
    return node_to_path(goal_node) if goal_node else []


if __name__ == "__main__":
    # Example puzzle with 1 move away
    sol = solution("123450786")
    for i, state in enumerate(sol):
        print(f"State {i}")
        print(state)
        print("---")
    print(f"{len(sol)} states in solution")
