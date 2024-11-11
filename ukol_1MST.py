
import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def calculate_tax(self):
        # Koeficienty pro typy pozemků
        estate_type_coefficients = {
            'land': 0.85,
            'building site': 9,
            'forrest': 0.35,
            'garden': 2
        }
        
        estate_coefficient = estate_type_coefficients.get(self.estate_type, 1)
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        return math.ceil(tax)
    
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        base_tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
           base_tax = base_tax * 2
        return math.ceil(base_tax)


# Manětín lokalita s koeficientem 0.8
manetin = Locality("Manětín", 0.8)
# Brno lokalita s koeficientem 3
brno = Locality("Brno", 3)

# Zemědělská půda Manětín
agricultural_land = Estate(manetin, "land", 900)
print("Daň za zemědělský pozemek:", agricultural_land.calculate_tax())  #  612

# Dům Manětín
house = Residence(manetin, 120, commercial=False)
print("Daň za dům:", house.calculate_tax())  # 1440

# Kancelář Brno
office = Residence(brno, 90, commercial=True)
print("Daň za kancelář:", office.calculate_tax())  # Expected: 8100