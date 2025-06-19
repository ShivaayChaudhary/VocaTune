import random

def predict_accent(file_path):
    accents = ['Indian', 'American', 'British']
    prediction = random.choice(accents)
    score = random.randint(70, 95)

    return {
        'accent': prediction,
        'score': score,
        'tip': 'Practice soft R sounds' if prediction == 'Indian' else 'Great job!'
    }
