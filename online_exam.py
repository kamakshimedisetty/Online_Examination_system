def student_login():
    print("=====student login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "student" and password == "1234":
        print("Login successful!\n")
        return username
    else:
        print("Invalid login details.\n")
        return None
def conduct_exam():
    questions = [
        {
        "question"
        : "Which keyword is uesd to define a function in python?","options": [
            "A. function",
            "B. def",
            "c. fun"
        ],
        "answer": "B"
        },
        {
            "question": "Which symbol is used for comments in python?",
            "options": [
                "A. //",
                "B. /* */",
                "C. #",
                "D. <!-- -->"
            ],
            "answer": "C"
        },
        {
            "question": "Which data type is used to store multiple values in a single variables?",
            "options": [
                "A. int",
                "B. float",
                "C. List",
                "D. char"
            ],
            "answer": "C"
        },
        {
            "question": "What is the output of: print(2 + 3 * 2)?",
            "options": [
                "A. 10",
                "B. 7",
                "C. 12",
                "D. 5"
            ],
            "answer": "B"
        }, 
        {
            "question": "Which loops used to iterate over a sequence in python?",
            "options": [
                "A. While",
                "B. loop",
                "C. for",
                "D. repeat"
            ],
            "answer": "C"
        }, 
        {
            "question": "What will be the output of the following python code?",
            "code": """list1 = ['a','b','c','d']
            i=0
            while True:
                print(list1[i])
                i += 1
                if i= len(list1):
                    break""",
            "options": [
                "A. a b c d",
                "B. d c b a",
                "C. a b c",
                "D. Error"
            ],
            "answer": "A"
        },
        {
            "question": "What will be the output of the following python code?",
            "code": """x = 5
            y = 3
            print(x + y * 2)""",
            "options": [
                "A. 16",
                "B. 11",
                "C. 13",
                "D. 10"
            ],
            "answer": "B"
        },
        {
            "question": "What will be the output of the following python code?",
            "code": """x = 10
            print(x > 5)""",
            "options": [
                "A. True",
                "B. False",
                "C. 10",
                "D. Error"
            ],
            "answer": "A"
        },
        {
            "question": "what is the output of the following code?",
            "code": """i = 0
            while i < 3:
                print(i)
                i += 1""",
            "options": [
                "A. 0 1 2",
                "B. 1 2 3",
                "C. 0 1 2 3",
                "D. Error"
            ],
            "answer": "A"
        },
        {
            "question": "What is the output of the following code?",
            "code": """x = 5
            y = 2
            print(x + y)""",
            "options": [
                "A. 10",
                "B. 5",
                "C. 7",
                "D. Error"
            ],
            "answer": "C"
        }        
    ]
    score = 0

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == q["answer"]:
            print("Correct answer!\n")
            score = score + 1
        else:
            print("Wrong answer!\n")
    return score, len(questions)

def show_scorecard(name, score, total):
    print("=====SCORE CARD=====")  
    print("student Name :", name)
    print("Total questions :", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total-score)

    percentage = (score / total ) * 100
    print("percentage :",percentage,"%")

    if percentage >= 50:
        print("Result : PASS")
    else:
        print("Result : FAIL")
print("======0NLINE EXAMINATION SYSTEM======\n")
student_name = student_login()

if student_name is not None:
    final_score, total_questions = conduct_exam()
    show_scorecard(student_name,final_score,total_questions)
else:
    print("Please try again later.")    
