# vizwiz-labels
A mini project for the extraction of labes from the VizWiz Image Captioning dataset.

Step 1: `extract.ipynb`
    
    Step 1a: For every picture, all nominal phrases (Keywords) for each caption are collected.

    Step 1b: The Keywords are counted. Keywords that appear less than 15 times in the whole corpus are dropped.

Step 2: `similarity.ipynb`
    
    Step 2a: Word embeddings are extracted (GloVe) and phrase embeddings (if a Keyword is phrasal) are calculated (averaged)

    Step 2b: The Keywords are clustered. We used 20 clusters in total.
