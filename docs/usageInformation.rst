singletCode For Your Data
===================================

singletCode is a framework that can be extended to most RNAseq or even ATACseq data to accurately identify singlets.

For Barcoded Datasets
-----------------------
If the data is barcoded, then it is straight-forward to use singletCode for the dataset. We provide both a python package called singletCode and a command lne interface. The only input needed is a csv file with cell ID, barcode and UMI counts for each barcode. 

non-barcoded Datasets
------------------------------
If the data is non-barcoded, the information from true singlets identified from singletCode can still be harnessed. A classifier trained on a barcoded dataset has the potential to detect singlets on other experimental datasets with similar cell type and tissue with high accuracy. We tested this out using two samples from Goyal et al. 1 - wherein the classifier is trained on sample A and used to detect singlets in sample B. The classifier was able to detect singlets with high accuracy (read more about the results on the page about classifiers).
