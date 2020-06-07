from question import Question

question_prompt = [
    "How many states in the United States?\n (a) 52\n (b) 48 \n (c) 50 \n (d) 51\n",
    "How many colours in the rainbow?\n (a) 6\n (b) 7\n (c) 5 \n (d) 8\n",
    "In what year did WW2 end?\n (a) 1914\n (b) 1939 \n (c) 1918 \n (d) 1945\n"
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "d")
]

def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct")

runTest(questions)