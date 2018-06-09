import requests
from bs4 import BeautifulSoup
import unicodedata
import json

url = 'https://www.flipkart.com/search?q=sneakers&marketplace=FLIPKART&otracker=start&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D3000&p%5B%5D=facets.price_range.to%3DMax'
scrapped_data = requests.get(url)

soup = BeautifulSoup(scrapped_data.content)

sneakers_arr = soup.find_all("div", {"class":"_3liAhj _1R0K0g"})

sneakers_json = [];


for i,sneakers in enumerate(sneakers_arr):
	temp_obj = {
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
	temp_obj["pageURL"] = sneakers.a["href"]
	cover_img_data = sneakers.find_all("div",{"class":"_3BTv9X"})
	img_data = cover_img_data[0].find('img');
	temp_obj["altText"] = img_data["alt"]
	temp_obj["title"] = img_data["alt"]
	temp_obj["coverImage"] = img_data["src"]
	star_rating_div = sneakers.find("div",{"class":"niH0FQ _36Fcw_"})
	if star_rating_div: #if Rating is available
		star_rating_spans = star_rating_div.find_all("span")
		star_rating  = star_rating_spans[0].find("div").getText()
		temp_obj["starRating"] = unicodedata.normalize('NFKD', star_rating).encode('ascii','ignore')
		temp_obj["starRatingBy"] = str(star_rating_spans[1].getText())[1:-1] # write a logic to parse this

	

	price = sneakers.find("div",{"class":"_1vC4OE"}).getText();

	temp_obj["price"] = unicodedata.normalize('NFKD', price).encode('ascii','ignore')


	sneaker_page_url = 'https://www.flipkart.com'+temp_obj["pageURL"]
	#print sneaker_page_url


	shoe_page_data = requests.get(sneaker_page_url);
	child_soup = BeautifulSoup(shoe_page_data.content)

	rating_review_unparsed = child_soup.find("span",{"class":"_38sUEc"});
	child_soup.find("div",{"class":"_1vC4OE _3qQ9m1"}); # tryng to access price on different page

	try:
		colours_lis = child_soup.find("div",{"class":"_2a2WU_ _2PBcpj"}).ul;
		
		for colors_li in colours_lis:
				temp_obj["availableColors"].append(colors_li.a["data-img"].replace("{@width}","100").replace("{@height}","100").replace("{@quality}","100"))
	except Exception as e:
		#print e
		#  means no colors available
		pass

	size_anchors = child_soup.find_all("a",{"class":"_2_26Ng _5FnwXU"})
	for a in size_anchors:
		temp_obj["sizes"].append(str(a.string))
	
	other_images = child_soup.find_all("div",{"class":"_2_AcLJ"})
	for div in other_images:
		image_url = div["style"]
		str_to_find = "background-image:url("
		start_i =  image_url.find(str_to_find)+len(str_to_find)
		end_i =  image_url.find(")",image_url.find(str_to_find));

		temp_obj["images"].append(image_url[start_i:end_i]);
	
	sneakers_json.append(temp_obj)
	
		#print size_li.a
	#break;
	#print colours_lis
	
	#print rating_review_unparsed
	


	#print shoe_page_data.content

	#print starRating
	

#print sneakers_json

f = open('data.json', 'a')
f.write(json.dumps(sneakers_json))  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it
#print sneakers_json
