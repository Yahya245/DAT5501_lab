import numpy as np 

def days_since(date_str):
    """
    Calculate how many days have passed since the given date.
    :param date_str: date string in 'YYYY-MM-DD' format
    :return: number of days since that date
    """
    input_date = np.datetime64(date_str)
    today = np.datetime64('today')
    return ( today - input_date).astype(int)

#Emap[le usage:
date_input = input ("Enter a date (YYYY-MM-DD): ")
days = days_since(date_input)
print(f"{days} days have passed since {date_input}.")