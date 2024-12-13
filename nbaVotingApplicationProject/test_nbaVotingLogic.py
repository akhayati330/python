import pytest
from nbaVotingLogic import VotingSystem

@pytest.fixture
#  Tests voting for a player and retrieving the results.
def voting_system():
    return VotingSystem()

def test_vote_and_results(voting_system):
    voting_system.vote("John", "LeBron James - Lakers")
    assert voting_system.vote_counts["LeBron James - Lakers"] == 1
    results = voting_system.get_results()
    assert "LeBron James - Lakers: 1" in results

def test_duplicate_vote(voting_system):
    voting_system.vote("John", "LeBron James - Lakers")
    with pytest.raises(ValueError, match="Only one submission per person."):
        voting_system.vote("John", "Stephen Curry - Warriors")

def test_reset_votes(voting_system):
    voting_system.vote("John", "LeBron James - Lakers")
    voting_system.reset_votes()
    assert voting_system.vote_counts["LeBron James - Lakers"] == 0
    assert voting_system.get_results() == "No votes have been cast yet!"

def test_invalid_vote(voting_system):
    with pytest.raises(ValueError, match="Invalid player selected."):
        voting_system.vote("John", "Invalid Player")