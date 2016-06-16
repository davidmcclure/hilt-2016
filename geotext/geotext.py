

import os
import click
import csv
import json

from bs4 import BeautifulSoup
from geojson import Point, Feature, FeatureCollection
from geopy.geocoders import Mapzen

from shapely.geometry import Point as ShapelyPoint
from shapely import wkt

from utils import degrees_to_meters


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

    geocoder = Mapzen(
        os.environ['MAPZEN_KEY'],
        timeout=10,
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


@geotext.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def csv_to_geojson(in_file, out_file):

    """
    Convert a geocoded CSV to GeoJSON.
    """

    reader = csv.DictReader(in_file)

    features = []
    for row in reader:

        lat = float(row.pop('latitude'))
        lon = float(row.pop('longitude'))

        point = Point((lon, lat))

        feature = Feature(
            geometry=point,
            properties=row,
        )

        features.append(feature)

    collection = FeatureCollection(features)

    print(json.dumps(collection, indent=2), file=out_file)


@geotext.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def csv_to_neatline(in_file, out_file):

    """
    Format a CSV file for Neatline.
    """

    reader = csv.DictReader(in_file)

    # Add wkt field to the CSV.
    cols = reader.fieldnames + ['wkt']
    writer = csv.DictWriter(out_file, cols)
    writer.writeheader()

    for row in reader:

        lat = float(row.pop('latitude'))
        lon = float(row.pop('longitude'))

        # Convert degrees -> meters.
        meters = degrees_to_meters(lon, lat)

        # Convert to WKT.
        point = ShapelyPoint(meters)
        row['wkt'] = wkt.dumps(point)

        writer.writerow(row)


if __name__ == '__main__':
    geotext()
