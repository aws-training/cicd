import requests
url_get="https://xqww3m5tk3.execute-api.ap-south-1.amazonaws.com/dev/item"
url_post="https://sce050h38j.execute-api.ap-south-1.amazonaws.com/dev/cart"
headers={"Content-Type":"application/json"}
payload="""{
	"items": ["123","233444"],
	"user": "Ravi"
}
"""
response_get=requests.request("GET",url_get,headers=headers)
print(response_get.text)


#response_post=requests.request("POST",url_post,headers=headers,data=payload)
#print(response_post.text)
