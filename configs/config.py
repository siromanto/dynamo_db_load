import os
from definitions import ROOT_DIR

# For download the file:
KAGGLE_URL = 'https://www.kaggle.com/piotrgrabo/breastcancerproteomes'
KEY_FILE = 'clinical_data'

# For transform the file:
ORIGIN_FILE = os.path.join(ROOT_DIR, 'data/diabetic_data.csv')
TRANSFORMED_FILE = os.path.join(ROOT_DIR, 'data/transformed_data.csv')

# For download into dynamodb:
DB_TABLE_NAME = 'temp_for_load'

