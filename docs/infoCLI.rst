=========================================
command line interface
=========================================


Availablility
-----------------
The source code for the command line tool is available in our GitHub repository (`repo <https://github.com/GoyalLab/singletCodeTools/>`_). You can clone the reposiory to access the code locally.

.. code-block:: bash

    git clone https://github.com/GoyalLab/singletCodeTools/

Using the interface
-----------------------

Navigating to commandLineTools folder, you will find 3 files and you will need to run  singletCodeCommandLine.py. There are 2 modules available, one to run singletCode and the other to create a sample sheet if you have used Watermelon barcoding techmology using the fastq sequenced files from MISEQ.

Detailed information about the modules in the command line interface
-----------------------------------------------------------------------------

This script contains two modules:
1. Count Module: generates a list of singlets.
2. Watermelon Module: Uses the MiSeq dial-out files to create the cell ID, barcode, and sample file. The output of this module can then be used as input for the Count module.

For the Count Module:

        .. code-block:: python

            python singletCode.py count -i /path/to/input.txt -o /path/to/output
            
For the Watermelon Module:

        .. code-block:: python

            python3 singletCode.py watermelon -i /path/to/fastq/files -o 
            path/to/save/csv/file -s path/sample/sheet -use10X False -input10X 
            path/to/barcodes/tsv

singletCode command line
-------------------------

.. automodule:: source.commandLineTools.singletCodeCommandLine 

