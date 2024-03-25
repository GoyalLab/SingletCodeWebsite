==========================================
Benchmarking Doublet Detection Methods
==========================================

Simulation datasets
------------------------

To simulate doublets for benchmarking, we randomly selected the gene expression counts data from two cells that were found to be true singlets by singletCode. We averaged the counts from these two cells to generate simulated doublets and create datasets with various doublet percentages for benchmarking.

.. figure:: /images/Figure1C.png
   :scale: 100 %
   :alt: Workflow schematic of how raw data is processed to generate true singlets based on a barcode UMI cutoff and doublet removal based on singletCode specifications, followed by the simulation of doublets for benchmarking doublet detection methods. 
 
   *Workflow schematic of how raw data is processed to generate true singlets based on a barcode UMI cutoff and doublet removal based on singletCode specifications, followed by the simulation of doublets for benchmarking doublet detection methods.*

Benchmarking
------------------


We used these datasets to benchmark four doublet detection methods - scDblFinder, DoubletFinder, Scrublet and Hybrid.
 -  `scDblFinder <https://bioconductor.org/packages/release/bioc/html/scDblFinder.html>`_, DoubletFinder `DoubletFinder <https://github.com/chris-mcginnis-ucsf/DoubletFinder>`_, `Scrublet <https://github.com/AllonKleinLab/scrublet/>`_ and `Hybrid <https://github.com/kostkalab/scds>`_. 

We evaluated the AUPRC, AUROC, TNR, and doublet scores and calls of the four methods and found lower than expected performance for all methods. A plot of our results for AUPRC value is found below.

.. figure:: /images/Figure2A.png
   :scale: 100 %
   :alt: Color-coded boxplots of AUPRC value for all four doublet detection methods. Each boxplot is calculated from the AUPRC value after running the respective method on each sample of the dataset with actual doublet rate of 0.08 and expected doublet rate set to 0.05, 0.08, 0.1, 0.15, 0.2, and 0.25 where applicable. Dots represent the mean AUPRC value for a detection method grouped across all samples within a dataset. Lines represent standard deviation of the AUPRC values for a detection method across all samples within a dataset. Boxes span the first and third quartiles. Outliers are not depicted.

   *Color-coded boxplots of AUPRC value for all four doublet detection methods. Each boxplot is calculated from the AUPRC value after running the respective method on each sample of the dataset with actual doublet rate of 0.08 and expected doublet rate set to 0.05, 0.08, 0.1, 0.15, 0.2, and 0.25 where applicable. Dots represent the mean AUPRC value for a detection method grouped across all samples within a dataset. Lines represent standard deviation of the AUPRC values for a detection method across all samples within a dataset. Boxes span the first and third quartiles. Outliers are not depicted.*

   
We examined the consistency of doublet labeling across different doublet detection methods by introducing a 'similarity score'—a measure of the fraction of doublets identically classified by two methods. With an average similarity score of 0.66 across all datasets and methods, we observed variability in doublet detection.

.. figure:: /images/Figure4A.png
   :scale: 100 %
   :alt: Pairwise similarity score between all benchmarked methods. A score of 1 indicates perfect identity and a 0 indicates complete disagreement. Average similarity score across all methods and datasets is 0.66. 

   *Pairwise similarity score between all benchmarked methods. A score of 1 indicates perfect identity and a 0 indicates complete disagreement. Average similarity score across all methods and datasets is 0.66.*

We further evaluated doublet detection on ensemble doublet detection methods (hybrid, Chord) and across sequencing technologies (10X Genomics, Smart-seq3). For a more detailed evaluation of our results, refer to our paper. 

Heterogeneity effects
---------------------------

We wanted to know whether heterogeneity of a dataset affects the performance of doublet detection methods. Because heterogeneity can be impacted by many properties of a dataset, such as experimental design and data processing, we made conclusions based on heterogeneity within a sample. We did this by subsampling singlets and doublets within a single PC cluster for a sample (less heterogeneous, low Euclidean distance), and across all clusters for a sample (more heterogeneity, higher Euclidean distance). 

.. figure:: /images/Figure3B.png
   :scale: 100 %
   :alt:  Schematic of how transcriptionally similar and dissimilar cells are subsampled for subsequent within-sample heterogeneity determinations. A principal component analysis (left) was performed on each dataset and the first 30 PCs are used to identify Louvain clusters, represented by color. Transcriptionally similar (less heterogeneous) cells are identified from a single cluster and have a low Euclidean distance in PC space. Transcriptionally dissimilar (more heterogeneous) cells are identified from all clusters within the dataset and have a high average Euclidean distance in PC space. 

   *Schematic of how transcriptionally similar and dissimilar cells are subsampled for subsequent within-sample heterogeneity determinations. A principal component analysis (left) was performed on each dataset and the first 30 PCs are used to identify Louvain clusters, represented by color. Transcriptionally similar (less heterogeneous) cells are identified from a single cluster and have a low Euclidean distance in PC space. Transcriptionally dissimilar (more heterogeneous) cells are identified from all clusters within the dataset and have a high average Euclidean distance in PC space.*

singletCode for scATAC-seq doublet detection
------------------------------------------------

We evaluated our method's ability to assess doublet detection in scATAC-seq datasets using AMULET for a proof-of-concept analysis. We generated Watermelon-barcoded 10X Genomics Multiome datasets and applied AMULET to scATAC-seq fragments to categorize singlets and doublets. Concurrently, we identified true singlets in a barcoded scRNA-seq library from the same cells. By comparing the true negative and false positive rates between AMULET and singletCode across six datasets, we calculated AMULET's average true negative rate (TNR) at 0.924. Our results demonstrate that singletCode can be used to benchmark doublet detection in other modalities besides scRNA-seq.

.. figure:: /images/Figure4G.png
   :scale: 100 %
   :alt: Schematic for 10X Single Cell Multiome dataset workflow resulting in TNR calculation. The same cells in the Multiome dataset undergo scATAC-seq, scRNA-seq, and barcode sequencing. Barcodes were processed with singletCode to identify ground truth singlets while the respective fragments file from ATAC was used to label doublets with AMULET. The AMULET-labeled singlets were compared with ground truth singletCode singlets to calculate TNR.

   *Schematic for 10X Single Cell Multiome dataset workflow resulting in TNR calculation. The same cells in the Multiome dataset undergo scATAC-seq, scRNA-seq, and barcode sequencing. Barcodes were processed with singletCode to identify ground truth singlets while the respective fragments file from ATAC was used to label doublets with AMULET. The AMULET-labeled singlets were compared with ground truth singletCode singlets to calculate TNR.*

.. contents:: Contents:
   :local: