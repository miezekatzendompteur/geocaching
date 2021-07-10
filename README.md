# geocaching
Script to solve the set of geocaches with the name "Schach-Mattinger Runde" from WarriorFoxes

This script works in this order:

1. Login to geocaching.com
2. This script loads the cachenames from "https://www.geocaching.com/play/search?types=8&a=0&sc=False&owner[0]=WarriorFoxes&sort=PlaceDate&asc=False"
3. Load the single caches and extract the parameters: coordinates, answers of the cache description
4. Save the parameters to a csv-file

Change the username and password to your own login credentials

This script was written with the jupyter notebook
