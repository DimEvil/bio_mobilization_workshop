from pygbif import registry
from pygbif import species
import csv

def country_datasets(countryCode, limit=5):
    # Search datasets published by Croatia
    registry.datasets(limit=limit)
    HRdatasets = registry.dataset_search(publishingCountry=countryCode)

    with open('../data/datasets.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, HRdatasets['results'][0].keys())
        writer.writeheader()
        for dataset in HRdatasets['results']:
            writer.writerow(dataset)

def name_lookup(name, limit=2):
    r=species.name_lookup(q=name, limit=limit)
    print(r['results'])

country_datasets('HR')
names = ['Tursiops truncatus', 'Milvus milvus']
for name in names:
    name_lookup(name)
