# Cheat Sheet : Nettoyage et Traitement des Données Clients

Ce cheat sheet fournit un guide complet pour nettoyer et traiter des données clients (énergétiques, numériques, tabulaires, etc.). Il couvre les concepts clés, les bonnes pratiques, ainsi que des exemples concrets, avec des comparaisons entre mauvaises et bonnes approches.

## 1. Objectifs et Concepts Fondamentaux

### 🎯 Objectif principal
Assurer que les données brutes deviennent propres, cohérentes et exploitables pour l’analyse et la prise de décision.

### 📌 Principes clés
- **Qualité des données** : Exactitude, complétude, cohérence, actualité.
- **Reproductibilité** : Un pipeline de nettoyage doit toujours produire les mêmes résultats sur un même jeu de données.
- **Automatisation** : Intégration dans des pipelines ETL (**Extract, Transform, Load**).

---

## 2. Étapes du Processus de Nettoyage

### a. Exploration et Profilage des Données
🎯 **Objectif** : Comprendre la structure et la qualité initiale des données.

**Actions** :
```python
# Inspection générale
df.head()
df.info()
df.describe()
```

---

### b. Traitement des Valeurs Manquantes

**Méthodes :**
- **Suppression** : `dropna()` si la perte de données est négligeable.
- **Imputation** :
  - Numériques : Moyenne, médiane, interpolation.
  - Catégoriques : Valeur la plus fréquente ou "inconnue".

**Exemples :**
❌ **Mauvais Exemple** :
```python
# Ignorer les valeurs manquantes
df = pd.read_csv('data.csv')
```
✅ **Bon Exemple** :
```python
# Imputation des valeurs manquantes pour une colonne numérique 'consommation'
df['consommation'] = df['consommation'].fillna(df['consommation'].mean())
```

---

### c. Gestion des Valeurs Aberrantes (Outliers)

**Méthodes :**
- **Détection** : Statistiques (IQR, Z-score) ou visualisation (boxplots).
- **Traitement** : Correction par interpolation, transformation ou filtrage.

❌ **Mauvais Exemple** :
> Accepter un pic de consommation sans vérification.

✅ **Bon Exemple** :
> Détection avec un boxplot, puis correction ou suppression.

---

### d. Normalisation et Standardisation
🎯 **Objectif** : Assurer l’homogénéité des formats et des unités.

**Actions :**
- Conversion d’unités : ex. **MWh → kWh**
- Standardisation des dates : `pd.to_datetime()`
- Normalisation : Transformation logarithmique ou scaling

✅ **Bon Exemple** :
```python
def convert_to_kwh(value, unit):
    return value * 1000 if unit == 'MWh' else value

df['consommation'] = df.apply(lambda row: convert_to_kwh(float(row['consommation']), row['unite']), axis=1)
```

---

### e. Déduplication et Correction des Incohérences

**Actions :**
- **Déduplication** : `drop_duplicates()`
- **Correction des incohérences** : Harmonisation des valeurs

✅ **Bon Exemple** :
```python
# Suppression des doublons
df = df.drop_duplicates()
```

---

## 3. Traitement Spécifique Selon le Type de Données

### a. Données Énergétiques (Séries Temporelles)
**Spécificités :**
- Vérification de la régularité des séries temporelles.
- Imputation avec interpolation linéaire ou temporelle.

✅ **Exemple :**
```python
# Conversion des timestamps et réindexation
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp').resample('H').mean()
df = df.interpolate(method='time')
```

---

### b. Données Numériques (Mesures Continues)
✅ **Standardisation des valeurs :**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['mesure1', 'mesure2']] = scaler.fit_transform(df[['mesure1', 'mesure2']])
```

---

### c. Données Tabulaires (CSV, Excel, etc.)
✅ **Fusion de données multiples :**
```python
df1 = pd.read_csv('clients.csv')
df2 = pd.read_csv('factures.csv')
df_merged = pd.merge(df1, df2, on='client_id', how='inner')
```

---

## 4. Automatisation et Tests

### 🚀 Automatisation du Pipeline
- **Orchestration ETL** : Airflow, Luigi
- **Scripts réutilisables et modulaires**

### 🧪 Tests Automatisés
- **Tests unitaires** : Vérifier les fonctions individuelles.
- **Tests d’intégration** : Vérifier l’ensemble du pipeline.

✅ **Exemple de test avec Pytest :**
```python
def test_convert_to_kwh():
    assert convert_to_kwh(1, 'MWh') == 1000
    assert convert_to_kwh(500, 'kWh') == 500
```

---

## 5. Bonnes Pratiques

### 📖 Documentation
- Ajouter des **commentaires** et **logs** pour tracer les modifications.

### 🔄 Reproductibilité
- S’assurer que le pipeline peut être exécuté avec des résultats identiques.

### 📊 Surveillance et Maintenance
- Mettre en place des **alertes** pour détecter anomalies et changements de schéma.

---

## 🔥 En résumé

- **Concepts fondamentaux** du nettoyage de données.
- **Étapes concrètes** : exploration, valeurs manquantes, outliers, normalisation, déduplication.
- **Exemples pratiques** en Python avec Pandas.
- **Automatisation et tests** pour garantir la fiabilité.

📌 Ce cheat sheet est une **ressource essentielle** pour préparer un **entretien technique** ou structurer un **pipeline de nettoyage de données** 🚀 !
