### Spécification du projet
L'interface graphique doit:
- pouvoir décrire une arborescence d'élements techniques.
- pouvoir placer ces elements techniques au sein de différents espaces et leurs donner des noms qui expriment les informations qui remontent (temperature, hygrométrie, etc).
- pouvoir composer des scénario qui permettront de manipuler des actionneurs en fonction de certains paramètres saisies dans les étapes précedentes.

Pour l'instant il peut y avoir 4 catégories d'élements téchniques:
- Raspberry Pi
- Arduino
- Capteur
- Actionneur

Il peut y avoir 3 types d'interfaces pour connecter ces élements téchniques:
- Wifi
- I2c
- GPIO
- Pin

Interconnection possible:

| Element Technique 1        | Element Technique 2           | Interfaces  |
| -------------------------- |:-----------------------------:| -----------:|
| Raspberry                  | Raspberry                     | Wifi, ?     |
| Raspberry                  | Arduino                       |   I2C       |
| Raspberry                  | Capteur/Actionneur            |    GPIO?        |
| Arduino                    | Capteur/Actionneur            | GPIO?, Pin  |



### Catalogue d'élements techniques
Chacune de ces catégories d'elements techniques fera réference à un catalogue de modeles disponible.

Ces catalogue seront partagés et enrichies par la communautée à travers un site Web dédié.

Cela permettra par exemple de disposer d'un grand nombre de capteurs ou de modèle d'arduino prédefinit.

Le site permettant de gérer ces catalogues fera office d'un autre projet, celui-ci se focalise sur le logiciel embarqué dans le raspberry maitre.



### Génération de l'application
A partir des ces informations l'application devra générer:
- les sketchs des arduinos préconfigurés pour récupérer les informations des capteurs/actionneurs qui lui son connectés
- le schéma de cablage des capteurs aux arduinos (Position des pin, etc)
- les fichiers de communications à embarquer sur les raspberry pi charger de l'échange de donnée maitre esclave
