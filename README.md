# braindev-analysis
Deep learning analysis of prenatal gene expression in neurological animal models.
## The Data
This project focuses on the analysis of two formats of data: matrices displaying normalized expression of a gene over several stages of development, over neuroanatomical regions, and raw images of ISH (in situ hybridization) results for genes over brain sections. 
## Sources and Downloading
### Genes in Human Brain Development
The genes in human development were downloaded from http://www.brainspan.org/static/download.html through the "RNA-Seq Gencode v10 summarized to genes" option (http://www.brainspan.org/api/v2/well_known_file_download/267666525).
### Genes in Mouse Brain Development
For the developing mouse genes, there is no single download file, meaning that a list of genes must first be obtained. The "Example Queries for Experiment Metadata" page (http://help.brain-map.org/display/api/Example+Queries+for+Experiment+Metadata) provides a link for how to obtain this preliminary list, which is found at:
```
http://help.brain-map.org/display/api/Example+Queries+for+Experiment+Metadata#ExampleQueriesforExperimentMetadata-AllDevelopingMouseBrainGenesincommadelimitedformat
```
## Methodology
Unsupervised image clustering will be implemented using the TensorFlow framework.
