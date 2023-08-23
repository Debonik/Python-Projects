from faker import Faker
import csv

def create_fake_data(filename, num_rows):
    # Create a Faker instance
    fake = Faker()

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'address', 'email', 'birthdate', 'phone_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(num_rows):
            writer.writerow({
                'id': i,
                'name': fake.name(),
                'address': fake.address().replace('\n', ', '),
                'email': fake.email(),
                'birthdate': fake.date_of_birth(minimum_age=22, maximum_age=90).isoformat(),
                'phone_number': fake.phone_number()
            })
        
# Generate 1000 rows of fake data
create_fake_data('fake_data.csv', 1000)