import requests
from requests import exceptions
import pandas as pd

"""Ejercicio 1"""

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    
    def __init__(self):
        pass

    @classmethod
    def is_hot_in_pehuajo(cls):
        params = {
            "lat": cls.LAT,
            "lon": cls.LON,
            "appid": cls.API_KEY,
            "units": "metric"
        }
        try:
            data = cls.get_weather(params)
            return data["main"]["temp"] > 28
        except exceptions.HTTPError:
            return False

    @staticmethod
    def get_weather(params):
        """Static method to get the weather from the API."""
        URL = "https://api.openweathermap.org/data/2.5/weather?"
        response = requests.get(URL, params=params)
        return response.json()

#Ejercicio 2.1

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate",
"Granizado", "Limon", "Dulce de Leche"], "quantity":
[3,10,0,5]})

def is_product_available(product_name, quantity):
    """Function to check if a product is available in the inventory."""
    """Args:
        product_name (str): The name of the product.
        quantity (int): The quantity of the product.
    Returns:
        bool: True if the product is available, False otherwise.
    Manage exception for evade infinite loop Ejercicio 2.2
    """
    try:
        # Filter the product dataframe by the product name
        product_df_filtered = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]

        if product_df_filtered.empty:
            raise ValueError(f"Product {product_name} not found")
        # Get the quantity of the product
        product_quantity = product_df_filtered["quantity"].values[0]

        if product_quantity < quantity:
            raise ValueError(f"Not enough quantity of {product_name} available")
        
        # Devolver si el producto está disponible
        return True
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print("Ejercicio 1, resultado: ", GeoAPI.is_hot_in_pehuajo())
    print("Ejercicio 2.1, resultado: ", is_product_available("Chocolate", 3))