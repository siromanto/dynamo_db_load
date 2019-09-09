import csv
import boto3
import csv

# def load():
#     dynampdb = boto3.resource('dynamodb')
#     db = dynampdb.Table('dataset_tes_load')
#
#     # db.put_item(
#     #     Item={
#     #         'connectionId': '42',
#     #         'orgId': '42'
#     #     }
#     # )


dynampdb = boto3.resource('dynamodb')

def batch_write(table_name, rows):
    table = dynampdb.Table(table_name)

    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item=row)
    return True


def read_csv(csv_file, litems_ist):
    rows = csv.DictReader(open(csv_file))


    for row in rows:
        print(len(dict(row)))
        litems_ist.append(row)


def get_item():
    client = boto3.client('dynamodb')
    response = client.get_item(TableName='cancer_dataset_load', Key={'patient_nbr': {'S': str('8222157')}})
    print(response)


if __name__ == '__main__':
    table_name = 'cancer_dataset_load'
    file_name = '../data/transformed_data.csv'
    items = []

    read_csv(file_name, items)
    # print(items)
    status = batch_write(table_name, items)
    # get_item()


