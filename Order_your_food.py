Hotel_location=[{"Southchennai":["Teynampet","Thousand Lights","Gopalapuram","Mylapore"],"Northchennai":["Red Hills","Royapuram","Korukkupet","Vyasarpadi"]}]

Hotel_list={"Teynampet":["Pandiyan Non veg hotel","Raja veg and Non veg hotel","Phachiamman veg hotel"],
            "Thousand Lights":["Taj Hotel","Annaporna pure Veg hotel","Ruchi Non veg hotel"],
            "Gopalapuram":["Vinayaga Pure veg hotel","Murugan idily kadi","Thala-Thalayathy hotel"],
            "Mylapore":["Manoj bhavan Non veg hotel","saravana bhavan","Adayar Aanatha Bhavan"],
            "Red Hills":["Italy Style food","Quick Brunch","Palmshore"],
            "Royapuram":["Mani Tiffen Center ","Raju veg Resturant","Bhommi Soup store"],
            "Korukkupet":["Vidhya Tiffen center","Rajam mess","Meat to Eat"],
            "Vyasarpadi":["Hunted House","Ghost Hall","Kaiyenthi bhavan"]}

class Hotels:

    print("************************************* Welcome to Swiggy **********************************")
          
    def __init__(self):

        print (" the locations are :")
        for i in Hotel_location:
            #print(i)
            for j in i.values():
                print("\n",j)

        self.area=input("\n Enter the area : ")
        #print(self.__area)


    def hotels(self):   

        if isinstance(self.area,str):
            print("The hotels are:")
            if self.area in Hotel_list.keys():
               lst= Hotel_list[self.area]
               for i in lst:
                   print("\n",i)
            else:
                raise ValueError("not present")
        else:
            raise TypeError("invalid data type")

        self.hotel_name=input("\n Enter the hotel name : ")
        if isinstance(self.hotel_name,str):
            if (self.hotel_name  in lst):
                pass
            else:
                raise TypeError("Hotel not found")
        else:
            raise ValueError("invalid data type")
        

    def menu(self):

        if(self.hotel_name == "Pandiyan Non veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")
                
        elif(self.hotel_name == "Raja veg and Non veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Phachiamman veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Taj Hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Annaporna pure Veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Ruchi Non veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Vinayaga Pure veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Murugan idily kadi"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Thala-Thalayathy hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Manoj bhavan Non veg hotel"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "saravana bhavan"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Adayar Aanatha Bhavan"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Italy Style food"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Quick Brunch"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Palmshore"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Mani Tiffen Center "):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Raju veg Resturant"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Bhommi Soup store"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Vidhya Tiffen center"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Rajam mess"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Meat to Eat"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Hunted House"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

        elif(self.hotel_name == "Ghost Hall"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")


        elif(self.hotel_name == "Kaiyenthi bhavan"):
                print( " \n The food Avalible are : ")
                print("___________________________")
                print("\n 1. Butter Non","\n 2. Chicken Briyani","\n 3. Chappathi and veg kuruma")

                
    def  order_food(self):
        self.order_food=input("\n Order your food : ")
        
        if(self.order_food =="Butter Non"):
             print("\n you had ordered butter non","\n The price is Rs:50")
            
             
        elif(self.order_food =="Chicken Briyani"):
             print("\n you had ordered Chicken briyani","\n The price is Rs:90")
             
             
        elif(self.order_food =="Chappathi and veg kuruma"):
             print("\n you had ordered Chappati and veg kuruma","\n The price is Rs:45")
            
             
    def bill(self):

        print("===================Ordered Details==============")
        print("you had ordered : " ,self.order_food )


print("Thanks for using this App")

         
        
object1=Hotels()
object1.hotels()
object1.menu()
object1.order_food()
object1.bill()


            
            
        
                

                       
                       




        
