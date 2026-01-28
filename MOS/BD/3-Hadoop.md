# Hadoop

## Big Data et parallélisme

En 2004, 2 ingés de Google

Hadoop ça permet d'encapsuler le //-isme comme ça c abstrait donc masqué pr une DX avec une learning curve assez trql.

## Modèle MapReduce

Inspiration de la programmation fn-elle.
Avec deux fn `map` & `reduce` pr resp. transf & agréger les données, on peut tt faire.

Bon point : qd on map et qu'y a une certaine indépendance, on peut paralléliser l'application dla fn.

E.g. mult matricielle $x_o = \sum a_{ij} x_j$, le reducer bah ça sera la somme, et donc le mapper sera la multiplication de scalaires.

On mappe $(a_{ij}; x_j)$ sur $(j; a_{ij} \times x_j)$, on reduce en sommant les valeurs ayant la mm clef (ie. la mm ligne ds la matrice).

## HDFS (_Hadoop-Distributed FS_)

### "Socle technique"

Le "socle technique" de Hadoop est composé de :

- l'archi pr orchestrer le MapReduce, ie.
    - ordonnancement
    - localiser les fichiers
    - distrib l'exéc
- le HDFS, qui est :
    - distribué (les données des fichiers sont sur plusieurs nodes)
    - répliqué (à la "RAID")

### Master-slave

Y a peu de noeuds maîtres (job trackers) et bcp d'esclaves (data nodes & task trackers) genre $1 000 \times$ plus.

Les pages mémoires c pas du 16 Ko, c du 64 Mo ! C ENORME !

Le nameNode (maître) monitore les fichiers, blocs et la health du sys, et sert de load balancer.
Les milliers de DataNodes (esclaves) stockent, font les read/write, font des replicas, font des checksums, et checkent la health de leur nameNode.

### Lire/écrire un fichier ds un HDFS

Le maître sert de reverse-proxy, qui redirige le client vers le bon esclave (comme ça le transfert est direct entre le client et un esclave, c + rapide que de transiter par le maître).

Y a du Java et une JVM on sait pas pk, elle a dit que ct un package Python...

ça se manipule en 100% CLI, c identique à du (S)FTP : ls, mv, cat, put, mkdir, rm.
Mais préfixé avec `hdfs dfs` ou son alias `hadoop fs`.

## MapReduce sur cluster Hadoop

le _Combiner_, c un mini-reducer qui commence l'agrégation en sortie du mapper.

## Générateurs et Itérateurs en Python

Rien de nouveau pr bibi, on voit ça à ÉCLAIR ms pas ds les cours de Centrale.
`next()`, `yield`, etc

```py
def read_mapper_output(file, separator='\t'):
    for line in file:
    yield line.rstrip().split(separator,1)
```

## Chaînage MapReduce avec Mrjob

Y a des libraires Python pr simplifier le dév d'algo chaînés, genre `mrjob`.

```py
from mrjob.job import MRJob

class MRWordCountUtility(MRJob):

    def __init__(self,*args, **kwargs):
        super(MRWordCountUtility,self).__init__(*args, **kwargs)
        self.chars=0
        self.words=0
        self.lines=0

    def mapper(self, _, line):
        # Don't actually yield anything for each line. Instead, collect them
        # and yield the sums when all lines have been processed. The results
        # will be collected by the reducer.
        self.chars+=len(line)+1 # +1 for newline
        self.words+=sum(1 for word in line.split() if word.strip())
        self.lines+=1

    def mapper_final(self):
        yield("chars", self.chars)
        yield("words", self.words)
        yield("lines", self.lines)

    def reducer(self, key, values):
        yield(key, sum(values))

if __name__=='__main__':
    MRWordCountUtility.run()
```

## Exemple Système de recommandation vidéo

Objectif : proposer une recommandation sur l'analyse de l’historique de
notations des films par les clients.

Pour cela, 3 étapes (c’est à dire 3 jobs consécutifs):

1. Pour chaque pair de films A et B, trouver tous les clients
   qui ont noté A et B.
2. Construire un vecteur de notes pour le film A et un vecteur
   de notes pour le film B, et calculer la corrélation entre ces
   deux vecteurs.
3. Pour chaque film, trier les films les plus similaires.

```py
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
...
class MoviesSimilarities(MRJob):
    OUTPUT_PROTOCOL = JSONValueProtocol
    def steps(self):
        return [
            MRStep(mapper=self.group_by_user_rating, reducer=self.count_ratings_users_freq),
            MRStep(mapper=self.pairwise_items, reducer=self.calculate_similarity),
            MRStep(mapper=self.calculate_ranking, reducer=self.top_similar_items)
        ]
    ...

def group_by_user_rating(self, key, line):
    user_id, item_id, rating = line.split("|")
    yield user_id, (item_id, float(rating))

def count_ratings_users_freq(self, user_id, values):
    item_count = 0
    item_sum = 0
    final = []
    for item_id, rating in values:
        item_count += 1
        item_sum += rating
        final.append((item_id, rating))
    yield user_id, (item_count, item_sum, final)
```

## Ecosystème Hadoop

Ut par les gros : LI, Gle, Ebay, MS, Yahoo, X, Amzn, le MIT, etc.
