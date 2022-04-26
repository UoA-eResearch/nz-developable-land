# nz-developable-land
Calculating the amount of developable land at different slope and distance thresholds from Functional Urban Areas (FUA) in New Zealand For Dr Ryan Greenaway-McGrevy (Economics » Faculty of Business and Economics) 

## Installation
packages and dependencies handled by conda

`conda create --name calc-developable-land`

`conda activate calc-developable-land`

`conda install --file requirements.txt`

`python -m ipykernel install --user -name=calc-developable-land`

`jupyter notebook`

## Processing 
- Step0 - removing undevelopable land (waterbodies) and generating slope images for each FUA
- Step01_mp - calculating developable area (sqkm) under given slope and distance thresholds 

## data sources
- 15m Digital elevation model for New Zealand, developed by School of Surveying, University of Otago https://www.otago.ac.nz/surveying/research/geospatial/otago040574.html#nzsosdem Tiles available to download free via Koordinates https://koordinates.com
- FUA coordinates (FUA_coordinates.xlsx)
- NZ landcover database (lcdb-v50-land-cover-database-version-50-mainland-new-zealand.shp) https://lris.scinfo.org.nz/layer/104400-lcdb-v50-land-cover-database-version-50-mainland-new-zealand/




