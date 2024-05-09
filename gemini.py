import re

def extract_restaurant_info(text_list):
    restaurants = []
    for text in text_list:
        # Extract restaurant name
        name_match = re.search(r"^([^;]+);", text)
        if name_match:
            name = name_match.group(1)

        # Extract address
        address_match = re.search(r"[\w\s]+(?= ⋅)", text)
        if address_match:
            address = address_match.group()

        # Extract price range
        price_range_match = re.search(r"€(\d+)", text)
        if price_range_match:
            price_range = price_range_match.group(1)
        else:
            price_range = None

        # Extract cuisine type
        cuisine_type_match = re.search(r"(?:Italiaans|Restaurant) · [\w\s]+", text)
        if cuisine_type_match:
            cuisine_type = cuisine_type_match.group()
        else:
            cuisine_type = None

        # Extract opening hours
        opening_hours_match = re.search(r"Geopend ⋅ Sluit om ([\d:]+)", text)
        if opening_hours_match:
            opening_hours = opening_hours_match.group(1)
        else:
            opening_hours = None

        # Extract closing hours
        closing_hours_match = re.search(r"Sluit binnenkort ⋅ ([\d:]+) ⋅ Gaat open op ([\w\s]+) om ([\d:]+)", text)
        if closing_hours_match:
            closing_hours = closing_hours_match.group(1)
            reopening_day = closing_hours_match.group(2)
            reopening_time = closing_hours_match.group(3)
        else:
            closing_hours = None
            reopening_day = None
            reopening_time = None

        # Extract rating
        rating_match = re.search(r"([\d.]+)\(", text)
        if rating_match:
            rating = rating_match.group(1)
        else:
            rating = None

        # Extract number of reviews
        reviews_match = re.search(r"([\d]+) reviews", text)
        if reviews_match:
            number_of_reviews = reviews_match.group(1)
        else:
            number_of_reviews = None

        restaurant_info = {
            "name": name,
            "address": address,
            "price_range": price_range,
            "cuisine_type": cuisine_type,
            "opening_hours": opening_hours,
            "closing_hours": closing_hours,
            "reopening_day": reopening_day,
            "reopening_time": reopening_time,
            "rating": rating,
            "number_of_reviews": number_of_reviews
        }

        restaurants.append(restaurant_info)

    return restaurants

if __name__ == "__main__":
    text_list = [
        'Bar en Bistro Raposa;Bar en Bistro Raposa\n4,6(263) · €€\nRestaurant · Vossenstraat 2\nGeopend ⋅ Sluit om 23:00',
        'Tokyo Sushi;Tokyo Sushi\n4,5(125) · €€\nRestaurant · Brusselsesteenweg 277\nGeopend ⋅ Sluit om 21:30',
        'Pitta Maestro;Pitta Maestro\n3,3(43)\nRestaurant · Brusselsesteenweg 200\nGeopend ⋅ Sluit om 00:00',
        'La Brasseria De Middenstand;La Brasseria De Middenstand\n4,3(483) · €€\nItaliaans · Hundelgemsesteenweg 281\nGeopend ⋅ Sluit om 22:00',
        ''t Fornuizeke;''t Fornuizeke\n4,6(405) · €€\nRestaurant · Mellestraat 286\nSluit binnenkort ⋅ 21:00 ⋅ Gaat open op wo om 12:00',
        'Ristorante Pizzeria Da Toto;Ristorante Pizzeria Da Toto\n4,5(47)\nItaliaans · Brusselsesteenweg 56\nGeopend ⋅ S
