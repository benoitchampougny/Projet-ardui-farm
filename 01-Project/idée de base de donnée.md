----------------------------------------------------------------------------------------------------------------------------------
CONFIGURATION

Arduino : models.Network.Arduino
- ID
- Adresse I2C
- ID du Raspberry pi auquel il est connecté en I2C
- ID ouvrage technique
- Liste des PIN I/O utilisé
- Nom de la carte

Raspberry pi :
- ID
- Adresse I2C
- ID ouvrage technique
- Liste des PIN I/O utilisé
- Liste des PIN Analogic utilisé
- Nom de la carte

Actionneurs : models.Network.Actuator
- ID
- Nom de l’actionneur
- ID driver actionneur
- ID appellation Fonctionnalités
- ID du temps réel actionneurs
- ID de la carte arduino ou du raspberry pi auquel il est connecté
- ID du volume
- ID de la surface
- ID du reseau
- ID du point de production
- Numéros de PIN*
- Puissance

Capteurs : models.Network.Sensor
- ID
- Nom du capteur
- ID driver capteur
- ID de la carte arduino ou du raspberry pi auquel il est connecté
- ID de la fonction capteur
- ID temps réel mesure
- ID du volume
- ID de la surface
- ID du reseau
- ID du point de production
- Délais d’attente de la mesure
- Numéros de PIN

Scenarios :
- ID
- Nom de la fonction
- ID driver scenario
- ID du temps réel scenarios
- ID des capteurs
- ID des actionneurs
- ID seuil
- ID Planning
- ID du volume
- ID de la surface
- ID du reseau
- Ordre de priorité

Scenarios de supervision et gestion des priorités:
- ID
- Nom de la fonction
- ID driver scenario de supervision et gestion des priorités
- ID du temps réel scenarios de supervision et gestion des priorités
- ID des scenarios
- ID seuil
- ID Planning
- ID du volume
- ID de la surface
- ID du reseau

Seuil :
- ID
- Nom du seuil
- ID temps réel seuil
- ID appelation mesures
- Seuil mini
- Seuil maxi

Planning :
- ID
- Plage de fonctionnement

Sketch :
- ID
- ID arduino
- Version
- Nombre de bit retourné par le sketch
- Nombre de bit attendue par le sketch
- sketch

----------------------------------------------------------------------------------------------------------------------------------

DESCRIPTION DE L'ENVIRONNEMENT

Volumes :
- ID
- Nom du volume
- ID du volume parent
- ID du ou des surfaces presente dans le volume

Surfaces :
- ID
- Nom de la surface
- ID de la surface parent
- ID du ou des volumes presents sur la surface

reseau :
- ID
- Nom du réseau
- ID de l’élément (eau,air...)

point de production (est equivalent à un volume):
- ID
- Nom du point de production
- ID du volume parent

Point de consommation :
- ID
- Nom du point de consomation
- ID du volumes
- ID de la surfaces

section de Réseau :
- ID
- ID du réseau
- ID des sections réseau connecté à celui ci
- ID de l'actionneur
- ID du capteur
- ID du ou des points de production
- ID du ou des points de consommation (peut être volume, surface ou autre)

----------------------------------------------------------------------------------------------------------------------------------

LIBRAIRIE COMMUNAUTAIRE APPELLATION :

Fonctionnalités :
- ID
- Nom (chauffe, refroidi, alerte, arrose, humidifie, ventile … )

Mesures :
- ID
- Grandeur physique (température, humidité … )
- Unité de mesures (°c, % ... )
- précision

Elément :
- ID
- Nom (eau, air, engrais, aliment pour animaux … )

Type technique :
- ID
- Nom (tuyaux cuivre, tuyaux PE, cuve, puit, pompe, capteur température, pompe, carte contrôleur, chauffage … )

Marque :
- ID
- Nom (Arduino, Gardena, Keyes Robot, Adafruit … )

Modéle :
- ID
- ID Marque
- Nom (uno, due, dht 22, … )

----------------------------------------------------------------------------------------------------------------------------------

LIBRAIRIE COMMUNAUTAIRE DRIVER:

Controleur :
- ID
- ID appellation modéle
- nombre de PIN I/O
- nombre de PIN analogique
- numero de pin SDA (i2c)
- numero de pin SCL (i2c)

Actionneur :
- ID
- ID appellation modéle
- ID appellation Fonctionnalités
- ID appelation type techniques
- Fonctionnement (digital ou analogique)
- Nombre de PIN
- Partage des données (oui/non)
- Descriptif

