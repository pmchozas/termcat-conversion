#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:19:09 2024

@author: pmchozas
"""

from rdflib import Graph

import os

# Directorio que contiene los archivos TTL
data_path = "data/linked"

# Crear un grafo RDF
grafo = Graph()

# Iterar sobre los archivos en el directorio
for file in os.listdir(data_path):
    if file.endswith(".ttl"):
        # Construir la ruta completa al archivo
        file_path = os.path.join(data_path, file)
        
        # Cargar el archivo TTL en el grafo RDF
        grafo.parse(file_path, format="ttl")

# Realizar operaciones en el grafo RDF
# Por ejemplo, ejecutar consultas SPARQL en el grafo
query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dct: <http://purl.org/dc/terms/> 
    PREFIX lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#> 
    PREFIX lime: <http://www.w3.org/ns/lemon/lime#> 
    PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#> 
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
    PREFIX tc: <http://w3id.org/termcat-ld/> 
    PREFIX vartrans: <http://www.w3.org/ns/lemon/vartrans#> 
    
    
    SELECT *
    WHERE {
        tc:Noms_de_peixos_C108_%3Ci%3EScomber_Thynnus%3C%2Fi%3E_nc_sense a ontolex:LexicalSense ;
        vartrans:synonym ?synonym ;
        vartrans:translation ?translation .
        
    }
"""

results = grafo.query(query)

# Imprimir los resultados
for line in results:
    print(line)
