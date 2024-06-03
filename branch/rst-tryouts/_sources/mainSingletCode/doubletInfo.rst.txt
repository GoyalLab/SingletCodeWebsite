================================
Doublets in RNA sequencing data
================================

.. line-block::
   **How scRNA-seq technologies work?**
   scRNA-seq technologies rely on distributing individual cells from a suspension into individual reactions, each labeled with a unique “ID”, usually in the form of a reaction-specific sequence barcode. 

   **Since each cell has an unique ID, why are there doublets?**
   Despite numerous technological optimizations, multiple cells can occasionally be encapsulated in a single reaction, resulting in doublets or multiplets where two or more cells are assigned the same reaction ID. The percentage of doublets in a given experiment depends on several factors, including the features of the sample and throughput, and can be as high as 40-50% :cite:`Bernstein_Fong_Lam_Roy_Hendrickson_Kelley_2020` :cite:`Xi_Li_2021`. In turn, such artifacts affect the downstream analysis :cite:`Luecken_Theis_2019`. 


.. contents:: Contents:
   :local:
