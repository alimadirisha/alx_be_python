# Prompt user for for current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Give the user recommendations based on weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")

else:
    print("I don't have recommendations for this weather")