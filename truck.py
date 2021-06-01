# Donovan Carr
class Truck:
    def __init__(self, id_num, plate, capacity):
        self.__id_num = id_num
        self.__plate = plate
        self.__content = []
        self.__capacity = capacity
        
#    def set_id_num(self, id_num):
#        self.__id_num = id_num
        
#    def set_plate(self, plate):
#        self.__plate = plate
                                         # not sure if i need the set data        
#    def set_content(self, content):
#        self.__content = []
# I almost for got that content was a list []

#    def set_capacity(self, capacity):
#        self.__capacity = capacity
        
    def get_id_num(self):
        return self.__id_num
    
    def get_plate(self):
        return self.__plate
    
    def get_content(self):
        return self.__content
    
    def get_capacity(self):
        return self.__capacity
    
    def __str__(self):
        return self.__id_num + ',' + self.__plate + \
               ', Capacity:' + str(self.__capacity)
    
    def Add_Item(self, more_item):
        num_of_items = len(self.__content)
        print('There is', num_of_items, 'items abord Truck id:', self.__id_num, '.')
        if num_of_items < self.__capacity:
            self.__content.append(more_item)
        else:
            print('Unable to add items to truck', self.__id_num)
            
            
    def Remove_Item(self, put_back_item):
        search_item = False
        for inventory in self.__content:
            print('Checking SKU:', inventory.get_sku())
            if inventory.get_sku() == put_back_item:
                search_item = True
                print('Item found')
            try:
                self.__content.remove(inventory)
                print('The item was removed')
            except ValueError:
                print('Unable to remove the item SKU:', put_back_item)
            if search_item:
                break