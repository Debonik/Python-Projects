import matplotlib.pyplot as plt
from faker import Faker
import random

def generate_data(num_students=100):
    # Create a Faker instance
    fake = Faker()

    data = {
        'name': [fake.name() for _ in range(num_students)],
        'math_marks': [random.randint(50, 100) for _ in range(num_students)],
        'english_marks': [random.randint(50, 100) for _ in range(num_students)],
        'science_marks': [random.randint(50, 100) for _ in range(num_students)]
    }
    
    return data

def plot_histogram(data):
    plt.hist(data['math_marks'], alpha=0.5, label='Math')
    plt.hist(data['english_marks'], alpha=0.5, label='English')
    plt.hist(data['science_marks'], alpha=0.5, label='Science')
    plt.legend(loc='upper right')
    plt.title('Distribution of marks in Math, English and Science')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.show()

data = generate_data()
plot_histogram(data)