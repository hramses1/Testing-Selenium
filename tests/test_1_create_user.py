import pytest
from src.page.login import LoginPage
from src.page.site_administrator import SiteAdministrator
from src.page.create_new_user import CreateNewUser
from dotenv import load_dotenv
import os
from common.drive import init_driver  # Importa el fixture
import time

load_dotenv()

@pytest.mark.usefixtures("init_driver")
class TestCreationApplicant:

    @pytest.mark.parametrize("n", range(5))  # Repetirá el test 5 veces
    def test_create_applicant_with_mandatory_values(self, n):
        LoginPage(self.driver).valid_login(os.getenv("USER"), os.getenv("PASSWORD"))
        SiteAdministrator(self.driver).result()
        CreateNewUser(self.driver).result()

        # Añade un pequeño retraso de 1 segundo entre cada repetición
        time.sleep(2)
