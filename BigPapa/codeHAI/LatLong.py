

import csv
from geopy.geocoders import Nominatim

#if your sites are located in France only you can use the country_bias parameters to restrict search
geolocator = Nominatim(country_bias="France")

with open('c:/temp/input.csv', 'rb') as csvinput:
    with open('c:/temp/output.csv', 'wb') as csvoutput:
       output_fieldnames = ['Site', 'Address_found', 'Latitude', 'Longitude']
       writer = csv.DictWriter(csvoutput, delimiter=';', fieldnames=output_fieldnames)
       writer.writeheader()
       reader = csv.DictReader(csvinput)
       for row in reader:
            site = row['site']
            if site != "NULL":
                try:
                    location = geolocator.geocode(site)
                    address = location.address
                    latitude = location.latitude
                    longitude = location.longitude
                except:
                    address = 'Not found'
                    latitude = 'N/A'
                    longitude = 'N/A'
            else:
                address = 'N/A'
                latitude = 'N/A'
                longitude = 'N/A'

            #here is the writing section
            output_row = {}
            output_row['Site'] = row['site']
            output_row['Address_found'] = address.encode("utf-8")
            output_row['Latitude'] = latitude
            output_row['Longitude'] = longitude
            writer.writerow(output_row)