Capteur :
- ID
- Nom de la fonction du capteur
- GPIO / arduino
- ID appellation modéle
- ID appelation de mesure
- ID appelation type technique
- Fonctionnement (digital ou analogique)
- Nombre de mesures
- Nom des variables des mesures
- Nombre de charactere maximum par mesure
- Nombre de PIN
- Plage de fonctionnement minimum
- Plage de fonctionnement maximum
- ID du calibrage
- Partage des données (oui/non)
- Descriptif
- code python (gpio)
- sketch void setup(arduino)
- sketch void loop(arduino)
- sketch include (librarie arduino)
- sketch define (definis le numero de pin arduino)

Variables extérieur :
- ID
- Nombre de variable
- Importation internet (OUI/NON)
- ID Appellation mesure
- nom des variable
- Partage des données (oui/non)
- Descriptif
- code python

Scenario :
- ID
- Nom de la fonction
- Nombre d'argument
- ID appellation de mesure (capteur)
- ID des fonctionnalités (actionneur) (chauffe, ventile...)
- ID Variables extérieur
- ID appellation de mesure (seuil)
- Nombre de planning utilisé
- Nom des plannings
- influence (le reseau, la surface, le volume ou les 2)
- ID appellation element (si reseau)
- ID appelation fonctionnalités (produite)
- Partage des données (oui/non)
- Descriptif
- code python

Scenario de supervision et gestion des priorités:
- ID
- Nom de la fonction
- Nombre d'argument
- ID scenario
- ID des fonctionnalités (produite par les autres scenario)
- ID Variables extérieur
- ID appellation de mesure (seuil)
- Nombre de planning utilisé
- Nom des plannings
- influence (le reseau, la surface, ou le volume)
- ID appellation element (si reseau)
- ID appelation fonctionnalités (produite)
- Partage des données (oui/non)
- Descriptif
- code python

----------------------------------------------------------------------------------------------------------------------------------

HISTORIQUE

Mesure :
- Date et heure
- ID temps réel Mesure
- Mesure 1
- Mesure 2
- Mesure 3
- Mesure 4
- Mesure 5
- Etc…

Capteur :
- Date et heure
- ID temps réel capteur
- En service (Oui/Non)
- En fonction (Oui/Non)
- En maintenance (Oui/Non)
- En calibrage (Oui/Non)
- Etc …

Actionneur :
- Date et heure
- ID temps réel actionneur
- En service (Oui/Non)
- En fonction (Oui/Non)
- En maintenance (Oui/Non)
- Etc …

Scenarios :
- Date et heure
- ID temps réel scenario
- En service (Oui/Non)
- En fonction (Oui/Non)
- Etc …

Seuil :
- Date et heure
- ID temps réel seuil
- Seuil mini dépassé (Oui/Non)
- Seuil maxi dépassé (Oui/Non)
- Etc …

Système :
- Date et heure
- ID temps réel alerte système
- ID libellé


TEMPS REEL
Mesure :
- ID
- Mesure 1
- Mesure 2
- Mesure 3
- Mesure 4
- Mesure 5
- Etc…

Capteur :
- ID
- En service (Oui/Non)
- En fonction (Oui/Non)
- En maintenance (Oui/Non)
- En calibrage (Oui/Non)
- Etc …

Actionneur :
- ID
- En service (Oui/Non)
- En fonction (Oui/Non)
- En maintenance (Oui/Non)
- Etc …

Scenario :
- ID
- En service (Oui/Non)
- En fonction (Oui/Non)
- Etc …

Données complémentaires :
- ID
- donnée 1
- donnée 2
- donnée 3
- donnée 4
- Etc …

Seuil :
- ID
- Seuil mini dépassé (Oui/Non)
- Seuil maxi dépassé (Oui/Non)
- Etc …

Système :
- ID
- libellé
- état (deb/fin)

----------------------------------------------------------------------------------------------------------------------------------

DONNEES ANNEXES :

Fiche contact :
- ID
- Nom
- Prénom
- Adresse
- Numéro de téléphone fixe
- Numéro de téléphone mobile
- Adresse mail principal
- Adresse mail secondaire
- Niveau de droit d’accès
- Mot de passe

Téléphone à contacter en cas d’urgence:
- ID
- ID fiche contact
- Ordre de priorité

Mail à contacter en cas d’urgence:
- ID
- ID fiche contact
- Ordre de priorité

Téléphone pour les rapports journaliers :
- ID
- ID fiche contact

Mail pour les rapports journaliers :
- ID
- ID fiche contact

Sketch généré :
- ID
- ID Arduino
- ID sketch
- Version du sketch

Mail d’envoie:
- ID
- Adresse mail
- Mot de passe
- Adresse SMTP

----------------------------------------------------------------------------------------------------------------------------------
