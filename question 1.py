

TICK = "✅"
CROSS = "❌"


questions = [
    {
        "question": "English: What is the synonym of 'happy'?",
        "choices": ["Sad", "Angry", "Joyful", "Tired"],
        "correct_index": 2  
    },
    {
        "question": "English: What is the past tense of 'eat'?",
        "choices": ["Eated", "Ate", "Eats", "Eating"],
        "correct_index": 1  
    },
    {
        "question": "Math: What is 7 + 5?",
        "choices": ["12", "10", "14", "11"],
        "correct_index": 0  
    },
    {
        "question": "Math: What is 9 × 3?",
        "choices": ["27", "18", "21", "36"],
        "correct_index": 0  
    }
]


letter_map = ["A", "B", "C", "D"]


score = 0

letter_map = ["A", "B", "C", "D"]


score = 0

print(" Multiple Choice Quiz - English & Math")
print("-----------------------------------------")


for i, q in enumerate(questions, 1):
    print(f"nQ{i}: {q['question']}")
    for idx, choice in enumerate(q["choices"]):
        print(f"   {letter_map[idx]}. {choice}")
    
  
    user_input = input("Your answer (A, B, C, D): ")
    if user_input in letter_map:
        user_index = letter_map.index(user_input)
        if user_index == q["correct_index"]:
            print(f"{TICK} Correct!\n")
            score += 1
        else:
            correct_letter = letter_map[q["correct_index"]]
            correct_answer = q["choices"][q["correct_index"]]
            print(f"{CROSS} Wrong! Correct answer is: {correct_letter}. {correct_answer}\n")
    else:
        print(f"{CROSS} Invalid choice. Skipped.\n")

print("-----------------------------------------")
print(f" You scored {score} out of {len(questions)}.")
if score == len(questions):
    print(" Perfect! Excellent job!")
elif score >= len(questions) // 2:
    print("👍 Good job! Keep practicing.")
else:
    print("Try again. You’ll get better!")
