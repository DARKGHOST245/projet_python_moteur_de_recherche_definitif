Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... import re
... from word_indexer import charger_index
... 
... def recherche_mot(index, mot):
...     return index.get(mot.lower(), [])
... 
... def recherche_multiple(index, mots, mode='OU'):
...     mots = [mot.lower() for mot in mots]
...     if mode == 'OU':
...         resultats = []
...         for mot in mots:
...             resultats.extend(index.get(mot, []))
...         return resultats
...     elif mode == 'ET':
...         # Intersection des ensembles de résultats
...         ensembles = [set(tuple(sorted(d.items())) for d in index.get(mot, [])) for mot in mots]
...         if not ensembles:
...             return []
...         communs = set.intersection(*ensembles)
...         return [dict(t) for t in communs]
...     else:
...         raise ValueError("Mode inconnu : utilisez 'OU' ou 'ET'.")
... 
... def recherche_regex(index, pattern):
...     regex = re.compile(pattern)
...     resultats = []
...     for mot in index:
...         if regex.match(mot):
...             resultats.extend(index[mot])
...     return resultats
... 
... 
... 
