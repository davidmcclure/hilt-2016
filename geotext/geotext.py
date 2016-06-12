

import os
import click
import csv

from bs4 import BeautifulSoup
from geopy.geocoders import GoogleV3


@click.group()
def geotext():
    pass


@geotext.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def ner_to_csv(in_file, out_file):

    """
    Extract tagged toponyms from a text file.
    """

    tree = BeautifulSoup(in_file.read(), 'html.parser')

    cols = ['toponym', 'offset']
    writer = csv.DictWriter(out_file, cols)
    writer.writeheader()

    for i, loc in enumerate(tree.select('location')):

        writer.writerow(dict(
            toponym=loc.text,
            offset=i,
        ))


@geotext.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def geocode(in_file, out_file):

    """
    Geocode toponyms in a CSV file.
    """

    reader = csv.DictReader(in_file)

    geocoder = GoogleV3(
        domain='dstk.dclure.org',
        timeout=10,
        scheme='http',
    )

    # Add lon/lat fields to the CSV.
    cols = reader.fieldnames + ['latitude', 'longitude']

    writer = csv.DictWriter(out_file, cols)
    writer.writeheader()

    for row in reader:

        print(row['toponym'])

        # Query the DSTK API.
        try:

            loc = geocoder.geocode(row['toponym'])

            print(loc.point)

            # Merge in the coordinates.
            row.update(dict(
                latitude=loc.latitude,
                longitude=loc.longitude,
            ))

            # Write the result to the CSV.
            writer.writerow(row)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    geotext()
