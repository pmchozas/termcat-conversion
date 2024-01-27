# Towards the Development a Mapping-based Conversion Platform for Terminological Resources

This is the repository for the Termcat use case of the Automatic Terminology Converters into RDF.

## About the project

In the era of Linguistic Data Science, language resources are increasingly gaining attention. Particularly interesting are those that represent knowledge of a certain domain, such as terminologies, taxonomies, thesauri, or glossaries. For this reason, their representation in the structured, open and interoperable formats of the Semantic Web (SW) is of utmost  importance. Despite the advances made on the publication of such resources in the Linguistic Linked Open Data cloud, their conversion still poses some problems with regard to resource-specific particularities, which might not be covered by current models. Furthermore, the creators of language resources exhibit limited familiarity with software formats and models, which prevents them from undergoing such an endeavour. In this project, we analyse some of these representation needs and propose the design of a mapping-based platform that automatically converts terminological resources to RDF. In addition, we intend to implement an algorithm that translates Natural Language queries into SPARQL, to help non-expert users easily access the converted data through.

## Our proposal: a mapping-based conversion platform

In order to ease the data conversion to the producers of terminological resources, we propose a mappings-based conversion platform. To this aim, two complementary modules will be built: a Data Conversion Module, and a Data Querying Module. The former will be in charge of transforming the terminological resources into RDF, using Ontolex-lemon as the core ontology. The latter, on the other hand, will enable users to query the data transformed by the Data Conversion Module.

<p align="center">

<img src="https://github.com/pmchozas/termcat-conversion/assets/37108648/d4303caa-273a-4f95-a8b1-72899f087bd7" width=80% >

</p>

### Platform Status
27/1/24: The proposed platform is not yet fully implemented. We are about to finish the Data Conversion module. The Data Querying module is still not developed. 
