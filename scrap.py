import requests
from bs4 import BeautifulSoup
url = 'https://www.flipkart.com/search?q=sneakers&marketplace=FLIPKART&otracker=start&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D3000&p%5B%5D=facets.price_range.to%3DMax'
scrapped_data = requests.get(url)

soup = BeautifulSoup(scrapped_data.content)

sneakers_arr = soup.find_all("div", {"class":"_3liAhj _1R0K0g"})

sneakers_json = {};


for i,sneakers in enumerate(sneakers_arr):
	sneakers_json[i] = {
		"pageURL":"",
		"coverImage":"",
		"altText":"",
		"title":"",
		"price":0,
		"starRating":0,
		"starRatingBy":0,
		"totalReviews":"",
		"totalReviewsBy":0,
		"sizes":[],
		"images":[],
		"availableColors":[]

	};
	sneakers_json[i]["pageURL"] = sneakers.a["href"]
	cover_img_data = sneakers.find_all("div",{"class":"_3BTv9X"})
	img_data = cover_img_data[0].find('img');
	sneakers_json[i]["altText"] = img_data["alt"]
	sneakers_json[i]["title"] = img_data["alt"]
	sneakers_json[i]["coverImage"] = img_data["src"]
	star_rating_div = sneakers.find("div",{"class":"niH0FQ _36Fcw_"})
	if star_rating_div: #if Rating is available
		star_rating_spans = star_rating_div.find_all("span")
		sneakers_json[i]["starRating"] = star_rating_spans[0].find("div").getText() # write a logic to parse this
		sneakers_json[i]["starRatingBy"] = star_rating_spans[1].getText() # write a logic to parse this

	sneakers_json[i]["price"] = sneakers.find("div",{"class":"_1vC4OE"}).getText();

	sneaker_page_url = 'https://www.flipkart.com'+sneakers_json[i]["pageURL"]
	shoe_page_data = requests.get(sneaker_page_url)
	print shoe_page_data.content

	#print starRating
	

print sneakers_json


#print sneakers_arr
