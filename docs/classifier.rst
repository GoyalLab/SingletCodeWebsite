=================
Classifier
=================


Working of the classifier
----------------------------------
We used the true singlets identified with singletCode to train a deep learning model to identify doublets. It is an extreme gradient-boosting (XGBoost) classifier on samples with 10% simulated doublets. Gradient boosting uses a series of decision trees to minimize the residuals of the prediction made by the previous tree. We chose XGBoost because of its out-of-the-box performance on tabular data, speed, and extensive documentation. To achieve peak performance, we used Bayesian optimization through the hyperopt library to tune the hyperparameters of our model. We split the classification datasets such that 60% of a dataset was used for training at both the parameter optimization and final training steps, and 20% each was used for validation during the optimization stage and testing during the final evaluation stage.. Despite the high class imbalance (singlets:doublets = 9:1), the average AUPRC and AUROC values of the classifier were 0.98*** and 0.99***, respectively, for testing datasets across all the technologies.

[SCHEMATIC : Fig 6]

Benchmarking
---------------------------------
To benchmark the classifier, we trained on sample A from Goyal et al. 1 and implemented it to identify singlets in sample B, an independently-performed experiment on the same cell type (melanoma). Similarly, we trained the classifier on sample B and used it to identify doublets in sample A. The performance was compared to other doublet detection methods and the classifier works significantly better. This highlights the practical impact of our approach on singlet detection from non-barcoded datasets.


.. contents:: Contents:
   :local:
