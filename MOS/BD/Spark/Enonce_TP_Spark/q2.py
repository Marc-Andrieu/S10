from pyspark import SparkContext
import csv

def parse_line(line):
    try:
        row = next(csv.reader([line], delimiter=';', quotechar='"'))
        return row
    except Exception:
        return None

def extract_info(row):
    coord_field = row[0].strip()
    lat_str, lon_str = [s.strip() for s in coord_field.split(',', 1)]
    lat = float(lat_str)
    lon = float(lon_str)
    arrondissement = row[21]
    cinconference = float(row[7])
    return (arrondissement, (cinconference, lat, lon))

if __name__ == '__main__':
    sc = SparkContext(appName='TallestTree')
    file = sc.textFile('arbresremarquablesparis2.csv')
    parsed = file.map(parse_line).filter(lambda r: r is not None)
    infos = parsed.map(extract_info).filter(lambda x: x is not None).reduceByKey(lambda v1,v2 : v1 if v1[0] > v2[0] else v2)

    print(*infos.collect(), sep="\n")
    sc.stop()