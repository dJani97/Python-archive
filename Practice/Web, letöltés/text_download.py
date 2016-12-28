from urllib import request

google = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=28&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

def download_text (input_url):
    response = request.urlopen(input_url)
    data = response.read()
    data_str = str(data)
    lines = data_str.split("\\n")
    dest_url = r"goog.scv"
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close


download_text(google)