# Mini Quiz Game

questions = [
    {"q": "What is the capital of France?", "a": "paris"},
    {"q": "What is 5 + 7?", "a": "12"},
    {"q": "Name the largest planet in our solar system.", "a": "jupiter"},
    {"q": "Which language is this quiz written in?", "a": "python"},
    {"q": "What color do you get by mixing red and white?", "a": "pink"}
]

score = 0

for i, item in enumerate(questions, 1):
    answer = input(f"Q{i}: {item['q']}\nYour Answer: ").strip().lower()
    if answer == item["a"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct Answer: {item['a'].capitalize()}\n")

print(f"\nFinal Score: {score}/{len(questions)}")
if score == 5:
    print("Excellent job!")
elif score >= 3:
    print("Good effort!")
else:
    print("Keep practicing!")
