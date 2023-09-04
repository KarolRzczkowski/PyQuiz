import pyautogui
import pymongo
import random

# Establish a connection to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')

# Access the database
db = client['mydatabase']

# Access the collection
collection = db['quiz']

coords = (pyautogui.size().width - 1, 1)
wronganswers = 0

def QuizApp(correctanswer, wronganswer):
    try:
        while True:
            # Pobierz wszystkie pytania z bazy danych
            questions_data = list(collection.find({}))

            if not questions_data:
                break  
           
            question_data = random.choice(questions_data)
            questions_data.remove(question_data)

            question_text = question_data['question']
            options = question_data['options']
            
            user_answer = input(f"{question_text} ({'/'.join(options.values())}): ")
            
            if user_answer.lower() == options[correctanswer].lower():
                print('Correct Answer')
            else:
                print('Wrong Answer')
                global wronganswers
                wronganswers += 1
                print(f"Wrong Answers Count: {wronganswers}")    
                if wronganswers == 4:
                    print('You are stupid')
                    break  
    except ValueError:
        print('Value Error')
    except Exception as e:
        print(f'An error occurred: {e}')

QuizApp('correct', 'wrong')
