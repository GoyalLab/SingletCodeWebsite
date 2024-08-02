implementing singletCode on your data
========================================

singletCode is a framework that can be extended to most scRNA-seq or even scATAC-seq data to accurately identify singlets.

Barcoded datasets
-----------------------

We created both a python package called singletCode and a command-line interface. The only input needed is a .csv file with cell ID, barcode, sample information, and UMI counts for each barcode. You can find more information to use it :ref:`here <package-info>`

Non-barcoded datasets
------------------------------

If the data is non-barcoded, the information from true singlets identified from singletCode can still be harnessed using a classifier trained on barcoded data from a different experiment using the cell type of interest. Find more information about this in the classifier page :ref:`here <classifier-Nonebarcoded>`.


