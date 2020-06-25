import requests as req

url = 'https://www.w3schools.com/python/demopage.php'
myObj = {'sampleKey': 'sampleValue'}

response = req.post(url, data = myObj)

print(response)