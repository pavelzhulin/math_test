import random


def generate_math_question(a: int, b: int) -> str:
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    signs = ['+', '-', '*', '/']
    sign = random.choice(signs)
    return f'{num1} {sign} {num2}'


def check_answer(question: str, user_answer: str):
    try:
        user_answer = float(user_answer)
        result = eval(question)
        return user_answer == result
    except ValueError:
        return False


def math_quiz(number_of_questions: int = 5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        math_question = generate_math_question(1, 20)
        user_answer = input(f'{math_question} = ')
        if check_answer(math_question, user_answer):
            correct_answers += 1



    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")
    if correct_answers >= number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку 5.")
    elif correct_answers >= number_of_questions * 0.6:
        print("Хорошо! Вы получаете оценку 4.")
    elif correct_answers >= number_of_questions * 0.4:
        print('Попробуйте ещё раз. Ваша оценка 3.')
    else:
        print("Плохо. Вы получаете оценку 2!")


math_quiz(7)