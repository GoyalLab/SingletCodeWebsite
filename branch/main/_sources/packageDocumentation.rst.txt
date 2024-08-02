===============================
singletCode PyPI package
===============================

Availablility
-----------------
The package is available on PyPI as `singletCode <https://pypi.org/project/singletCode/>`_ . 

.. _package-info:

How do I use it?
------------------

    #. Installation

        It can be installed from PyPI using the following in the terminal:

        .. code-block:: python

            pip3 install singletCode
            from singletCode import check_sample_sheet, get_singlets 
    
    #. Preparing the input sample sheet.

        The input sample sheet is a .csv file that contains the information about cell ID (added while sequencing), lineage barcode, and sample name. Each row should be repeated n times where n is the number of UMIs associated with that barcode and cell ID combination. For creating the input, you can read the .csv file in as a pandas dataframe.

        .. code-block:: python

            import pandas as pd
            df = pd.read_csv("path/to/csv/file.csv")

       You can check if the format and the column names are valid for running singletCode using check_sample_sheet() function.

        .. code-block:: python

            check_sample_sheet(df)

        It will either return an error with information about how to modify the sample sheet to make it a valid input or will print the message, “The sample sheet provided can be used as input to get_singlets to get a list of singlets identified”, in which case you can move to the next step.

    #. Running get_singlets() to get an assignment of singlet status for each cell ID and barcode combination. 

        This is the step where singlet identification is done using the singletCode framework. You can read more about the parameters for get_singlets() below. In this example, default values are used.

        .. code-block:: python

            cellLabelList, stats = get_singlets(df, dataset_name = "Sample1")

        **cellLabelList** is a pandas dataframe that contains 5 rows: cellID, barcode, sample, nUMI and label. Label is whether the particular cell ID and barcode combination has been called a singlet or not.

        To get a dataframe containing just the singlets, you can run this:
        
        .. code-block:: python

            singletList = cellLabelList[cellLabelList["label"] == "Singlet"]

        **stats** contains the statistics for each sample present in your dataset: total cells, total number of singlets, number of singlets recovered from different categories of singlets (such as single-barcode singlets, muli-barcode singlets, dominant-UMI singlets), number of cells removed due to low barcode UMI counts for the barcode and number of indeterminate cells since singletCode can identify only truly singlet cells but not be certain if the other cells are truly not singlets.

        You can save the singlets list in a .txt file and the list of cell IDs in each category of singlets by setting **save_all_singlet_categories** parameter to TRUE. 



Detailed information about the parameters for the functions in the package
-----------------------------------------------------------------------------

.. currentmodule:: source.singletCode.singletCode

get_singlets
---------------

.. autofunction:: get_singlets

check_sample_sheet
--------------------

.. autofunction:: check_sample_sheet


