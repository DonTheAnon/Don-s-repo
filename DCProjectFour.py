# Donovan Carr
import truck
import item
import boto3
import credentials
from datetime import datetime

print('DEFINING S3 RESOURCE.')

s3 = boto3.client('s3',
    aws_access_key_id = credentials.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = credentials.AWS_SECRET_ACCESS_KEY)

print('BEGINNING DOWNLOADING TWO FILES.')

s3.download_file('nlc-data-files', 'fleet.txt', 'C:/Data/fleet.txt')
s3.download_file('nlc-data-files', 'loading.txt', 'C:/Data/loading.txt')

print('FINISHED')

def main():
    Trucks = []
    
    ListTrucks(Trucks)
    
    ListItems(Trucks)
    
    DisplayReport(Trucks)
    
def ListTrucks(Trucks):
    print('Truck list created')
    TruckInfo = open('C:/Data/fleet.txt', 'r')
    for info in TruckInfo:      # I put info instead of chunk and it ended up ignoring line 32
        chunk = info.split(',') # started printing each number starting from the first string in the file
        id_num = chunk[0]       # and that was why it was saying I defined indTrucks as 'int' causing an error
        # Truck id number
        plate = chunk[1]        
        # Truck plate number
        capacity = int(chunk[2])
        # Truck carrying wieght
        new_Truck = truck.Truck(id_num, plate, capacity) # this line puts the data in the file into objects
        Trucks.append(new_Truck) # this line puts the objects into the list(argument) created in main
    TruckInfo.close()
    
    count = len(Trucks)
    print(count, 'Trucks are in the lot')
    for indTrucks in Trucks: # I almost tried to print out a list for count and not Trucks
        print(' ', indTrucks)

def ListItems(Trucks):
    print('Item list created')
    Freight = open('C:/Data/loading.txt', 'r')
    
    productNum = 0
    skipNum = 0
    
    for product in Freight:
        productNum += 1
        chunk = product.split(',')
        
        code = chunk[0]
        # add or remove code
        id_num = chunk[1]
        # Truck id number
        sku = chunk[2]
        
        description = None
        for Goods in Trucks:
            if Goods.get_id_num() == id_num:
                description = Goods
                break
        if description is None:
            skipNum += 1
            print('Record', productNum, 'Skipped for invalid ID:', id_num)
            continue
        
        if code == 'A':
            weight = chunk[3]
            value = chunk[4].rstrip('\n')
            new_Items = item.Item(sku, weight, value, description)
            description.Add_Item(new_Items)
            
        elif code == 'R':
            print('Attempting to remove Item:', sku)
            description.Remove_Item(new_Items)
                
        else:
            skipNum += 1
            print('Record', productNum, 'Skipped for invalid code:', code)
                
    Freight.close()
    print(productNum, 'Items are shipped from the WareHouse.', skipNum, 'invalid items are removed from shipment\n')
            
def DisplayReport(Trucks):
    print('Report created')
    NewFile = open('C:/Data/Report.txt', 'w')
    NewFile.write('Donovan L. Carr for the CarrBros Shipping Company, Ltd.\n')
    now = datetime.now()
    time = now.strftime("%B %d, %Y %H:%M:%S")
    print(time)
    NewFile.write('Prepared on:')
    NewFile.write(str(time) + '\n')
    NewFile.write('LOADING REPORT\n')
    for truckID in Trucks:
        truckID = truck.Truck.get_id_num(truckID)
        print('ID:', truckID)
        NewFile.write(str(truckID) + '\n')
        
    for truckPlate in Trucks:
        truckPlate = truck.Truck.get_plate(truckPlate)
        print('Plate:', truckPlate)
        NewFile.write(str(truckPlate) + '\n')
        
    for truckcap in Trucks:
        truckcap = truck.Truck.get_capacity(truckcap)
        print('Capacity:', truckcap)
        NewFile.write(str(truckcap) + '\n')
        
#    NewFile.write(str(truckID) + ' ' + str(truckPlate)+ ' ' + str(truckcap))
        
#    for unite in Trucks:
#        unite = item.Item.get_sku(unite)
#        print('SKU:', unite)
# It kept saying I that the Item class did not have the data from loading.txt    
    NewFile.close()

main()