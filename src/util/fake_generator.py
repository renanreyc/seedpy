import pandas as pd
from faker import Faker
import datetime
import random
import re


class FakeGenerator:
    def __init__(self, fake):
        """
        Initialize FakeGenerator

        validation = validator.FakeGenerator(dataframe)

        Parameters
        ----------
        dataframe: df

        Returns
        ----------
        new FakeGenerator class

        Atributes
        ----------

        """
        self.fake = fake

    def random_older_date(self, date_value, specify_end_date=None):
        random_date = self.fake.date_between(
            start_date=date_value, end_date=specify_end_date
        )
        return random_date

    def gen_random_day_time(self, days=10, only_days=False):
        random_days = random.randint(0, days)
        if only_days:
            return datetime.timedelta(days=only_days)

        random_hours = random.randint(1, 24)
        random_minutes = random.randint(1, 60)
        random_seconds = random.randint(1, 60)

        return datetime.timedelta(
            days=random_days,
            hours=random_hours,
            minutes=random_minutes,
            seconds=random_seconds,
        )
