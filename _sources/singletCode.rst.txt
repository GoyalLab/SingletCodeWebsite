======================
what is singletCode?
======================

singletCode is a framework to extract true singlets from barcoded scRNA-seq data. Our pipeline identified barcoded singlets from 10 different publications and 6 original experimental scRNA-seq samples generated in this study, encompassing 7 different barcoding technologies, 94 scRNA-seq samples, 3 unique sequencing technologies, and a total of 564,579 cells. Of the 338,948 barcoded cells, we extracted 293,618 singlets.(read more about the barcoded datasets we used singletCode with :ref:`here<datasetInfo>`). 


.. figure:: /images/Figure1B.png
   :scale: 50 %
   :alt: Stacked bar chart showing types of singlets in each dataset. Each color represents one type of barcode composition that constitutes a singlet. Single barcode means one cell ID has one associated lineage barcode. Dominant barcode means one barcode has the highest UMI counts in one cell. Multiple barcodes within or across samples are scenarios where the same barcode combinations are observed in the same sample or across twin samples. See our paper for details.
   :align: center

Singlet identification
-----------------------------------
singletCode leverages the fact that the lineage barcodes are present within the cell before sequencing. As a result of multiplicity of infection, singletCode identifies cells which meet any of the following conditions as a true singlet:

   #. 1 barcode/1 cell ID
   #. >1 barcode per 1 cell ID, but 1 barcode has significantly more UMI counts than the other barcodes within the same cell
   #. M barcodes per 1 cell ID, but the same combination of M barcodes are found in other cells in the same sample
   #. M barcodes per 1 cell ID, but the same combination of M barcodes are found in other cells across samples within the same experimental design (common in barcoding studies) 


.. figure:: /images/Figure1F.png
   :scale: 50 %
   :alt: Stacked bar chart showing types of singlets in each dataset. Each color represents one type of barcode composition that constitutes a singlet. Single barcode means one cell ID has one associated lineage barcode. Dominant barcode means one barcode has the highest UMI counts in one cell. Multiple barcodes within or across samples are scenarios where the same barcode combinations are observed in the same sample or across twin samples. See our paper for details.
   :align: center
   
   *Stacked bar chart showing types of singlets in each dataset. Each color represents one type of barcode composition that constitutes a singlet. Single barcode means one cell ID has one associated lineage barcode. Dominant barcode means one barcode has the highest UMI counts in one cell. Multiple barcodes within or across samples are scenarios where the same barcode combinations are observed in the same sample or across twin samples. See our paper for details.*

.. _simulationInfo:

.. contents:: Contents:
   :local: