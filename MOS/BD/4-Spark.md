# Spark

Ca remplace Hadoop ds les entreprises, psk c + rapide, mm si ça bouffe bcp + de RAM ms ça les entreprises s'en foutent.

## Programmation fonctionnelle en Python

### Fn "pures"

> Une fonction pure est une fonction qui, pour un même ensemble d'entrées, renvoie toujours le même résultat, sans produire d'effets de bord.

Autrement dit, elle ne modifie pas l'état du programme (pas de variables globales modifiées, pas d'entrées/sorties, etc.).

### Immutabilité

Que du `const` en gros

### Récursivité

rec sur le moindre truc

### Evaluation paresseuse

On exécure rien tant qu'on a pas besoin d'utiliser réellement le résultat

### Pas d'effet de bord

Cf. fns pures

### Exemple

Somme des carrés:

#### ENn mode Map-Reduce

```py
sum(x ** 2 for x in liste)
# ou
sum(
    map(lambda x: x ** 2, liste)
)
```

NB: `map` renvoie un `Generator`

```ocaml
List.fold_left (+) 0 (List.map (fun x -> x .* x) l)
```

#### En mode rec

```py
def norme2(liste):
    return liste[0]**2 + somme_des_carres_recursive(liste[1:]) if liste else 0
```

```ocaml
let norme2 l =
    match l
    | [] -> 0
    | a :: l' -> a .* a + norme2 l';;
```

### `map`, `filter`, `reduce`

Des fn usuelles hein

Fn $\lambda$ en Py: `addition = lambda x, y: x + y`

```py
a=[1,2,3,4]
b=[17,12,11,10]
print(list(
    map(lambda x, y: x + y, a, b)
))
# =>[18, 14, 14, 14]
```

```py
list(filter(lambda x: x<0, number_list))
```

```py
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# => 120 (factorielle)
```

Donc somme des carrés c aussi :

```py
reduce(lambda acc, x: acc + x, liste, 0)
```

## Principes de PySpark

Spark c en Scala (paradigme fn-el), ms y a un wrapper Python: PySpark.

La mm chose, juste :

- on fout la liste ds un `sc.parallelize`
- comme ça on peut appeler dessus des méthodes `.map(fn)`, `.filter(fn)`, etc,
- et `.collect()` pr re à une liste Python clasico.

```py
monRDD = sc.parallelize([1, 2, 3, 4])
print(monRDD.map(lambda n: n + 1).collect())
print(monRDD.filter(lambda n: (n % 2) == 0).collect())
```

## Spark versus Map-Reduce

### Comparaison à Hadoop

En Hadoop y a des tuples à faire, en Spark non wtf c fini les tuples, on ft dla bonne vieille programmation fn-elle.
L'autre diff avec Hadoop c de stocker les "RDD" en RAM alors que Hadoop stocke sur disque ses tuples.
La 3e c que c $\approx 10 \times$ + rapide (en partie dû au stockage en RAM).

Inventé en 2009 à Berkeley, devenu un projet dla Apache Foundation en 2013.

S'intègre au HDFS de Hadoop.
Fonctionne en standalone, en général chiant sous Windows (pas Unix-based).

### Archi Spark

Comme Hadoop : y a un "Spark Context" (un maître) qui se co au "Cluster Manager" (un K8s par ex) qui manage un cluster d'"executors" (des esclaves).

## Exemples PySpark

### `wc`

```py
#!/usr/bin/env python3
import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>", file=sys.stderr)
        exit(1)
    sc = SparkContext(appName="Spark WordCount")
    sc.setLogLevel("ERROR")
    lines = sc.textFile(sys.argv[1])
    counts = lines.flatMap(
        lambda x: x.split(" ")
    ).map(
        lambda x: (x, 1)
    ).reduceByKey(
        lambda v1, v2: v1 + v2
    )
    outputs = counts.collect()
    for word, count in outputs:
        print(f"{word}: {count}")
    sc.stop()
```

```bash
spark-submit --deploy-mode client --master local[2] PySpark_wc.py input/dracula
hadoop fs -ls sortie
hadoop fs -text sortie/part-00000
hadoop fs -rm -r -f sortie
```

### Transformations & Actions

- Transformations : `map`, `filter`, `flatMap`, `groupByKey`,
  `reduceByKey`, `aggregateByKey`, `pipe` et `coalesce`, etc.
- Actions : `reduce`, `collect`,
  `count`, `first`, `take`, `countByKey` et `foreach`.

## Lib PySpark

### Formats d'IO

- `rdd.wholeTextFiles`
- `rdd.saveAsPickleFile` et `rdd.pickleFile`
- `rdd.saveAsSequenceFile`

### Transformations

#### FlatMap

comme un map, sauf que la lambda dedans renvoie une séquence, et FlatMap concat ces séquences :

```py
A=sc.parallelize([2,3,4]).flatMap(lambda x:[x,x,x]).collect()
# =>[2, 2, 2, 3, 3, 3, 4, 4, 4]
B=sc.parallelize([1,2,3]).map(lambda x:[x,x,x]).collect()
# =>[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

#### union, intersection, distinct

Ds l'exemple là-dessous les `persist` c juste psk sinon, le calcul de `U` va consommer les deux générateurs donc D se retrouvera avec des générateurs épuisés.

```py
one=sc.parallelize(range(1,10))
two=sc.parallelize(range(5,15))
one.persist()
two.persist()
U=one.intersection(two).collect()
# =>[5, 6, 7, 8, 9]
D=one.union(two).distinct().collect()
# =>[8, 12, 4, 1, 13, 5, 9, 2, 14, 10, 6, 11, 3, 7]
```

#### Clef-valeur : groupByKey, reduceByKey, aggregateByKey

#### sortByKey, join

```py
names1=sc.parallelize(("abe","abby","apple")).map(lambda a: (a,1))
names2=sc.parallelize(("apple","beatty","beatrice")).map(lambda a: (a,1))
names1.persist()
names2.persist()

fulljoin=names1.join(names2).collect()
# =>[('apple', (1, 1))]
leftjoin=names1.leftOuterJoin(names2).collect()
# =>[('abe', (1, None)), ('apple', (1, 1)), ('abby', (1, None))]
rightjoin=names1.rightOuterJoin(names2).collect()
# =>[('apple', (1, 1)), ('beatrice', (None, 1)), ('beatty', (None, 1))]
```

#### cogroup, cartesian, pipe, coalesce, repartition

> _"C'est technique, j'vais pas en parler"_

### Actions

`reduce`, `collect`, `count`, `first`, `take`, `takeSample`, `takeOrdered`, `saveAsTextFile`, `saveAsSequenceFile`, `saveAsObjectFile`, `countByKey` et `foreach`.

####

```py
>>> 4 * sum([1 for x, y in [(r(), r()) for _ in range(1000000)] if x**2 + y**2 < 1]) / 1000000
3.142188
```

#### Shared variable

Si jms y en a besoin, c possible :

```py
broadcastVar = sc.broadcast([1, 2, 3])
broadcastVar.value
# => [1, 2, 3]
```

## EcoSystème Spark
