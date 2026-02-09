from pyspark import SparkContext
import csv

def parse_line(line):
    try:
        row = next(csv.reader([line], delimiter=',', quotechar='"'))
        return row
    except Exception:
        return None

def moyenne_poids(tuple1, tuple2):
    v1, p1 = tuple1
    v2, p2 = tuple2
    return ( (v1*p1+v2*p2) / (p1+p2), p1+p2)

if __name__ == '__main__':
    sc = SparkContext(appName='TallestTree')
    movies = sc.textFile('movies.csv').map(parse_line).filter(lambda r: r is not None).map(lambda row: (row[0], row[1]))
    ratings = sc.textFile('ratings.csv').map(parse_line).filter(lambda r: r is not None).map(lambda row: (row[1], float(row[2])))
    jointure = movies.join(ratings)
    titre_vers_rating = jointure.map(lambda row: (row[1][0], (row[1][1], 1.0)))
    rating_moyen = titre_vers_rating.reduceByKey(moyenne_poids).sortBy(lambda row: row[1], ascending=False)

    #print(*titre_vers_rating.collect()[:20], sep="\n")
    print(*rating_moyen.collect()[:100], sep="\n")
    sc.stop()