import pandas as pd

def generate_date_range(start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date)
    return [date.date() for date in date_range]