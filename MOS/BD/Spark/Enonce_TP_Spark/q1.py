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
    height_str = row[8].strip()
    if height_str == '':
        print(row)
        return None
    height = float(height_str)
    address = row[6].strip() if len(row) > 6 else ''
    return (height, (lat, lon, address))

if __name__ == '__main__':
    sc = SparkContext(appName='TallestTree')
    file = sc.textFile('arbresremarquablesparis2.csv')
    parsed = file.map(parse_line).filter(lambda r: r is not None)
    infos = parsed.map(extract_info).filter(lambda x: x is not None)
    if infos.isEmpty():
        print("Aucun enregistrement avec hauteur valide trouvé.")
    else:
        tallest = infos.max()
        height, (lat, lon, address) = tallest
        print("Arbre le plus grand :")
        print("  latitude =", lat)
        print("  longitude =", lon)
        print("  hauteur  =", height)
        print("  adresse  =", address)
    sc.stop()