**Lancer le serv**, en précisant où est le volume avec les données en dur :

```bash
mongod --dbpath c:\data\db
```

---

**Lancer le client CLI** :

```bash
mongosh
```

puis pr se placer ds la bonne db :

```
use mongoLab
```

Là on peut taper nos queries en (pseudo- ?) javascript :

```js
db.velov_geo.find().pretty();
```

---

**Importer** une collection (~table), depuis un JSON, ds une db existante (le contenu seulement, y a pas de validation d'un schema) :

```bash
mongoimport --db mongoLab --collection velov_geo --file "velov_geo.json"
```
