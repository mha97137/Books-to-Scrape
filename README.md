# Books-to-Scrape

_scrape du site  Books to Scrape_

_PROJET 2 OPPENCLASSROOMS - Développeur d'application - Python_

--------------------------------------------------------------------
### Pré-requis  📋

_connexion Interne requise_

_travail effectué avec ubuntu et python 3.8_

-------------------------------------------------------------------


## A - création d'environnement virtuel  🚀

_La première chose que nous créons un dossier où tout sera enregistré, 
dans mon cas je l'appellerai "EV"_
```
mkdir EV
```

_installation environnement virtuel dans le dossier "EV" je l'appellerai "ENV"_
```
python -m venv ENV                
```

_l'environnement virtuel est créé avec le nom ENV en principe il n'a pas de bibliothèques installée_

_activation environnement virtuel_
```
source ENV/bin/activate
```

_pouvons regarder à l'intérieur tout installé_
```
pip freeze
```

_voir bibliothèques installées_
```
pip list
```

_désactivation environnement virtuel_
```
deactivate
```

_nous avons vu comment créer un environnement virtuel, activer et le désactiver_

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
## B - configuration environnement virtuel 🔧

_dans mon cas, je dois installer trois bibliothèques_

_activation environnement virtuel_
```
source ENV/bin/activate
```

_installation bibliothèques requises_

```
pip install requests
pip install beautifulsoup4
pip install pandas
```

_voir tout installé_
```
pip freeze
```
_voir bibliothèques installées_
```
pip list

```
_possibilité crée fichier "requirements.txt"_
```
pip freeze > requirements.txt
```
_possibilité installer des bibliothèques à partir fichier "requirements.txt"_
```
pip install -r requirements.txt
```

_une fois que tout est installé, tournerons le code d'application_

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
## Exécution des tests  ⚙️
_run the code:_

```
python projet2.py
```

------------------------------------------------------------------------------------
## Resultat  🔩
_un dossier "P2" sera créé avec deux sous-dossiers_ 
 
 _- dossier COUVERTURE:  image couverture tous les livres, format .jpg_
 
 _- dossier CSV:   les fichiers sont stockés par catégorie contiennent informations précises des livres, format .csv_ 



_.CSV CONTENT:_

_product page url_

_universal product code (upc)_

_title_

_price including tax_

_price excluding tax_

_number available_

_product description_

_category_

_review rating_

_image url_



## Auterurs ✒️
* **Alberto Munumer** - [mha97137](https://github.com/mha97137/)

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
## License 📄
_Ce projet est informatif, apprentissaget & usage personnel._
