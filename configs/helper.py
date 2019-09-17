import boto3
import requests
from bs4 import BeautifulSoup


def create_client_connection(table_name):
    dynampdb = boto3.resource('dynamodb')
    db = dynampdb.Table(table_name)
    print('CONNECT TO DYNAMODB...')
    return db


def get_parsed_page(url):
    raw_html = get_page_html(url)
    soup = BeautifulSoup(raw_html, 'lxml')
    return soup


def get_page_html(url):
    try:
        r = requests.get(url)
    except requests.exceptions.InvalidSchema as e:
        raise Exception(f'Can\'t parse url, error: {e}')

    if not r.status_code == 200:
        if r.status_code == 404:
            if 'Job is expired' in r.text:
                print('RESPONSE FROM SITE: Job is expired. Find your next job and advance your career today')
                return 'na'
            else:
                raise Exception('Invalid url from parsed url')
    else:
        response = r.text
        return response
