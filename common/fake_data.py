from faker import Faker
import random

class FakeData:
    def __init__(self):
        self.faker = Faker('es_MX')  # Configura Faker para generar datos en español

    def generate_person_data(self):
        data = {}
        data['first_name'] = self.faker.first_name()
        data['last_name'] = self.faker.last_name()
        data['email'] = self.faker.email()
        data['password'] = self.faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        data['city'] = self.faker.city()
        data['country'] = self._generate_latin_american_country()
        data['code_country'] = self.faker.country_code()
        data['description'] = self.faker.text(max_nb_chars=200)
        return data

    def _generate_latin_american_country(self):
        # Lista de países latinoamericanos
        latin_american_countries = [
            "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Costa Rica",
            "Cuba", "República Dominicana", "Ecuador", "El Salvador", "Guatemala",
            "Honduras", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "Uruguay", "Venezuela"
        ]
        return random.choice(latin_american_countries)
