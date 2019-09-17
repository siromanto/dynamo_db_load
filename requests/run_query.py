from __future__ import print_function
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

from configs.helper import create_client_connection


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


def get_data(table_name, partition_key, search_value):
    table = create_client_connection(table_name=table_name)
    data = get_query(table, partition_key, search_value)
    print(data)


def get_query(table, partition_key, search_value):
    try:
        response = table.query(
            KeyConditionExpression=Key(partition_key).eq(search_value)
        )
    except Exception as e:
        print(e)

    data = response.get('Items')[0]
    return data


if __name__ == '__main__':
    get_data(table_name='temp_for_load', partition_key='encounter_id', search_value='964548')