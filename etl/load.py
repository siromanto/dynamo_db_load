import csv
import boto3

from configs.config import TRANSFORMED_FILE, DB_TABLE_NAME


# TODO: refactor this and change config file
def create_client_connection():
    dynampdb = boto3.resource('dynamodb')
    db = dynampdb.Table(DB_TABLE_NAME)
    print('CONNECT TO DYNAMODB...')
    return db


def get_rows_from_csv():
    items_list = []

    print('GET DATA FROM CSV FILE...')
    rows = csv.DictReader(open(TRANSFORMED_FILE))
    for row in rows:
        items_list.append(row)

    print(f'ROWS COUNT... {len(items_list)}')
    return items_list


def write_into_db(items):
    db = create_client_connection()

    try:
        with db.batch_writer() as batch:
            for row in items:
                print(f"LOAD ROW - encounter_id: {dict(row.items()).get('encounter_id')}, "
                      f"date: {dict(row.items()).get('generated_date')}")
                batch.put_item(Item=row)
        print(f'LOADED {len(items)} ROWS...')
    except Exception as e:
        print(f'Error: {e}')


def load_data():
    prepared_rows = get_rows_from_csv()
    write_into_db(prepared_rows)


if __name__ == '__main__':
    load_data()


