### Spécification du projet
L'interface graphique doit:
- pouvoir décrire une arborescence d'éléments techniques.
- pouvoir placer ces éléments techniques au sein de différents espaces et leurs donner des noms qui expriment les informations qui remontent (température, hygrométrie, etc).
- pouvoir composer des scénario qui permettront de manipuler des actionneurs en fonction de certains paramètres saisies dans les étapes précédentes.

Pour l'instant il peut y avoir 4 catégories d'éléments techniques:
- Raspberry Pi
- Arduino
- Capteur
- Actionneur

Il peut y avoir 3 types d'interfaces pour connecter ces éléments techniques:
- Wifi
- I2c
- GPIO
- Pin

Interconnexions possible:

| Élément Technique 1        | Élément Technique 2           | Interfaces  |
| -------------------------- |:-----------------------------:| -----------:|
| Raspberry                  | Raspberry                     | Wifi, ?     |
| Raspberry                  | Arduino                       |   I2C       |
| Raspberry                  | Capteur/Actionneur            |    GPIO?        |
| Arduino                    | Capteur/Actionneur            | GPIO?, Pin  |



### Catalogue d'éléments techniques
Chacune de ces catégories d'éléments techniques fera référence à un catalogue de modèles disponible.

Ces catalogues seront partagés et enrichies par la communauté à travers un site Web dédié.

Cela permettra par exemple de disposer d'un grand nombre de capteurs ou de modèles d'Arduino prédéfinis.

Le site permettant de gérer ces catalogues fera office d'un autre projet, celui-ci se focalise sur le logiciel embarqué dans le Raspberry.



### Génération de l'application
A partir des ces informations l'application devra générer:
- les sketchs des Arduinos pré-configurés pour récupérer les informations des capteurs/actionneurs qui lui son connectés
- le schéma de câblage des capteurs aux Aarduinos (Position des pin, etc)
- les fichiers de communications à embarquer sur les Raspberry Pi charger de l'échange de donnée maître esclave


