# COURSE_PLAN — Introduction to Data Science (14771150)

This document maps the official syllabus to the current repository structure and proposes a practical teaching sequence.

## Course Metadata

- **Course Unit**: Introduction to Data Science
- **Code**: 14771150

- **ECTS**: 7.5

## Recommended Teaching Sequence

1. `0-Python-revisions/`
2. `1-Databases/`
3. `2-WebAPI/`
4. `3-data-analysis/`
5. `4-dashboarding/`
6. Final practical project (integration of data, API, analysis, and dashboard)

## Syllabus to Repository Mapping

## 1) Data Manipulation

### 1.1 Relational databases (review)
- **Topics**: relational model, modeling/normalization, SQL CRUD, DBMS access
- **Main materials**:
  - `1-Databases/01_relationaldb.ipynb`
  - `1-Databases/Exercises/MySQL/Exercises.ipynb`

### 1.2 Non-relational databases (NoSQL / MongoDB)
- **Topics**: documents/collections, CRUD, indexing, MapReduce, replication/sharding concepts
- **Main materials**:
  - `1-Databases/02_mongo.ipynb`
  - `1-Databases/03_mongo-extra.ipynb`
  - `1-Databases/04_mongo_handout_examples.ipynb`
  - `1-Databases/Exercises/MongoDB/exercises_usersDB.ipynb`
  - `1-Databases/Exercises/MongoDB/exercises_weatherDB.ipynb`

### 1.3 Web frameworks for API use and creation
- **Topics**: Flask basics, routing, CRUD endpoints, REST principles
- **Main materials**:
  - `2-WebAPI/Flask-API/library/app_00_intro.py`
  - `2-WebAPI/Flask-API/library/app_01_a_first_get.py`
  - `2-WebAPI/Flask-API/library/app_02_CRUD.py`
  - `2-WebAPI/Flask-API/app.py`
  - `2-WebAPI/Flask-API/try_API.ipynb`
  - `2-WebAPI/Flask-Website/` (routing/templates examples)

### 1.4 Other data sources (web scraping, IoT)
- **Topics**: acquiring external data sources
- **Main materials**:
  - `0-Python-revisions/urls.py` (web-related examples)
  - `3-data-analysis/data/weather_data/get_weather_data.ipynb`
  - `3-data-analysis/data/portugal_meteo/` (weather-related datasets)

## 2) Data Analysis

### 2.1 Foundations (Series/DataFrames)
- **Main materials**:
  - `3-data-analysis/01_Intro-to-Pandas.ipynb`
  - `3-data-analysis/02_Series.ipynb`
  - `3-data-analysis/03_Dataframes.ipynb`
  - Exercises in `3-data-analysis/Exercises/`

### 2.2 Exploratory data analysis
- **Topics**: visualization, descriptive stats, missing data, grouping, data preparation
- **Main materials**:
  - `3-data-analysis/04_a_exploratory_data_analysis.ipynb`
  - `3-data-analysis/04_b_exploratory_data_analysis.ipynb`
  - `3-data-analysis/04_c_exploratory_data_analysis.ipynb`
  - `3-data-analysis/04_d_exploratory_data_analysis.ipynb`
  - Corresponding exercises and draft solutions

### 2.3 Time-series analysis and tooling
- **Main materials**:
  - `3-data-analysis/05_a_getting_started_with_TS.ipynb`
  - `3-data-analysis/05_b_exploring_TS.ipynb`
  - `3-data-analysis/05_c_storing_TS (optional).ipynb`
  - `3-data-analysis/07_regression_in_TS.ipynb`

### 2.4 Text/data mining applications
- **Main materials**:
  - `3-data-analysis/08_a_text.ipynb`
  - `3-data-analysis/Exercises/08_a_text.ipynb`
  - Supporting datasets in `3-data-analysis/data/IMDB/` and `3-data-analysis/data/FootballEvent/`

## 3) Applications

### 3.1 Time series
- **Main materials**:
  - `3-data-analysis/05_a_getting_started_with_TS.ipynb`
  - `3-data-analysis/05_b_exploring_TS.ipynb`
  - `3-data-analysis/07_regression_in_TS.ipynb`

### 3.2 Anomaly detection
- **Main materials**:
  - `3-data-analysis/06_anomaly_detection_TS.ipynb`
  - `3-data-analysis/Exercises/06_anomaly_detection_TS.ipynb`

### 3.3 Dashboarding and communication
- **Main materials**:
  - `4-dashboarding/00_intro.ipynb`
  - `4-dashboarding/01_components.ipynb`
  - `4-dashboarding/03_computer_monitor.py`
  - `4-dashboarding/04_stocks_dashboard.py`
  - `4-dashboarding/05_swipe.ipynb`

### 3.4 Recommendation systems
- **Current status**: no clearly dedicated notebook/module yet.
- **Recommended addition**:
  - `3-data-analysis/09_recommender_systems.ipynb`
  - `3-data-analysis/Exercises/09_recommender_systems_exercises.ipynb`
