# Implementing a scikit-learn worflow

Hello again 👋

+ I created this repository as a reference for one of my tutorial lessons on **AI fundamentals**. All materials used (the question, slides, dataset, Jupyter Notebook) are attached in this repository with respective directory names.
+ Here, I demonstate how to implement a simple [scikit-learn](https://scikit-learn.org/stable/index.html) workflow by solving a student performance prediction problem (using [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#kneighborsclassifier) algorithm).
+ I cover the following concepts: Data Wrangling, Exploratory Data Analysis (EDA), splitting the dataset, data preprocessing in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#pipeline), model training, model evaluation and model persistence using [`joblib`](https://joblib.readthedocs.io/en/stable/). Finally, I deploy the KNN model interactively on my Hugging Face [Space](https://huggingface.co/spaces/martinmbiro/student-knn-task).
+ Please note that the slides and the Jupyter Notebook go hand in hand - they are complementary. If possible, refer to both of them side by side.

## Contents 📂
The contents of this repository are as follows:
##### 1. `question` 📁
Contains the question we're solving in this repository
##### 2. `slides` 📁
Contains the slides I used for the tutorial lessons. I go into detailed explaination of the code and concepts.
##### 3. `model` 📁
Contains the serialized trained model state - `knn_model.joblib`. Note, that the same has been saved to my Hugging Face Model repository linked [here](https://huggingface.co/martinmbiro/student_knn)
##### 4. `dataset` 📁
Contains the excel dataset used for model training. Please note that this is just a dummy dataset and not representative of real-world data
##### 5. `space` 📁
+ This directory contains all the files required to run and deploy the Web Application on Hugging Face Spaces: `app.py` (the Gradio application inference code), `requirements.txt` (Python dependencies), `README.md` (Space configuration and description), and `model_loader.py` (the code to load and deserialize the saved model state object)
+ It serves as the self-contained deployment directory that [GitHub Actions](https://docs.github.com/en/actions) syncs to Hugging Face, keeping deployment files separate from everything else.
##### 6. `.github/workflows/sync-to-hf.yaml` 📄
+ The YAML file defines the [GitHub Actions](https://docs.github.com/en/actions) workflow that automatically syncs the contents of the `space` directory to my Hugging Face [Space](https://huggingface.co/spaces/martinmbiro/student-knn-task) whenever changes are pushed to the main branch or the workflow is triggered manually.
+ Find Hugging Face Hub reference for [GitHub Actions](https://docs.github.com/en/actions) linked [here](https://huggingface.co/docs/hub/main/en/repositories-github-actions)
##### 7. [`00_scikit_learn_question_solution_github.ipynb`](https://github.com/Martinmbiro/student-knn-task/blob/main/00_scikit_learn_question_solution_github.ipynb)
Find the annotated code and plots in this Jupyter Notebook. Feel free to open and explore in Google Colab

## Tools 🛠️
**The tools used for this project are:**
1. [Google Colab](https://colab.google/) - A hosted _Jupyter Notebook_ service by Google.
2. [Hugging Face](https://huggingface.co/) - An open-source platform and community hub for sharing, hosting, and building ML models, datasets, and AI applications
3. [`gradio`](https://gradio.app/) - An open-source Python library for sharing and building interactive web-based user interfaces for ML models
4. [`sklearn`](https://scikit-learn.org/stable/getting_started.html) - An open-source Python toolset that provides algorithms for machine learning, data preprocessing, and model evaluation
5. [`matplotlib`](https://matplotlib.org/) - A comprehensive library for making static, animated, and interactive visualizations in Python
6. [`numpy`](https://numpy.org/) - The fundamental package for scientific computing with Python
7. [`pandas`](https://pandas.pydata.org/) - An open-source tool for data analysis and manipulation in Python
8. [`joblib`](https://joblib.readthedocs.io/en/stable/) - An open-source Python library designed for parallel computing, disk-based result caching, and efficient object serialization

## [Web App](https://huggingface.co/spaces/martinmbiro/student-knn-task) 💻
The KNN model trained in this exercise is deployed interactively on my Hugging Face Space linked [here](https://huggingface.co/spaces/martinmbiro/student-knn-task). Feel free to explore.

> ℹ️ **Disclaimer**  
> _The Web App uses the free **ZeroGPU** hardware which is allocated a daily 5 minutes quota. An error message will be displayed once the daily quota is exhausted_ 💔

## References 📚
+ GitHub. (2024). _GitHub Actions Documentation - GitHub Docs._ Docs.Github.Com. https://docs.github.com/en/actions
+ Microsoft Learn. (2025). _Online Training – Learn New Technology Skills | Microsoft_. Microsoft.Com. https://www.microsoft.com/en/microsoft-learn
+ Udemy. (2024). _Online Courses - Learn Anything, On Your Schedule._ Udemy; Udemy. https://www.udemy.com/
