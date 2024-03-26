=================
Classifier
=================


How was it built?
----------------------------------

We used the true singlets identified with singletCode to simulate datasets with 10% doublets and trained an extreme gradient-boosting (XGBoost) classifier to detect these doublets. 

The classifier is built in two steps:

   #. Hyperparameter optimization (using hyperopt()) with a training and validation set.
   #. Training the optimal model with a training and test set


.. figure:: /images/Figure6A.png
   :scale: 80 %
   :alt:  Schematic of classifier optimization and training. Data was first split into training, validation, and testing sets. The training and validation sets were used to optimize the hyperparameters using the hyperopt library. A search space (blue cube) was defined in high dimensional hyperparameter space and, through Bayesian optimization, the optimal value for each hyperparameter was determined based on maximizing the AUPRC value. Once the model’s parameters were optimized, the final, optimal, classifier was trained using the training and test sets. An extreme gradient boosted (XGBoost) classifier was trained to recognize doublet cells with input data being gene count matrices of datasets made from singlets and 10% simulated doublets. 
   :align: center
   
   *Schematic of classifier optimization and training. Data was first split into training, validation, and testing sets. The training and validation sets were used to optimize the hyperparameters using the hyperopt library. A search space (blue cube) was defined in high dimensional hyperparameter space and, through Bayesian optimization, the optimal value for each hyperparameter was determined based on maximizing the AUPRC value. Once the model’s parameters were optimized, the final, optimal, classifier was trained using the training and test sets. An extreme gradient boosted (XGBoost) classifier was trained to recognize doublet cells with input data being gene count matrices of datasets made from singlets and 10% simulated doublets.*

How well does it perform?
---------------------------------

We achieved significantly higher AUPRC and AUROC scores using our classifier compared to the other methods we benchmarked for doublet detection. 

.. figure:: /images/Figure6B.png
   :scale: 30 %
   :alt: Results of classifier doublet detection compared to other doublet detection methods as measured by AUPRC. Each dot represents the average AUPRC score of a doublet detection method (color) on a given dataset (x-axis). The ribbon has the width of the standard deviation of the AUPRC score for each doublet detection method.
   :align: center
   
   *Results of classifier doublet detection compared to other doublet detection methods as measured by AUPRC. Each dot represents the average AUPRC score of a doublet detection method (color) on a given dataset (x-axis). The ribbon has the width of the standard deviation of the AUPRC score for each doublet detection method.*

.. _classifier-Nonebarcoded:

Classifying doublets in non-barcoded datasets 
------------------------------------------------

Although barcoding experiments are becoming increasingly prevalent, they are still relatively uncommon. Therefore, we sought to train a doublet classifier on barcoded data that could detect doublets in non-barcoded data. We trained a classifier on a melanoma cell sample using true singlet labels from singletCode and successfully identified doublets in a similar cell sample without needing barcoding data. 

.. figure:: /images/Figure6G.png
   :scale: 50 %
   :align: center
   :alt: Schematic of training a doublet classifier on barcoded data from 1 experiment and using that classifier to identify doublets in a biological replicate, experiment 2.

   *Schematic of training a doublet classifier on barcoded data from 1 experiment and using that classifier to identify doublets in a biological replicate, experiment 2.*

As barcoded scRNA-seq data becomes more abundant, experimenters can train a classifier specific to their cell type using a barcoded subset of data, and, eventually, there could be enough data to train a classifier on multiple barcoded cell types which can be used more generally.

.. contents:: Contents:
   :local:
