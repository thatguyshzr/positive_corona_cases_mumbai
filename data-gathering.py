import requests
import re
import csv


def get_site_content(url):
    r = requests.get(url)
    return r.text


def get_location(page_content):
    markers = re.findall(
        'L.marker\(\s*\[[0-9]{2}\.[0-9]{4,},\s*[0-9]{2}\.[0-9]{4,}',
        page_content)
    # look for 'L.marker(', then white-spaces,
    # then location digits seperated by comma

    location = []
    for i in markers:
        '''
        # get digits from 'markers'
        location_digits= re.findall('[0-9]{2}\.[0-9]{4,}', i)
        # convert location to float
        location_float= [float(qwe) for qwe in location_digits]
        # add it to location
        location.append(x)
        '''

        # the whole thing can be written as:
        location.append([float(qwe)
                        for qwe in re.findall('[0-9]{2}\.[0-9]{4,}', i)])

    '''
    They messed up the latitude and longitude for some entries,
    gotta fix that or we'll end up in Norwegia.
    '''
    for i in location:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]

    return location


def export_to_csv(data):
    with open("locations.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Latitude', 'Longitude'])
        writer.writerows(data)

if __name__ == '__main__':
    url = 'http://3.21.5.119/COVID19/containment_zones/'
    site_content = get_site_content(url)
    location = get_location(site_content)
    export_to_csv(location)
