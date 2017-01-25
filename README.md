# braindev-analysis
Unsupervised analysis of gene expression in neurological animal models.
## Summary
The focus of this project is to compare relative landscapes of expression in developing mouse and human brains. In particular, this project makes use of dimensionality reduction to apply powerful clustering methods to a 2-dimensional representation of expression data. By comparing these derived clusterings, this project was able to assess the similarity of expression between mouse and human brains without direct analysis, which requires assumptions of homologous developmental timepoints and regions. The results of this study suggest a high divergence between the two organisms' expression profiles that is explained by widespread discrepancies at the local (i.e region and timepoint-specific) levels of expression.
## Sources of Data
### Genes in Human Brain Development
The genes in human development were downloaded from http://www.brainspan.org/static/download.html through the "RNA-Seq Gencode v10 summarized to genes" option (http://www.brainspan.org/api/v2/well_known_file_download/267666525) as a .zip file. The unpacked file is in this repository at allen_data/dev_human/normalized_genes. The matrix of expression values is zipped in order to comply with GitHub's file size limits.
### Genes in Mouse Brain Development
For the developing mouse genes, there is no single download file of expression values, meaning that a list of genes must first be obtained. The "Example Queries for Experiment Metadata" page (http://help.brain-map.org/display/api/Example+Queries+for+Experiment+Metadata) provides a link for how to obtain this preliminary list, which is found at:

```
http://help.brain-map.org/display/api/Example+Queries+for+Experiment+Metadata#ExampleQueriesforExperimentMetadata-AllDevelopingMouseBrainGenesincommadelimitedformat
```

A copy of this list may be found in this repository at allen_data/dev_mouse/all_the_genes.csv.
Alternatively, a comma-separated-values (csv, openable in Excel) list of all 2107 genes may be found at
```
http://api.brain-map.org/api/v2/data/Gene/query.csv?criteria=products[id$eq3]&num_rows=3000
```
The developing mouse brain expression matrix data for a list of genes may be downloaded using the provided RESTful Model Access (RMA) pipeline. For instance, expression values for FOXP2 and SHH (with IDs 76994 and 20186, from all_the_genes.csv) can be found using the below query:

```
http://api.brain-map.org/api/v2/data/query.csv?criteria=model::StructureUnionize,rma::criteria,section_data_set[delegate$eqfalse]%28genes[id$in%2776994%27,%2720186%27],specimen%28donor%28age[name$in%27E11.5%27,%27E13.5%27,%27E15.5%27,%27E18.5%27,%27P4%27,%27P14%27,%27P28%27]%29%29%29,structure%28structure_sets_structures%28structure_set[name$eq%27Developing%20Mouse%20-%20Coarse%27]%29%29&tabular=genes.id,ages.days,structures.acronym,structures.name,structures.graph_order,structure_unionizes.expression_energy&num_rows=10000000
```

This query returns the expression values for FOXP2 and SHH in seven developmental stages E11.5, E13.5, E15.5, E18.5, P4, P14, and P28 in eleven coarse-level structures. These structures are the rostral secondary prosencephalon (RSP), telencephalic vesicle (Tel), peduncular (caudal) hypothalamus (PHy), prosomeres 1, 2, and 3 (p1, p2, and p3), the midbrain (M), the prepontine and pontine hindbrains (PPH and PH), the pontomedullary hindbrain (PMH), and the medullary hindbrain (MH).

When querying the API, a useful reference is the class hierarchy page (http://api.brain-map.org/class_hierarchy), which details the attributes of each parameter. 

The search may also be restricted to a subset of the eleven regions. For instance, expression of FOXP2 and SHH in the seven stages, but only in the rostral secondary prosencephalon may be found at 

```
http://api.brain-map.org/api/v2/data/query.csv?criteria=model::StructureUnionize,rma::criteria,section_data_set[delegate$eqfalse](genes[id$in%2776994%27,%2720186%27],specimen(donor(age[name$in%27E11.5%27,%27E13.5%27,%27E15.5%27,%27E18.5%27,%27P4%27,%27P14%27,%27P28%27]))),structure(structure_sets_structures(structure[acronym$in%27RSP%27]))&tabular=genes.id,ages.days,structures.acronym,structures.name,structures.graph_order,structure_unionizes.expression_energy&num_rows=10000000
```

The image URLs for the expression matrices also follow a regular format, which is developingmouse.brain-map.org/expressionSummaries/[GENE_ID].png. The matrix_downloader.py script automatically downloads these images from the website into the dev_mouse/expression_matrices/ directory. 

Additionally, the precise numerical values may be downloaded using a Ruby script supplied by the Allen Institute's [API example repository](https://github.com/AllenBrainAtlas/api-examples). The devmouse_histogram_values.rb program was used to compile the devmouse_histogram_values.csv file. **Note: This file has been sorted by gene name in order to group genes with each other. The original file produced from running devmouse_histogram_values.rb is unsorted.** The expression values returned by this script were the ones used in the analysis.

These numerical values can be used to construct heatmaps similar to the ones provided by the Allen Brain Atlas. First, the expression values are transformed to their base 10 logarithm (log_mouse.py). The mouse_filter.py program then filters for genes that have samples from all seven stages (E11.5, E13.5, E15.5, E18.5, P4, P14, and P28) of development. The mouse_heatmap program then constructs and saves the heatmaps to the /figures/dev_mouse/heatmaps/ directory with the help of the Seaborn data visualization library. A total of 2012 heatmaps were generated.

Mouse<img src="https://raw.githubusercontent.com/kevin-who/braindev-analysis/master/figures/dev_mouse/heatmaps/Foxp2.png" width="200"/>Human<img src="https://raw.githubusercontent.com/kevin-who/braindev-analysis/master/figures/dev_human/heatmaps/FOXP2.png" width="200"/> 

## Methodology
### Gene selection and pre-processing

Genes with similar sequence, origin, and products (orthologs) were identified by comparing a list of the human and mouse genes. Incomplete data were also eliminated in the process. Comparison and selection resulted in a list of 1,912 genes that were present in both organisms' datasets without missing data values. The expression values for each dataset were then transformed by taking the base 2 logarithm in order for a more normal distribution, and these resultant values were further transformed to fit in the [-1,1] interval for subsequent analysis.

### Preliminary analysis

Preliminary analysis of the data consisted of analysis of the expression values using existing methods, namely correlation clustering.

### Autoencoder

### Comparison of clusters
