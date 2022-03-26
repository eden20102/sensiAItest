from unittest import result
import requests
import csv

def api_req(url):
    res = requests.get(url)
    data = res.json()
    return data

def get_all(url):
    results = []
    info = {'next': url}
    while info['next']:
        url = info['next']
        res = api_req(url)
        info, data = res['info'], res['results']
        results.extend( data )
    return results

def extract_data(data):
    new = []
    for row in data:
        name = row['name']
        image = row['image']
        location = row['location']['name']
        new.append([name, image, location])
    return new

def main():
    url = 'https://rickandmortyapi.com/api/character/?Species=uman&status=alive&origin=Earth'
    print('Extracting data from api...')
    results = get_all(url)
    data = extract_data(results)
    with open('data.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        header = ['Name', 'Image', 'Location']
        writer.writerow(header)
        writer.writerows(data)


main()