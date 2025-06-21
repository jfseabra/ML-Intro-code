# An Introduction to Machine Learning: Code, data and plots
This repository contains the code I wrote to generate data and plots for introducing key Machine Learning (ML) concepts in my PhD thesis, titled *Search for Hidden New Physics Signals at the Large Hadron Collider* (you can find it [here](https://scholar.tecnico.ulisboa.pt/api/records/OyQUt3MJB6nkaXp-3luDm2SpHyRHOjqSXwYE/file/f5bfec1322e74710acd105555b48b333a6c042aefd256552f091e2ba340f1800.pdf)). The material shared here is related to Chapter 4 and Appendices C and D of the thesis. I outline the structure of those chapters below, in order to identify the notebooks and/or Python codes associated with each section. <br>

<b>Note:</b> I'm currently using TensorFlow 2.18 and Keras 3.8, which differ from the versions I had when the Jupyter notebooks were originally written. To ensure compatibility with the newer versions, I re-ran the notebooks. For that reason, some plots show very small differences compared to those presented in the thesis. <br>

## Basic concepts of ML
PolynomialRegression.ipynb
## Metrics for classification tasks
gaussians.py <br>
ROC.py <br>
altROC.py
## Neural Networks
### The first artificial neuron
LogicGates.py
### Logistic Regression
sigmoid.py <br>
LogisticRegression.ipynb
### Making logistic regression nonlinear
NN.ipynb
## Decision Trees
DecisionTree.ipynb
## Gradient Boosting
GradientBoosting.ipynb
## Appendix C: More on the XOR problem
LogicGates.py (with the option 'XOR2')
## Appendix D: Enhancing Gradient Descent
LinearRegression.ipynb
