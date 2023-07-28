#!/usr/bin/python3
"""This module solves the nqueen bactracking problem"""
import sys


class Solution:
    def solveNQueens(self, n):
        """Find all solutions to the N-Queens problem.
        Args: n (int) - The size of the chessboard (N).
        Returns: list - A list of solutions, each as a nested list of
                [row, column] positions for each queen.
        """
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        """Check if the current state is a valid solution.
        Args: state (list) - A list representing the current state of
                the chessboard.
              n (int) - The size of the chessboard (N).
        Returns: bool - True if the state is a valid solution, False otherwise.
        """
        return len(state) == n

    def get_candidates(self, state, n):
        """Get the valid candidate positions for the next queen placement.
        Args: state (list) - A list representing the current state of the
                chessboard.
              n (int) - The size of the chessboard (N).
        Returns: set - A set of column indices representing the valid
                candidate positions.
        """
        if not state:
            return set(range(n))

        position = len(state)
        candidates = set(range(n))
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        """Recursively search for all valid solutions to the N-Queens problem.
        Args: state (list) - A list representing the current state of the
                chessboard.
              solutions (list) - A list to store the valid solutions.
              n (int) - The size of the chessboard (N).
        """
        if self.is_valid_state(state, n):
            state_string = self.state_to_nested_list(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_nested_list(self, state, n):
        """Convert the state representation to a nested list.
        Args: state (list) - A list representing the current state of the
                chessboard.
              n (int) - The size of the chessboard (N).
        Returns: list - A nested list of [row, column] positions for each queen
        """
        answer = []
        for index, value in enumerate(state):
            answer.append([index, value])
        return answer

arg = sys.argv
try:
    arg_1 = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
except IndexError:
    print("Usage: nqueens N")
else:
    if arg_1 < 4:
        print("N must be at least 4")
    else:
        NQueen = Solution()
        solution_list = NQueen.solveNQueens(int(sys.argv[1]))
        for solution in solution_list:
            print(solution)
