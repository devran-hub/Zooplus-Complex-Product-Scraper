from bs4 import BeautifulSoup
import requests
import json
import csv

url = "https://www.zooplus.co.uk/"
response = requests.get(url).content

soup = BeautifulSoup(response,"html.parser")
categories = soup.find("div",{"class":"LeftNavigation_navigationContent__18usf"})
categories_list = list()
for href in categories.find_all("a"):
    categories_list.append("https://www.zooplus.co.uk/"+href["href"])

brand_link_list = list()
other_link_list = list()


for link in categories_list:
    new_response = requests.get(link).content
    new_soup = BeautifulSoup(new_response,"html.parser")
    new_list = new_soup.find_all(class_="ProductGroupListNavigation_productGroupLinksContainer__xawig")
    if len(new_list) == 0:
        lim = new_soup.find ("ul", {"class" : "MainNavigation_mainNavigationGrid__eLHxx"})
        for y in lim.find_all("li"):
            resp = requests.get("https://www.zooplus.co.uk/"+y.div.a["href"]).content
            sp = BeautifulSoup (resp, "html.parser")
            lis = sp.find(class_="ProductGroupListNavigation_productGroupLinksContainer__xawig")
            try:
                for i in lis.find_all("li"):
                    brand_link_list.append ("https://www.zooplus.co.uk/" + str(i.a["data-pg-link"]))
            except:
                continue
    for x in new_list:
        for brand in x.find_all("a"):
            brand_link_list.append("https://www.zooplus.co.uk/"+str(brand["data-pg-link"]))

product_links = list()
for brand in brand_link_list:
    new_response = requests.get(brand).content
    new_soup = BeautifulSoup(new_response,"html.parser")
    products = new_soup.find_all("div",{"class":"ProductListWrapper-module_productListWrapper__sMiJ4"})
    for x in products:
        for product in x.find_all("a"):
            if product["href"].startswith("/shop"):
                product_links.append("https://www.zooplus.co.uk/"+product["href"])
            else:
                continue


product_links = list(set(product_links))
Animals = ["Dog","Cat","Rabbit","Hamster","Guinea Pig","Gerbil","Ferret","Rat","Budgie","Canary","Ferplast"]
types = ["Bird","Small Pet"]

with open ("products.csv", "w") as csv_file :
    c = csv.writer (csv_file)
    c.writerow (["product", "price", "image url", "description", "SKU", "Animal", "Rating", "Category"])
    for product in product_links:
        try:
            re = requests.get (product).content
            bsoup = BeautifulSoup (re, "html.parser")
            jsonx = bsoup.find("script", {"type" : "application/ld+json"}).text
            dicts = json.loads(str(jsonx))
        except:
            continue
        for info in dicts["offers"] :
            rating = 0
            product = dicts["name"]

            price = info["price"]

            image_url = dicts["image"]

            description = BeautifulSoup(dicts["description"],"html.parser").get_text()

            SKU = info["sku"]

            rate = bsoup.find ("div", class_="Bar_ratingStars__gNYgb Bar_ratingStarsLink__mpUt6 Bar_subRating__1zZ6-")
            try:
                for r in rate.find_all("svg") :
                    if r["role"] == "full-star" :
                        rating += 1
            except:
                continue

            path = bsoup.find ("ul", class_="Breadcrumbs_breadcrumbs__3zXcF")
            categories = path.find_all ("li")
            category = ""
            for x in categories[2 :len (categories) - 1] :
                category += str(x.a["title"]) + " > "
            whole_name = category + categories[-1].text
            category = category[:-3]

            Animal = ""
            for i in Animals :
                if i in whole_name :
                    Animal = i
            if Animal == "" :
                for i in types :
                    if i in whole_name :
                        Animal = i

            c.writerow ([product, price, image_url, description, SKU, Animal, rating, category])
