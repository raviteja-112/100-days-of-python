import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "iambatman"
TOKEN = "ddfdlfj787$^^dlfhe81"
user_params = {
    "token":TOKEN,
    "username":"iambatman",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# get = getting data from server
# post = placing data to server
# put = updating data to server
# deleter = deleting data from server

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id":"graph1",
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"ajisai"

# }

# headers = {
#     "X-USER-TOKEN" : TOKEN
# }
# # response = requests.post(url = graph_endpoint,json = graph_config,headers=headers)
# # print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

post_config = {
    "date":"20240604",
    "quantity":"16.3"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)
DATE = 20240604
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{DATE}"

# put_config = {
#     "quantity":"4.6"
# }

# response = requests.put(url = put_endpoint,json=put_config,headers=headers)
# print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{DATE}"

respone = requests.delete(url = delete_endpoint,headers=headers)
print(respone.text)