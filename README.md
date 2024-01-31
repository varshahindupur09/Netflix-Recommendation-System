# Netflix Recommendation System
Tried Different Recommendation Algorithms on Netflix Prize Data downloaded from Kaggle

# Important Git commands
conda deactivate
git remote origin main https://github.com/varshahindupur09/NetflixRecommendationSystem.git
git add .
git commit -m "update" 
git push origin main
git pull origin main

# Exploratory Data Analysis (EDA)


![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/87559809-990d-4799-ad13-a2ce93aadee1)


![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/325fd0d0-6378-483b-bbcb-2c565f5f7513)


![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/5c73a3cc-a7d3-4493-bc6a-283b416dccb3)

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/c36253b8-ec3e-4139-afcc-24fca468ce66)

# Collaborative Filtering

To address some of the limitations of content-based filtering, collaborative filtering uses similarities between users and items simultaneously to provide recommendations. This allows for serendipitous recommendations; that is, collaborative filtering models can recommend an item to user A based on the interests of a similar user B. Furthermore, the embeddings can be learned automatically, without relying on hand-engineering of features.

Tech Stack: Scikit-Surprise

Results:

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/8c985474-7d00-4004-abc5-b3584e8b4749)

Best RMSE: 0.9892


# Analyzed Data with respect to movie titles

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/62fa74d0-fbed-42c0-a9f5-f993f248cb5e)

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/4af29e50-666d-4f80-9659-38beb228e03d)

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/f4007355-ba93-4f51-950b-540c55cda7d5)

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/9e521b0b-b7ea-4662-8220-6fb86fb4f446)

![image](https://github.com/varshahindupur09/Netflix-Recommendation-System/assets/114629181/fbc1f69f-028b-4dd4-8028-d97d0a970e5f)


# All the execution is done on Northeastern's Discovery - High Performance Computing Cluster (HPP)

I loved the recommendations!


# Future Action Plans:

- Added innovative ‘Mood  Chart’ in the which reflected if someone is happy or depressed
(I am developing a scripts for this Mood Chart or Mood based recommendation). Furthermore, I am writing codes for scrapping IMDB genres for the listed movies as it can also assist in determining mood/ different types of movies user has recently watched in a form of a dashboard. (Stay Tuned!) 

# What is already done? 
- Cleansed, Refined and completely integrated Netflix Prize Data (set of txt files) into a single CSV that contains User Ratings, Customer Id (User Id), Movie IDs, Movie Title, User Ratings Date, Genre, and Release Year

- Added Collaborative Filtering process that is recommending a specific user what to watch based on their watch history

- Every code is getting executed on Discovery (Northeastern's High Performance Computing VM) on MAC OS






