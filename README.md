# vizwiz-labels
A mini project for the extraction of labes from the VizWiz Image Captioning dataset.

Step 1: `extract.ipynb`
    
- For every picture, all nominal phrases (Keywords) for each caption are collected.
- The Keywords are counted. Keywords that appear less than 15 times in the whole corpus are dropped.

Step 2: `similarity.ipynb`

- Word embeddings are extracted (GloVe) and phrase embeddings (if a Keyword is phrasal) are calculated (averaged)
- The Keywords are clustered. We used 20 clusters in total.


Step 3: `classification.ipynb`

Work in progress.
