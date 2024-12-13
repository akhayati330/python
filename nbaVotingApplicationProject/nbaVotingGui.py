from PyQt6.QtWidgets import (
    QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QRadioButton, QButtonGroup, QMessageBox
)
from nbaVotingLogic import VotingSystem

class VotingApp:
    def __init__(self, window):
        # Initialize the voting system
        self.voting_system = VotingSystem()

        # Configure the main window
        window.setWindowTitle("NBA Voting App")
        window.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # Header Label
        self.header = QLabel("NBA All-Star Voting")
        self.header.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(self.header)

        # Name Input
        layout.addWidget(QLabel("Enter your name:"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        # Radio Buttons for Player Selection
        layout.addWidget(QLabel("Select your favorite player:"))
        self.player_group = QButtonGroup()
        self.radio_buttons = []
        for player in self.voting_system.get_candidates():
            rb = QRadioButton(player)
            self.player_group.addButton(rb)
            layout.addWidget(rb)
            self.radio_buttons.append(rb)

        # Buttons for Voting, Viewing Results, and Resetting Votes
        self.vote_button = QPushButton("Vote")
        self.vote_button.clicked.connect(self.submit_vote)
        layout.addWidget(self.vote_button)

        self.results_button = QPushButton("View Results")
        self.results_button.clicked.connect(self.display_results)
        layout.addWidget(self.results_button)

        self.reset_button = QPushButton("Start New Session")
        self.reset_button.clicked.connect(self.reset_votes)
        layout.addWidget(self.reset_button)

        # Status Label for Feedback
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        # Finalizing Layout
        container = QWidget()
        container.setLayout(layout)
        window.setCentralWidget(container)

    def submit_vote(self):
        """This handles the voting logic."""
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(None, "Error", "Please enter your name!")
            return

        selected_player = None
        for i, rb in enumerate(self.radio_buttons):
            if rb.isChecked():
                selected_player = self.voting_system.get_candidates()[i]
                break

        if not selected_player:
            QMessageBox.warning(None, "Error", "Please select a player!")
            return

        try:
            self.voting_system.vote(name, selected_player)
            self.status_label.setText(f"Thank you for voting, {name}!")
        except ValueError as e:
            QMessageBox.warning(None, "Error", str(e))

        # These are the inputs and reset radio buttons
        self.name_input.clear()
        self.player_group.setExclusive(False)
        for rb in self.radio_buttons:
            rb.setChecked(False)
        self.player_group.setExclusive(True)

    def display_results(self):
        """Show voting results in the GUI interface."""
        results_text = "Votes Received:\n\n"
        vote_counts = self.voting_system.vote_counts
        total_votes = sum(vote_counts.values())

        # Determine the winner(s)
        max_votes = max(vote_counts.values())
        winners = [player for player, votes in vote_counts.items() if votes == max_votes]

        # Append vote counts for each player
        for player, votes in vote_counts.items():
            results_text += f"{player}: {votes} votes\n"

        # Add the winner(s) to the results
        if total_votes > 0:
            if len(winners) > 1:
                results_text += f"\nWinners: {', '.join(winners)}"
            else:
                results_text += f"\nWinner: {winners[0]}"
        else:
            results_text += "\nNo votes have been cast yet!"

        # Display results in the status label
        self.status_label.setText(results_text)

    def reset_votes(self):
        """Reset votes and clear voter tracking."""
        confirm = QMessageBox.question(
            None, "New Session", "Are you sure you want to reset the votes?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.voting_system.reset_votes()
            self.status_label.setText("Votes have been reset.")