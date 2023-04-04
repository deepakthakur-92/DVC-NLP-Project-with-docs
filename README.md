# Project Name
StackOverflow Text Classification: Identifying Python-Related Questions with ML

# Project Description
This project involved using machine learning algorithms to classify StackOverflow questions based on their relevance to Python. The dataset consisted of a large collection of text-based questions with binary labels indicating whether they were related to Python or not. The project focused on developing a text classification model that could accurately distinguish between Python-related questions and other programming language questions. Techniques such as data preprocessing, feature extraction, model selection, and hyperparameter tuning were applied to improve the model performance. The final model achieved high accuracy in identifying Python-related questions, and the project demonstrates the potential for applying machine learning to large-scale text classification tasks.

## Original repo:

 - [Project Repo link](https://github.com/deepakthakur-92/DVC-NLP-Project-with-docs)

# Usage:
- Building a recommendation system: The model can be used to recommend relevant Python questions to StackOverflow users based on their interests and past activity. This can help improve user engagement and satisfaction by providing them with targeted content that matches their needs.

- Streamlining question moderation: The model can be used by moderators to automatically classify questions as either Python-related or not, allowing them to quickly identify and address issues related to irrelevant or inappropriate content.

- Data analysis and research: The project can be used as a starting point for data analysis and research on StackOverflow question data. Researchers and data analysts can use the model to filter and analyze questions related to specific topics or programming languages, providing valuable insights into trends, user behavior, and other aspects of the StackOverflow community.

- Natural language processing: The techniques used in this project can be applied to other text-based classification problems, including sentiment analysis, spam detection, and document classification. The project can serve as a template or reference for developing similar models in different domains or industries.

# Dataset:
 - 

# STEPS to run this project:

## STEP 01: 
Clone the repository

```bash
git clone https://github.com/deepakthakur-92/DVC-NLP-Project-with-docs.git
```

## STEP 02: 
Create an environment

```bash
conda create --prefix ./env python=3.7 -y
```

## STEP 03:
Activate the environment

```bash
conda activate ./env
```

## STEP 04: 
Install the requirements

```bash
pip install -r requirements.txt
```
## STEP 05:
Initialize the dvc project

```bash
dvc init
```

## STEP 06:
To run the project

```bash
dvc repro
```

# Technology Used
## :hammer_and_wrench: Requirements
- python 3.x
- tqdm
- dvc
- pandas
- numpy
- mkdocs-material
- PyYAML
- scikit-learn
- RandomforestClassifier

# Authors:
```bash
Author: Deepak Thakur
```