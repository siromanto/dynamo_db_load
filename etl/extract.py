import re
import json
import sys
import os
import requests
import wget
from configs.helper import get_parsed_page
from definitions import ROOT_DIR


def extract_csv(url, key_file=None):
    csv_links = scrape_site(url)
    print(csv_links)
    print('test')
    target_link = ''

    if len(csv_links) < 1:
        print('There is no csv files in scraped data. Please, check the link you entered')
        sys.exit()
    elif len(csv_links) >= 1:
        target_link = find_target_link(csv_links, key_file)

    download_data_file(target_link)




    # target_link = find_target_link(csv_links, key_file)
    print(target_link)



def download_data_file(url):
    file_name = parse_file_name(url)
    file_path = os.path.join(ROOT_DIR, f'data/{file_name}')

    print('Beginning file download with wget module...')
    print(f'FILE NAME --- {file_name}')

    try:
        wget.download(url, file_path)
        print(f'File {file_path} successfully downloaded')
    except Exception as e:
        print(e)


def parse_file_name(url):
    try:
        chunk = url.split('.csv')[0]
        chunk = chunk.split('/')[-1]
        full_name = f'{chunk}.csv'
        return full_name
    except Exception as e:
        print(e)
        return 'kaggle_data.csv'



def get_data():
    pass


def find_target_link(links_list, key_file):
    if key_file:
        target_link = ''

        for link in links_list:
            match = re.search(key_file, link)
            if match:
                target_link = link

        if not target_link:
            print("Target link doesn't found, but other csv file presented. Try to get data....")
            return links_list[0]  # return first csv file from list
        else:
            return target_link
    else:
        return links_list[0]  # return first csv file from list


def scrape_site(url):
    soup = get_parsed_page(url)
    # print(soup)
    data_links = get_parse_data(soup)

    csv_links = []
    # get only .csv files
    for link in data_links:
        match = re.search(r'.csv', link)
        if match:
            csv_links.append(link)

    return csv_links


def get_parse_data(soup):
    content_block = json.loads(soup.find('script', type='application/ld+json').text)
    link_list = [v.get('contentUrl') for v in content_block['distribution']]
    return link_list


if __name__ == "__main__":
    # extract_csv('https://www.kaggle.com/xiaotawkaggle/inhibitors')
    # extract_csv('https://www.kaggle.com/piotrgrabo/breastcancerproteomes')
    extract_csv('https://www.kaggle.com/piotrgrabo/breastcancerproteomes', 'clinical_data')

