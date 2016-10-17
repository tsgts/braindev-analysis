# braindev-analysis
Deep learning analysis of prenatal gene expression in neurological animal models.
## The Data
This project focuses on the analysis of two formats of data: matrices displaying normalized expression of a gene over several stages of development, over neuroanatomical regions, and raw images of ISH (in situ hybridization) results for genes over brain sections. 
## Sources and Downloading
The genes in human development were downloaded from http://www.brainspan.org/static/download.html through the "RNA-Seq Gencode v10 summarized to genes" option.
For the developing mouse genes, there is no single download file, meaning that a list of genes must first be obtained.
```
http://help.brain-map.org/display/api/Example+Queries+for+Experiment+Metadata#ExampleQueriesforExperimentMetadata-AllDevelopingMouseBrainGenesincommadelimitedformat
## Methodology
```
Unsupervised image clustering will be implemented using the TensorFlow framework.
