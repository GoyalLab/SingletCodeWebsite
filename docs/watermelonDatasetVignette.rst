Vignette for using Watermelon Barcodes with singletCode
==================================================================================================

This a notebook that will walk you through using watermelon barcode FASTQ files
all the way to identifying singlets. The barcode region is assumed to be amplified 
using Illumina MiSeq.

All the data for this vignette and the files output from it can be
downloaded from
`here <../source/dataVignette/watermelonVignetteData.zip>`__. It
contains inputFiles and the outputFiles.

First step is to understand the samples present in the FASTQ files.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample fastq files are in the inputFolder. We can identify the
sample name and number from the FASTQ file. For example,
sampleName_S1_L001_R1_001.fastq.gz means that the sample name is
sampleName and sample number is 1.Make sure that both read 1 and read 2
for each sample are present in the same folder (R1 and R2)

Creating sample sheet for these two samples.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    import pandas as pd

.. code:: ipython3

    Path = "path/to/where/the/repo/was/cloned"
    p = "path/to/zipped/folder"

.. code:: ipython3

    sampleSheet = pd.read_csv(f"{p}/inputFiles/sampleSheet.csv")
    sampleSheet




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>sampleName</th>
          <th>sampleNumber</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>sampleName</td>
          <td>1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>otherSampleName</td>
          <td>2</td>
        </tr>
      </tbody>
    </table>
    </div>



Installing singletCode Command line tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the singletCode command line tool, clone the repository from
GitHub. Let the path to the folder you are running this command be
**Path**

.. code:: ipython3

    !git clone https://github.com/GoyalLab/singletCodeTools

Now, to run the watermelon module of singletCodeTools, you need to run
this command. If we are going by the folder structure of the zipped file
and **p** is *path to the unzipped folder containing example files*,
then 1. **inputFolder** will be p/inputFiles/ 2. **outputFolder** will
be p/outputFiles/ 3. **sampleSheet** will be
p/inputFiles/sampleSheet.csv

.. code:: ipython3

    import subprocess
    
    command = [
        'python',
        f'{Path}/commandLine/singletCodeCommandLine.py',
        'watermelon',
        '-i',  f'{p}/inputFiles',
        '-o',  f'{p}/outputFiles',
        '-s', f'{p}/inputFiles/sampleSheet.csv',
        '--outputName', 'watermelonBarcodeUmi.csv'
    ]
    
    result = subprocess.run(command)


**NOTE**

In the current FASTQ file, the pattern for the watermelon barcode is
GGGCTG(([AT][CG]|[CG][AT]){15})GACGCT.

If this is not true for the barcodes in your data, then you can go to
*processSampleBarcode* function in
*Path/commandLine/watermelonUtilityFunctions.py* and change the line
starting with **pattern =**.

Using 10X list of cell IDs to check that all the cell IDs were also captured in scRNAseq
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use a 10X single-cell RNA sequencing of the same set of
cells to check which barcoded cells are of interest to you, then you can
add –use10X flag to your command and provide the path to the list of
cell IDs.

.. code:: ipython3

    result = subprocess.run([
        'python',
        f'{Path}/commandLine/singletCodeCommandLine.py',
        'watermelon',
        '-i', f'{p}/inputFiles/',
        '-o', f'{p}/outputFiles/',
        '-s', f'{p}/inputFiles/sampleSheet.csv',
        '--outputName', 'watermelonBarcodeUmiWith10X.csv',
        '--use10X', "True",
        '--input10X', 'barcodes.tsv'
    ], capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully")
        print("Output:\n", result.stdout)
    else:
        print("Command failed")
        print("Error:\n", result.stderr)

Run singletCode to identify true singlets using the cellID-Barcode-UMI file just created
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the count module available in the command line

.. code:: ipython3

    import subprocess
    
    result = subprocess.run([
        'python',
        f'{Path}/commandLine/singletCodeCommandLine.py',
        'count',
        '-i', f'{p}/outputFiles/watermelonBarcodeUmi.csv',
        '-o', f'{p}/outputFiles/watermelon'
    ], capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully")
        print("Output:\n", result.stdout)
    else:
        print("Command failed")
        print("Error:\n", result.stderr)

There different files which are output from this command: 1. different
kinds of singlets in each of the samples: single_barcode, dominant_umi,
multi_barcode 2. a combined list of all singlets for a sample:
singlets_all 3. a csv file containing the statistics of each kind of
singlet, number of potential multiplets and cells filtered out due to
low UMI counts of barcodes 4. the list of potential multiplets for each
of the samples: multiplets

For more explanation on different kinds of singlets seen in the output
files, you can refer
`here <https://goyallab.github.io/SingletCodeWebsite/singletCode/>`__
and for example of data showing this, you can refer to the vignette
about singletCode package.
