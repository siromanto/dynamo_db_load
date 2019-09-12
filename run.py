from etl import extract, transform, load

from configs.config import KAGGLE_URL,KEY_FILE, ORIGIN_FILE, TRANSFORMED_FILE

"""
    Transform:
        The original dataset has more than 65k rows and hasn't date field.
        This script create transformed csv file with:
         - incremented the date by a random day number between 1 and 5
         - takes the number of rows specified in orig_rows parameter
         - duplicate each original record by repeat counts
         
     Load:
        Load data into dynamodb table
        
    File and db names described in configs/config.py file
"""


if __name__ == '__main__':
    extract.extract_csv(KAGGLE_URL, KEY_FILE)
    transform.transform_csv(ORIGIN_FILE, TRANSFORMED_FILE, rows=300, repeat=10)
    load.load_data()
