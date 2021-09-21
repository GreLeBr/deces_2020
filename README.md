Page available at : [page with graphs](https://grelebr.github.io/deces_2020/)

# Data analysis
- Document here the project: deces_2020
- Description: Deaths in 2020 in FRANCE
- Data Source: Public data made available by [INSEE](https://www.insee.fr/fr/information/4190491)
- Type of analysis: Analyzing public data

# Data sources

Following instructions from [france_geojson](https://github.com/gregoiredavid/france-geojson) , I rebuilt a geojson file of France using the IGN public data of June 2021 available at [IGN](https://geoservices.ign.fr/)telechargement  
and using the package [Mashaper](https://github.com/mbloch/mapshaper)  
The file in raw_data is stripped of many of the original file properties to get the file weight down and I used:  

 `mapshaper -i *.shp combine-files snap -proj wgs84 -simplify 1% weighted keep-shapes -merge-layers -o format=geojson precision=0.00001 commune_simp1.json`  
 
to make a file lighter

