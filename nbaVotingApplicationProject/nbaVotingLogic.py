import csv
from typing import List, Dict

class VotingSystem:
    """
    This handles the NBA All-Star Voting System.

    Attributes:
        candidates (List[str]): List of player names.
        vote_counts (Dict[str, int]): Tracks the vote counts for each player.
        voters (set): Tracks the names of voters to ensure one vote per person.
        file_name (str): This is the Name of the CSV file where votes are saved.
    """

    def __init__(self):
        """
        Initializes the voting system with the different candidates and prepares the CSV file.
        """
        self.candidates: List[str] = [
            "LeBron James - Lakers",
            "Stephen Curry - Warriors",
            "Giannis Antetokounmpo - Bucks",
            "Jayson Tatum - Celtics",
        ]
        self.vote_counts: Dict[str, int] = {player: 0 for player in self.candidates}
        self.voters: set = set()
        self.file_name: str = "votes.csv"

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter Name", "Player Voted For"])

    def get_candidates(self) -> List[str]:
        """
        Returns the list of candidates.
        """
        return self.candidates

    def vote(self, voter_name: str, player_name: str) -> None:
        """
        Records a vote for a player from a voter.

        Args:
            voter_name (str): Name of the voter.
            player_name (str): Name of the player.

        Raises:
            ValueError: If voter_name is empty, has already voted, or if player_name is invalid.
        """
        if not voter_name:
            raise ValueError("Please enter a name.")
        if voter_name in self.voters:
            raise ValueError("Only one submission per person.")
        if player_name not in self.vote_counts:
            raise ValueError("Invalid player selected.")

        self.voters.add(voter_name)
        self.vote_counts[player_name] += 1

        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([voter_name, player_name])

    def get_results(self) -> str:
        """
        Returns the voting results.

        Returns:
            str: A formatted string of player names and vote counts.
        """
        if sum(self.vote_counts.values()) == 0:
            return "No votes have been cast yet!"

        results = [f"{player}: {votes}" for player, votes in self.vote_counts.items()]
        return "\n".join(results)

    def reset_votes(self) -> None:
        """
        Resets all votes and clears the list of voters.
        """
        self.vote_counts = {player: 0 for player in self.candidates}
        self.voters.clear()

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter Name", "Player Voted For"])