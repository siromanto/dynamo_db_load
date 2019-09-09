## How to start script:
##### Recuirements:
- Python 3.6.5
- AWS CLI
#### SET UP:
- `python -m venv .venv` 
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

and execute `run.py`
#### Configs:
File and db names discribed in configs/config.py file
#### AWS credentials:
Make sure, you set up aws credentials into `aws configure`
    
## Script parts    
    Transform:
        The original dataset has more than 65k rows and hasn't date field.
        This script create transformed csv file with:
         - incremented the date by a random day number between 1 and 5
         - takes the number of rows specified in orig_rows parameter
         - duplicate each original record by repeat counts
         
    Load:
        Load data into dynamodb table
        
