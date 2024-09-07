from faker import Faker
from main_app.models import TodoList
from accounts.models import MyUser

faker = Faker()

def generate_fake_data():
    # Get the specific user by email
    user = MyUser.objects.get(email="symonbarua4@gmail.com")
    
    for _ in range(20): 
        # Create a TodoList entry for the specified user
        TodoList.objects.create(
            tasks=faker.sentence(nb_words=4),
            owner=user,  # Use the specified user directly
            description=faker.paragraph()[:100],  
            completed_task=faker.boolean(),
            not_completed_task=faker.boolean(),
            due_date=faker.date_between(start_date='today', end_date='+30d'),
            created_at=faker.date_time_this_year(),
            updated_at=faker.date_time_this_year()
        )

    print("Successfully generated fake data")

