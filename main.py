import django_setup

from app.models import *

print("Виберіть дію:")
print("1. Створити Quiz")
print("2. Створити Question")
print("3. Створити Option")
print("4. Переглянути всі Quizzes")
print("5. Переглянути всі Questions для Quiz")
print("6. Оновити Quiz")
print("7. Видалити Quiz")

choice = input("Введіть номер дії: ")

if choice == '1':
    title = input("Введіть назву Quiz: ")
    description = input("Введіть опис Quiz: ")
    quiz = Quiz.objects.create(title=title, description=description)
    print(f"Створено Quiz: {quiz}")

elif choice == '2':
    quiz_id = input("Введіть ID Quiz: ")
    content = input("Введіть текст питання: ")
    quiz = Quiz.objects.get(id=quiz_id)
    question = Question.objects.create(quiz=quiz, content=content)
    print(f"Створено питання: {question}")

elif choice == '3':
    question_id = input("Введіть ID питання: ")
    content = input("Введіть варіант відповіді: ")
    is_correct = input("Правильна відповідь? (так/ні): ").lower() == 'так'
    question = Question.objects.get(id=question_id)
    option = Option.objects.create(question=question, content=content, is_correct=is_correct)
    print(f"Створено варіант відповіді: {option}")

elif choice == '4':
    quizzes = Quiz.objects.all()
    for quiz in quizzes:
        print(f"ID: {quiz.id}, Назва: {quiz.title}, Опис: {quiz.description}")

elif choice == '5':
    quiz_id = input("Введіть ID Quiz: ")
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    for question in questions:
        print(f"ID: {question.id}, Питання: {question.content}")

elif choice == '6':
    quiz_id = input("Введіть ID Quiz для оновлення: ")
    quiz = Quiz.objects.get(id=quiz_id)
    title = input(f"Нова назва ({quiz.title}): ") or quiz.title
    description = input(f"Новий опис ({quiz.description}): ") or quiz.description
    quiz.title = title
    quiz.description = description
    quiz.save()
    print(f"Оновлено Quiz: {quiz}")

elif choice == '7':
    quiz_id = input("Введіть ID Quiz для видалення: ")
    quiz = Quiz.objects.get(id=quiz_id)
    quiz.delete()
    print("Quiz видалено")
