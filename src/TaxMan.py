class TaxMan():
    
    def __init__ (self, items, percent):
        self.items = items
        percent = percent.split("%")
        self.percent = percent[0]
        self.__total = 0.00
        
    
    def calc_total(self):
        self.__total = sum(item['price'] for item in self.items)
        
    def get_total(self):
        self.__total += float(self.__total) * (float(self.percent)/100)
        return self.__total