# geocaching
Script to solve the set of geocaches with the name "Schach-Mattinger Runde" from WarriorFoxes

This py-script works in this order:

1. Login to geocaching.com
2. This script loads the cachenames from "https://www.geocaching.com/play/search?types=8&a=0&sc=False&owner[0]=WarriorFoxes&sort=PlaceDate&asc=False"
3. Load the single caches and extract the parameters: coordinates, answers of the cache description
4. Save the parameters to a csv-file

The basic-script was created under libreOffice. The basic script creates N and E coordinates from the decimal values.

Workflow

1. run the py-script
2. open csv-file in libreOffice or openOffice
3. open macro editor and import the bas-file
4. run the basic macro

Change the username and password to your own login credentials

This script was written with the jupyter notebook
