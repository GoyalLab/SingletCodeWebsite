Vignette to use singletCode package
===================================

The input needed to run singletCode is a .csv file that contains the
information about cell ID (added while sequencing), lineage barcode, and
sample name. Each row should be repeated n times where n is the number
of UMIs associated with that barcode and cell ID combination. You can
download a sample input sheet `here <https://github.com/GoyalLab/SingletCodeWebsite/raw/main/source/dataVignette/singletCodePackageVignetteData.zip>`_. It is a subset of data from
Jiang Et al and details about it are described in the singletCode paper
in detail. This folder contains the input sheet (in inputFiles) along with test output files you can compare to(in outputFiles).

Install singletCode package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    !pip3 install singletCode


Import necessary functions from it

.. code:: ipython3

    from singletCode import check_sample_sheet, get_singlets

Read in input sheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let path to the downloaded and unzipper folder be **path**. 

.. code:: ipython3

    import pandas as pd
    path = "path/to/downloaded/and/unzipped/folder"
    pathToInputSheet = f"{path}/inputFiles/JiangEtAlSubset_InputFiles.csv"
    df = pd.read_csv(pathToInputSheet)

Check formatting of input sheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    check_sample_sheet(df)

Identify singlets from input sheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    outputPath = f"{path}/outputFiles/"
    cellLabelList, stats = get_singlets(df, dataset_name= "JiangEtAlSubset", save_all_singlet_categories = True, output_path=outputPath)


Saving the stats and the singlet list

.. code:: ipython3

    stats.to_csv(f"{outputPath}/JiangEtAlSubset_stats.csv")
    cellLabelList[cellLabelList['label'] == "Singlet"].to_csv(f"{outputPath}/JiangEtAlSubset_singletList.csv")

Understanding the output files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To understand some of the files in the output, we can look at cell IDs
and their data in the original input sheet

For the dominant_umi_singlets, there are two cell IDs. One of them is
TGTAAGCGTCTCGCGA. If we look at that entry in the input sheet and count
the number of UMI associated with each barcode, we see that one barcode
has 99 UMI counts while the second highest UMI count is 7. So, the cell
most likely has only one barcode associated with it and hence, a
singlet.

.. code:: ipython3

    import pandas as pd
    df[df['cellID'] == 'TGTAAGCGTCTCGCGA'].groupby(['cellID', 'barcode', 'sample']).size().reset_index(name='count').sort_values('count', ascending=False).reset_index(drop=True)




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
          <th>cellID</th>
          <th>barcode</th>
          <th>sample</th>
          <th>count</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATTGTTGTTGCAGATGCAGTTGATGCTGATGAAGTTGTACAAGGTC...</td>
          <td>1</td>
          <td>99</td>
        </tr>
        <tr>
          <th>1</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATTCGACTTGATCTTCTAGAACATGGTGAACTAGCAGGTGCTGATC...</td>
          <td>1</td>
          <td>7</td>
        </tr>
        <tr>
          <th>2</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATACTAGCTCAAGCAGTACTACTACTTCGTCTTCATGCAGAACAAC...</td>
          <td>1</td>
          <td>6</td>
        </tr>
        <tr>
          <th>3</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATAGATGCACTTGGTGGTCGAGTTCTAGTTGTAGCTGATCGTCCAG...</td>
          <td>1</td>
          <td>6</td>
        </tr>
        <tr>
          <th>4</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATTCGACCAGAACCACATGCAGTTCAACGTGTTCGAGGTGTAGATG...</td>
          <td>1</td>
          <td>6</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>82</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATAGTAGTAGCTGTTGGTGTTGAAGTACTTCCTCTTGCTCCTCGTG...</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>83</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATAGTAGATGAACGTCCTCTACATGTTCTTCGTCAAGTACCAGCAC...</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>84</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATAGTACATGGTGGACCTGGACTTCGAGATGGAGCTCTTGTTCCTG...</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>85</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>ATAGGAGTAGTTGGTGATGGTCTACCAGAAGGTGAAGGTGGAGAAG...</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>86</th>
          <td>TGTAAGCGTCTCGCGA</td>
          <td>GGTGCTCAACTTCTTGTTGTACTTCTAGTTGATGTTGGACGTCATC...</td>
          <td>1</td>
          <td>1</td>
        </tr>
      </tbody>
    </table>
    <p>87 rows × 4 columns</p>
    </div>



Next, we can look at multi-barcode singlets. There are two cell IDs:
AGGCTGCTCTTTCCGG and GAGGGATGTAACATCC. If we look at the barcodes with
greater than 2 UMI counts, we see that they have the same combination.
The only way this can occur is if a cell receives multiple barcode
initially and then divides.

.. code:: ipython3

    (df[df['cellID'] == 'AGGCTGCTCTTTCCGG']
     .groupby(['cellID', 'barcode', 'sample'])
     .size()
     .reset_index(name='count')
     .sort_values('count', ascending=False)
     .query('count >= 2')
     .reset_index(drop=True)
    )




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
          <th>cellID</th>
          <th>barcode</th>
          <th>sample</th>
          <th>count</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>AGGCTGCTCTTTCCGG</td>
          <td>ATAGGAGTAGTTGGTGATGGTCTACCAGAAGGTGAAGGTGGAGAAGTTGG</td>
          <td>1</td>
          <td>13</td>
        </tr>
        <tr>
          <th>1</th>
          <td>AGGCTGCTCTTTCCGG</td>
          <td>ATTGAACGTGGAGTTGAACTTGTACTACGAGTACGTCTAGAACATGAACC</td>
          <td>1</td>
          <td>2</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    (df[df['cellID'] == 'GAGGGATGTAACATCC']
     .groupby(['cellID', 'barcode', 'sample'])
     .size()
     .reset_index(name='count')
     .sort_values('count', ascending=False)
     .query('count >= 2')
     .reset_index(drop=True)
    )




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
          <th>cellID</th>
          <th>barcode</th>
          <th>sample</th>
          <th>count</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>GAGGGATGTAACATCC</td>
          <td>ATAGGAGTAGTTGGTGATGGTCTACCAGAAGGTGAAGGTGGAGAAGTTGG</td>
          <td>1</td>
          <td>12</td>
        </tr>
        <tr>
          <th>1</th>
          <td>GAGGGATGTAACATCC</td>
          <td>ATTGAACGTGGAGTTGAACTTGTACTACGAGTACGTCTAGAACATGAACC</td>
          <td>1</td>
          <td>2</td>
        </tr>
      </tbody>
    </table>
    </div>


