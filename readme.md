# Distributed Recommender System using Deep Reinforcement Learning

This repository contains the code for my Master's thesis on "Distributed Recommender System using Deep Reinforcement Learning". The goal of this project is to develop a distributed recommender system that uses deep reinforcement learning to provide personalized recommendations to users.

## Background
Recommender systems have become increasingly popular recently because they can address the problem of information overload by suggesting items of interest to the users. However, most traditional recommender systems ignore the dynamic and sequential nature of the recommendation problem. In this thesis, I propose a method for modeling the recommendation problem as a Markov Decision Process using reinforcement learning techniques.

## Overview
The system consists of two models: a set of local agents that are trained in parallel by interacting with a local copy of the environment, and a global model whose parameters each local agent updates at the end of a training episode. The implementation is based on the Asynchronous Advantage Actor-Critic algorithm (A3C).

The code is implemented in Python using the following libraries:

* TensorFlow
* Keras
* Pandas
* NumPy
* Matplotlib
* Usage

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


## Evaluation
The performance of the algorithm is evaluated on a known dataset, using popular recommender systems metrics such as CTR and NDCG. The results are compared with other related work and show that in many cases, it can achieve comparable performance.

## Conclusion
The code provided in this repository can be used as a starting point for developing distributed recommender systems using deep reinforcement learning. The system is designed to capture the dynamic interaction between user and item and adapt to user preferences by encoding the dynamics of addiction and boredom in the rewards.

## Future Work
Future work could include experimenting with different deep reinforcement learning algorithms or optimizing the system's performance by exploring different hyperparameters and architecture designs.

## References
The thesis document can be found [here](https://www.dropbox.com/s/d7k7ez9dvm1pqdx/Stergiou_vasileios.pdf?dl=0). The code is based on the following research papers:

* [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783)
* [Deep Reinforcement Learning for List-wise Recommendations](https://arxiv.org/abs/1801.00209)

Feel free to use this repository as a reference or inspiration for your own research. If you have any questions or feedback, please don't hesitate to contact me.
