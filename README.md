# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Sample game on Normal (secret = 30, range 1–50, 6 attempts):

1. Start new game → score 0, attempts left 6
2. Guess 20 → "Go HIGHER!" → score −5
3. Guess 35 → "Go LOWER!" → score −10
4. Guess 30 → "Correct!" → +80 → final score 70
5. Game ends; New Game resets score, attempts, and secret

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.12.2, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/zhuoerdu/AI110/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                                                                                                                                                      

tests/test_game_logic.py .....                                                                                                                                   [100%]

========================================================================== 5 passed in 0.03s ===========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
