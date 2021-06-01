# Donovan Carr
class Item:
    def __init__(self, sku, weight, value, description):
        self.__sku = sku
        self.__weight = weight
        self.__value = value
        self.__description = description

# I might need to set the object data

    def get_sku(self):
        return self.__sku # Product number or something like a barcode
    
    def get_weight(self):
        return self.__weight
    
    def get_value(self):
        return self.__value
    
    def get_description(self):
        return self.__description
    
    def __str__(self):
        return 'SKU:' + self.__sku, ', Weight:' + self.__weight, ', Value:'+ self.__value, ', Description:' + self.__description
    