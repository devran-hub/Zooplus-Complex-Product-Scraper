# Zooplus-Complex-Product-Scraper
A webscraper that scrapes product name, price, image link, description, SKU, Animal name, Rating, Category from https://www.zooplus.co.uk/

you can view the output of the script here: https://docs.google.com/spreadsheets/d/1as0r1LUOCalZYHqfsv5AHZldgVJSJMt5vm-aFDqYPFM/edit?usp=sharing

In this project i used: BeautifulSoup, Requests, CSV libraries

## Working process
1- Firstly script reaches category then it's sub-categories one by one

<img width="1064" alt="Ekran Resmi 2023-01-14 13 24 46" src="https://user-images.githubusercontent.com/73471656/212467970-16bb3791-25ae-4e69-adf5-c02b5e4b2e47.png">


2- Once you click a sub category for example 'Dry Dog Foods' you don't see products but you see brand links which shows products of the brand related to this sub-category. Therefore, the script scrapes brand links one by one.

<img width="1279" alt="Ekran Resmi 2023-01-14 13 28 48" src="https://user-images.githubusercontent.com/73471656/212468031-c52dc072-c2ad-43f3-a67c-376c746b6fe0.png">


3- By clicking each brand links you can see products of the brand which are related to the sub-category

<img width="806" alt="Ekran Resmi 2023-01-14 13 42 57" src="https://user-images.githubusercontent.com/73471656/212468154-807fc48b-e528-4869-a26e-cb215120a31e.png">

4- Finally, web scraper scrapes all the products of each brand links to scrape the whole sub-category then it does this for other sub-categories and categories
