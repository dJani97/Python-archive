
class Year:
    def __init__(self, year, happy):
        self.year = year
        self.happy = happy

    def __str__(self):
        return "{} is {}".format (self.year,  "happy" if self.happy else "sad") 
    

ev = Year(year = 2017, happy = True)

print (str(ev))
