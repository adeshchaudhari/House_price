import pickle
import config

class usa_house_price():
    def __init__(self,Avg_AreaIncome, Avg_AreaHouseAge,
     Avg_AreaNumberofRooms,
       Avg_AreaNumberofBedrooms, 
       Area_Population, Price):

       self.Avg_AreaIncome =Avg_AreaIncome  
       self.Avg_AreaHouseAge = Avg_AreaHouseAge
       self.Avg_AreaNumberofRooms = Avg_AreaNumberofRooms
       self.Avg_AreaNumberofBedrooms= Avg_AreaNumberofBedrooms
       self.Area_Population = Area_Population
       self.Price = Price

    def load_model(self):
        with open(config.model_file_path, 'rb') as f:
            model = pickle.load(f)

    def get_predicted_price(self):
        self.load_model()
        test_array = len(self.json_file_path['columns'])

Avg_AreaIncome = 79545
Avg_AreaHouseAge = 5.682861
Avg_AreaNumberofRooms = 7.009188	
Avg_AreaNumberofBedrooms = 4
Area_Population = 23086.800503
price = 21203949233

price_1 = usa_house_price(Avg_AreaIncome, Avg_AreaHouseAge,
     Avg_AreaNumberofRooms,
       Avg_AreaNumberofBedrooms, 
       Area_Population,price)

price_1.get_predicted_price()