# Prompt user for waether input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Give the user recommendations based on weather input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
    
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
    
elif weather == "cold":
    print("Make sure to wear a warmcoat and a scarf.")
    
else:
    print("I dont have reccomendations for this weather.")