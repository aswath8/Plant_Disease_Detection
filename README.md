List of packages:
```
conda list -e
conda list -e > requirements.txt
```
To export environment
```
activate ericsson
conda env export > ericsson.yml
```
For other person to use the environment
```
conda env create --file ericsson.yml -n ericsson
```
For collaborator to update the environment
```
conda activate ericsson
conda env update --file ericsson.yml
```
Main scripts:
1. nlp.ipynb 
2. SQL_Helper_notebook.ipynb
3. concept_drift.ipynb

Dataset references: \
[TNAU horticulture](https://agritech.tnau.ac.in/horticulture/horti_index.html) \
[University of California, Master Gardeners of Sacramento County](http://sacmg.ucanr.edu/Vegetable_Problems_Summer/diseases/#:~:text=Tomato%20%2D%20Fusarium%20and%20Verticillium%20Wilts,soil%20fungi%20Fusarium%20and%20Verticillium.)
