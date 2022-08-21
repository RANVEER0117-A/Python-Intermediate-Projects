from faker import Faker

fake = Faker ()

fakejp = Faker('ja_JP')

for _ in range(10): print(fake.name())