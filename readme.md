# Thesis-recsys 

## Installation 
1. clone the project 

```bash
 git clone https://github.com/vstergiou/thesis-recsys.git
 cd thesis-recsys
```
2. Prepare the MLFairnessGym fork and download the dataset
```bash
 git submodule add https://github.com/vstergiou/ml-fairness-gym.git mlfairnessgym
 python -m mlfairnessgym.environments.recommenders.download_movielens
```

3. Install the project and its dependencies
```bash
 pip install -e . 
```