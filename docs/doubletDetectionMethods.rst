=============================
Benchmarking Doublet detection Methods
=============================

Using the dataset we created using the results from Singlet code as described in :ref:`singletCode`, we benchmark four doublet detection methods - scDblFinder (`link <https://bioconductor.org/packages/release/bioc/html/scDblFinder.html>`_), DoubletFinder (`link <https://github.com/chris-mcginnis-ucsf/DoubletFinder>`_), Scrublet (`link <https://github.com/AllonKleinLab/scrublet/>`_) and Hybrid (`link <https://github.com/kostkalab/scds>`_). 

We evaluated the AUPRC, AUROC, TNR, and doublet scores and calls of the four methods on each of the barcoded datasets with doublets formed by averaging ground-truth singlets. 

.. figure:: /images/Figure3.svg
   :scale: 50 %
   :alt: Benchmark results of doublet detection methods
   
   Benchmark results of doublet detection methods

Since doublet methodologies yielded different doublet detection performances, we also analysed the data to see if the different methods exhibit any pair-wise patterns of doublet labeling. To do this, we devised a new metric called similarity score, which calculates the fraction of doublets in a sample on which two methods make the same call. Across all datasets and doublet detection methods, the average similarity score was 0.66, suggesting some degree of inconsistency of doublet labeling.

We also asked whether doublet detection methods differ in their performance on the same cell type and experimental design, but performed on multiple platforms. We leveraged TREX-barcoded datasets of the same cell type (mouse brains) sequenced using both 10X Genomics and Smart-seq3. We found variable performance of each doublet detection method on the two datasets.

The results overall demonstrate that the doublet detection method performances vary depending on their underlying algorithms, some methods exhibiting similar or unique patterns of doublet assignments, with the technologies used to create scRNAseq datasets also impacting the choice of method. More details about the analysis we did on the results of these doublet detection method can be found in our paper.

We also asked whether our approach could be harnessed for evaluating the performance of doublet detection methods on scATAC-seq datasets and chose Amulet for our proof-of-concept analysis. For this, we used a de-novo generated 10X Genomics Multiome datasets(RNA + ATAC) using the Watermelon barcoding technology. We ran AMULET on the fragment files from the scATAC-seq modality to extract singlet/doublet labels, and, in parallel, extracted true singlets from barcoded scRNA-seq library from the exact same cells. By comparing labels of true negatives and false positives across AMULET and singletCode-extracted singlets from across 6 datasets, we estimated the average TNR for AMULET to be 0.924.


.. contents:: Contents:
   :local: