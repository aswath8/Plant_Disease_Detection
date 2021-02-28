List of packages:
```
conda list -e
conda list -e > requirements.txt
```
#To export environment
```
activate <environment-name>
conda env export > <environment-name>.yml
```
#For other person to use the environment
```
conda env create -f ericsson.yml
```