import urllib.request,json
url=http://api.openweathermap.org/data/2.5/forecast/""daily?cnt=7&units=meteric&mode=json7q=london"
req=urllib.request.Request(url)
forecast_string=yrllib.request.urlopen(req).read()
forecast_dict=json.loads(forecast_string.decode("UTF_8"))
print(forecast_dict)
