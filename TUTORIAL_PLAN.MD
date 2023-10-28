Level 0: Introduction
Introduction to Geospatial objects
Talk about CRS and map distortions when working in WGS84
Introduction to GeoPandas
Introduction to OpenStreetMap data

Level 1: population in districts
(Warsaw data)
Load districts for Warsaw
Load population data for Warsaw
Join them

Level 2: population in buildings (approximation)
Load buildings for Warsaw (online with osmnx)
Interpolate population over buildings with floor information.
Map points into hexes and display a map with aggregated H3 values

Level 3: green one boxes
(OneBox dataset)
Load OneBoxes dataset
Show them on map
Filter them to the Warsaw only
Buffer each OneBox with 1km radius (BE CAREFUL ABOUT BUFFER IN GEOPANDAS, USE BUFFER FUNCTION FROM SRAI)
Load greenery data from OSM (online with osmnx) and trees
Intersect greenery with buffers individually
Calculate fraction of the greenery in the buffers
Find one with most greenery in the radius

Level 4: contextual count embedder for bikes
(Bike dataset from Hugging Face)
Load geofabrik features (or base features) for Warsaw (here users can use other cities if the want)
Use contextual count embedder in hexes
Simple predict if station exists or not
Plot on map probabilities and points


Level 5: harder embeddings with hex2vec or geovex and distance calculation
(Porto dataset - CLEAN IT !!!)
Load trips hexes dataset
Find area of interest from hexes - map to points and maybe use administrative boundary regionizer
Load features for Porto and regions around (here we can download PBF)
Train embedder and generate embeddings for dataset
Create pairs and train based on starting hex embedding to predict ending hex embedding (minimize distance between predicted vector and end embedding), duplicate pairs with multiple trips.
Show data on the map (CREATE A DECK.GL APPLICATION FOR HIGHLIGHTING HEXES ON CLICK AND SHOWING ARCS / COLOUR SIMILLAR HEXES)

Transfer learning of the model to Warsaw (or other city) and again show it on the map.




 Wykorzystując informacje publiczne udostępnione w serwisie otwarte dane po warszawsku, należy:

    zamieścić informacje o źródle danych podając nazwę: Miasto Stołeczne Warszawa oraz, jeśli to możliwe, adres URL serwisu otwarte dane po warszawsku: http://api.um.warszawa.pl
    podać datę wytworzenia oraz pozyskania informacji publicznej;





https://warszawa.stat.gov.pl/publikacje-i-foldery/inne-opracowania/panorama-dzielnic-warszawy-w-2021-r-,5,23.html



https://stat.gov.pl/obszary-tematyczne/ludnosc/ludnosc/powierzchnia-i-ludnosc-w-przekroju-terytorialnym-w-2022-roku,7,19.html