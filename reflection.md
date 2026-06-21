# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input   | Expected Behavior | Actual Behavior | Console Output / Error |
|---------|-------------------|-----------------|------------------------|
|New Game | start new game    |nothing happened | none
| 45      | Go Lower          |   Go Higher     | none
| -5      | Go Higher         |   Go Lower      | none 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code as a teammate to help me read the starter code, explain Streamlit behavior, and suggest fixes.

When I described that the game told me to "Go HIGHER!" after I guessed too high, the AI suggested the hint messages in check_guess function were mapped backwards and recommended pulling them into a single HINT_MESSAGES dictionary so "Too High" → "Go LOWER!" and "Too Low" → "Go HIGHER!". This was correct. I verified it two ways: I wrote pytest regression tests (test_too_high_hint_points_lower and test_too_low_hint_points_higher) and they passed, and I also replayed the game — guessing a number above the secret now correctly says "Go LOWER!", matching my bug log row for input 45.

The original code cast the secret to a string on every other attempt (secret = str(...)), and when I asked about the check_guess function the AI suggested keeping a try/except TypeError fallback that compares the guess and secret as strings, claiming it made the code "more robust." This was misleading: comparing numbers as text gives wrong answers (for example, the string "9" is "greater than" "100"), so the hints would still flip on certain attempts. I verified it was wrong by tracing it by hand and testing with pytest — comparing values as strings produced a "Too High" result when the number was actually lower, so I removed the string casting entirely and compared the guess to the integer secret directly, which made the tests pass consistently.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided the bug was fixed by checking the exact situations where the hint logic had been wrong before. The bug was that when the player guessed too high, the game told them to go higher, and when they guessed too low, it told them to go lower. So I wrote regression tests for both cases to make sure the directions were no longer flipped.

One test I ran was test_too_high_hint_points_lower(). In this test, the guess was 60 and the secret number was 50, so the correct hint should be “Go LOWER!” The test passed, which showed that my code now correctly handles guesses that are above the secret number.

I also ran test_too_low_hint_points_higher(). In this test, the guess was 40 and the secret number was 50, so the player should be told to “Go HIGHER!” This test also passed, showing that the opposite case was fixed too.

AI helped me understand these as regression tests. It helped me think through the edge cases by asking: “What was the original bug, and what test would fail if that bug came back?” That made it easier to design tests that directly checked the broken behavior instead of only testing random guesses.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
