from Questions import Questions


questions_promt =[
    "1. What color are apple \n a)Red \n b)Yellow \n c)Blue \n",
    "2. What color are strawberries \n a)Red \n b)Green \n c)Black \n",
    "3. What color are bananas \n a)Yellow \n b)White \n c)Purple \n"
]
questions = [
    Questions(questions_promt[0],"a"),
    Questions(questions_promt[1],"a"),
    Questions(questions_promt[2],"a")
]

def run_test(question):
    score=0
    for question in questions:
        ans=input(question.question)
        if ans==question.answer:
            score=score+1
    print("Your score is "+str(score)+"/"+str(len(questions_promt)))



run_test(questions)