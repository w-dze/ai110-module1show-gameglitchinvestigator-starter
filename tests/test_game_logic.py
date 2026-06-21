from logic_utils import check_guess, HINT_MESSAGES

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_hint_points_lower():
    # Regression: a guess ABOVE the secret must tell the player to go LOWER.
    # The original bug returned "Go HIGHER!" for a too-high guess.
    outcome = check_guess(60, 50)
    assert HINT_MESSAGES[outcome] == "📉 Go LOWER!"

def test_too_low_hint_points_higher():
    # Regression: a guess BELOW the secret must tell the player to go HIGHER.
    # The original bug returned "Go LOWER!" for a too-low guess.
    outcome = check_guess(40, 50)
    assert HINT_MESSAGES[outcome] == "📈 Go HIGHER!"
