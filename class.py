def main():
    class Car:
        def __init__(self, name: str, brand: str, color: str, year: int, is_new: bool):
            self.name = name
            self.brand = brand
            self.color = color
            self.year = year
            self.is_new = is_new

            min_year = 1950
            max_year = 2025
            if not (min_year <= self.year <= max_year):
                raise ValueError(
                    f"Error while creating car '{self.name}': Invalid year ({self.year}). "
                    f"The year must be between {min_year} and {max_year}."
                )

            allowed_brands = {"Chevrolet", "Volkswagen", "Mitsubishi"}
            if self.brand not in allowed_brands:
                raise ValueError(
                    f"Error while creating car '{self.name}': Invalid brand ({self.brand}). "
                    f"Allowed brands are: {', '.join(sorted(allowed_brands))}."
                )

        def drive(self):
            print(f"I'm driving a {self.year} {self.color} {self.brand} {self.name}.")

    class SportsCar(Car):
        # This class inherits everything from Car.
        # No explicit __init__ is needed if no new attributes or logic are added.
        pass

    try:
        fox = Car("Fox", "Volkswagen", "Red", 2015, False)
        fox.drive()

        cobalt = Car("Cobalt", "Chevrolet", "Black", 2023, True)
        cobalt.drive()

        pajero = SportsCar("Pajero", "Mitsubishi", "Silver", 2005, False)
        pajero.drive()

        lancer = SportsCar("Lancer Evolution", "Mitsubishi", "White", 2008, False)
        lancer.drive()

        # Examples that would raise errors:
        # invalid_year_car = Car("Old Beetle", "Volkswagen", "Blue", 1900, False)
        # invalid_year_car.drive()

        # invalid_brand_car = Car("Civic", "Honda", "Gray", 2020, False)
        # invalid_brand_car.drive()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
