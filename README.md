# Portfolio of projects
![](https://img.shields.io/badge/author-Leandro%20Corrêa-blue.svg)

## Overview
In this document, I aim to provide a compilation of the key public projects I have been developing in recent years. By sharing these projects, my objective is to showcase practical work in the field of analytics and foster collaborations that can enhance my professional growth. Furthermore, I aspire to inspire and motivate potential collaborators to explore new possibilities in the realm of data analysis.

If any of these projects pique your interest or if you have ideas for new initiatives, improvements, suggestions, and so on, please do not hesitate to get in touch. I firmly believe in the power of collaboration and continuously seek ways to expand my network and contribute to the advancement of the analytics field.

## Projects

### E-commerce propensity purchase based on Google Analytics Data
![](https://img.shields.io/badge/last%20edited-10--01--2021-yellow.svg)

#### Business Problem:
Build a predictive model to identify the user's propensity to purchase, based on browsing behavior metrics obtained from Google Analytics.

#### Proposed Solution:
Six prediction models were built and compareted using user browsing behavior data from a [public e-commerce website](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset), as input information (1-SVM with Linear Kernel; 2- SVM with RBF Kernel; 3-SVM with Polynomial Kernel; 4-Random Forest; 5-LightGBM and 6-Adaa Boost). The response variable considered was whether or not the user's browsing behavior resulted in a purchase (binary output). Data preprocessing, class balancing, and standardization procedures were performed to improve the results. At the end of the experiment, the best model achieved an accuracy of 93.24%, indicating the probability of a user making a purchase or not in the e-commerce based on their browsing behavior data collected through Google Analytics.

#### Access address to the code and further development details:
Link: [Propensity purchase based on GA](https://github.com/hscleandro/Portfolio/tree/main/notebooks/propensity_purchase_ga)

### Sentiment analysis on Twitter using Apache streaming
![](https://img.shields.io/badge/last%20edited-01--02--2022-yellow.svg)

#### Business Problem:
To create a proof of concept for evaluating the behavior of terms or keywords related to a specific aspect of a product within the Twitter social media platform. During the development phase, the stakeholder was involved in promoting a product within a Brazilian television show, and Twitter served as the primary feedback channel for the marketing team to assess the product's reception in an open environment. The evaluation process was conducted manually, with marketing professionals monitoring Twitter during the product's airing on the show (during evening and late-night hours), using intuitive judgment to gauge the brand's impression.

#### Proposed Solution:
To develop a real-time data analysis tool with an embedded sentiment classifier that can retrieve posts related to specific keywords and provide sentiment analysis for each post with a known accuracy margin. The tool aims to streamline the process of monitoring and evaluating public sentiment on Twitter, enabling the marketing team to gain actionable insights into the brand's perception and acceptance during the program's broadcast.

#### Access address to the code and further development details:
Link: [Sentiment analysis on twitter](https://github.com/hscleandro/Portfolio/tree/main/notebooks/sentiment_analysis_twitter)

## Author

* **Leandro Corrêa** - Computer Scientis and Specilist Anlytics - [Twitter profile](https://twitter.com/leandrohsc)

## Acknowledgments

* Data Science Academy class [DSA](https://www.datascienceacademy.com.br/), that served as a basis for improving problems of propensity to purchase and sentiment analysis.
