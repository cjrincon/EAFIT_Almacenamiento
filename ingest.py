import sys
import os
os.system("curl https://cdn.buenosaires.gob.ar/datosabiertos/datasets/calidad-de-aire/calidad-de-aire-2017.csv > calidad_del_aire.csv")
os.system("aws s3 cp calidad_del_aire.csv s3://trabajo1-datalake/raw/calidad_del_aire/calidad_del_aire.csv")
