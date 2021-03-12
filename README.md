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

Main script:
1. Open nlp.ipynb 
2. Run first 3 cells