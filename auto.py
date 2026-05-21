import requests 
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    if response.status_code == 200:
        result = [user["name"] for user in users ]
        print (result)
    else:
        print("API failed")
except Exception as e:
        print ("Error:", e)

