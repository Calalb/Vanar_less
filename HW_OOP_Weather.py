import datetime

class Weather():

    def __init__(self, d, m, y, mint, maxt, s):
        self.data = {
            'day': d,
            'month': m,
            'year': y
        }
        self.temperature = {
            'minTemp': mint,
            'maxTemp': maxt,
            'avrTemp': (mint + maxt)/2
        }
        self.sky = s
       
    def convData(self):
        datetime_object = datetime.datetime.strptime(str(self.data['month']), "%m")
        month_name = datetime_object.strftime("%b")
        return (month_name)
    def __str__(self):
        return f"Wheater [{self.data['day']} {self.convData()} {self.data['year']}], averange temperature is {self.temperature['avrTemp']:3}C, the sky is {self.sky}\n"

    def __gt__(self, other):
        return self.temperature['avrTemp'] > other.temperature['avrTemp']

    def __eq__(self, other):
        return self.temperature['avrTemp'] == other.temperature['avrTemp'] and self.sky == other.sky
d1 = Weather(19, 8, 2020, 10, 22, 'clear')
d2 = Weather(20, 8, 2020, 12, 24, 'clear')
print(d1)
print(d2)

if d1 > d2:
    print("Today is hotter than it will be TOMORROW")
else:
    print("Tomorrow will be hotter than TODAY")

if d1 == d2:
    print("The weather tomorrow will be like today")


