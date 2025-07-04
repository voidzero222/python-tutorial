import random

game_running = False


class Part:
    def __init__(
        self,
        name:str,
        speed_modifier:float=1,
        speed_offset:float=0,
        wind_resistance_modifier:float=1,
        wind_resistance_offset:float=0,
        weight_modifier:float=1,
        weight_offset:float=0,
        acceleration_modifier:float=1,
        acceleration_offset:float=0,
    ):
        self.name = name
        self.speed_modifier = speed_modifier
        self.speed_offset = speed_offset
        self.wind_resistance_modifier = wind_resistance_modifier
        self.wind_resistance_offset = wind_resistance_offset
        self.weight_modifier = weight_modifier
        self.weight_offset = weight_offset
        self.acceleration_modifier = acceleration_modifier
        self.acceleration_offset = acceleration_offset


class Nitro(Part):
    def __init__(
        self, name:str="Nitro", speed_offset:float=0, wind_resistance_offset:float=0, weight_offset:float=0
    ):
        self.speed_offset = speed_offset
        self.wind_resistance_offset = wind_resistance_offset
        self.weight_offset = weight_offset
        self.name = name

    def __str__(self)-> str:
        return (
            f"A {self.name} booster with a speed boost of {self.speed_offset},"
            f"it is heavy, affecting the weight by {self.weight_offset} "
            f"and the wind resistance by {self.wind_resistance_offset}."
        )


class Tire(Part):
    def __init__(self, name:str="Tires", speed_modifier:float=1):
        self.speed_modifier = speed_modifier
        self.name = name

    def __str__(self)->str:
        return f"A set of {self.name} that modify your speed by {self.speed_modifier}."


class Motor(Part):
    def __init__(
        self, name:str="Motor", weight_offset:float=0, acceleration_modifier:float=1, speed_modifier:float=1
    ):
        self.weight_offset = weight_offset
        self.acceleration_modifier = acceleration_modifier
        self.speed_modifier = speed_modifier
        self.name = name

    def __str__(self)->str:
        return (
            f"A {self.name}, that weighs {self.weight_offset},"
            f"and modifies your acceleration by {self.acceleration_modifier}."
            f"It additionally modifies your speed by {self.speed_modifier}."
        )


class Spoiler(Part):
    def __init__(self, name:str="Spoiler", wind_resistance_modifier:float=1, weight_offset:float=0):
        self.wind_resistance_modifier = wind_resistance_modifier
        self.weight_offset = weight_offset
        self.name = name

    def __str__(self)->str:
        return f"A {self.name} that impacts your wind resistance by {self.wind_resistance_modifier} and increases your weight by {self.weight_offset}."


class Car:
    def __init__(
        self, brand:str, model:str, base_speed:float, base_wind_resistance:float, weight:float, acceleration:float
    ):
        self.brand = brand
        self.model = model
        self.base_speed = base_speed
        self.base_wind_resistance = base_wind_resistance
        self.weight = weight
        self.acceleration = acceleration

        self.nitro = Nitro()
        self.tire = Tire()
        self.motor = Motor()
        self.spoiler = Spoiler()

    def __str__(self)->str:
        return (
            f"The {self.model} by {self.brand} speed:{self.base_speed}km/h "
            f"acceleration:{self.acceleration}kmh/s wind resistance:"
            f"{self.base_wind_resistance}cmÂ² weight:{self.weight}kg."
        )


CARS = [
    Car("VW", "Golf", 200, 1100, 1300, 20),
    Car("Mercedes", "CLA Coupe", 300, 900, 1650, 35),
    Car("Jeep", "Renegade", 220, 1200, 2000, 21),
    Car("Kia", "Soul", 210, 1000, 1400, 21),
    Car("Honda", "Civic Type R", 350, 800, 1200, 42),
    Car("Audi", "A7", 310, 950, 1500, 36),
]

NITROS = [
    Nitro("Bad Nitro", 35, 100, 45),
    Nitro("Alright Nitro", 50, 110, 60),
    Nitro("Good Nitro", 80, 160, 90),
]

TIRES = [
    Tire("Tires with holes", 1),
    Tire("Michelin Tires", 1.6),
    Tire("No holes Tires", 1.2),
]


MOTORS = [
    Motor("Barely working Motor", 100, 1.1, 1.1),
    Motor("I guess it works Motor", 120, 1.3, 1.4),
    Motor("Good Motor", 150, 1.5, 1.6),
]


SPOILERS = [
    Spoiler("Illuminati Spoiler", 0.8, 15),
    Spoiler("Broken in half Spoiler", 1, 8),
    Spoiler("Beautiful spoiler", 0.6, 20),
]


def speed_calculation(car:Car)->float:
    distance:float = 10000
    final_speed:float = (
        car.base_speed * car.motor.speed_modifier * car.tire.speed_modifier
    ) + car.nitro.speed_offset

    final_acceleration:float = car.acceleration * car.motor.acceleration_modifier

    effective_weight:float = (
        car.weight
        + car.motor.weight_offset
        + car.nitro.weight_offset
        + car.spoiler.weight_offset
    )

    effective_wind_resistance:float = (
        car.base_wind_resistance * car.spoiler.wind_resistance_modifier
    )

    final_speed -= effective_wind_resistance / 100
    final_speed -= effective_weight / 100
    race_time = distance / (final_speed * (final_acceleration / 10))
    return race_time


start = input(
    "Welcome to this little racing game! I hope you have fun! Type something in to start playing.\n>>>"
)
if start:
    game_running = True
else:
    exit()

while True:
    i = 0
    for car in CARS:
        print(f"[{i}] {car}")
        i += 1
    selection = input("Which car would you like to start with?\n>>>")
    try:
        current_car = CARS[int(selection)]
        break
    except ValueError:
        print("Only numbers, try again.")
    except IndexError:
        print("That wasn't a choice, try again.")
while game_running == True:
    player_choice = input(
        "What would you like to do?\n[C]Check Car\n[E]Equip Part\n[S]Select Car\n[P]Play race\n[exit]\n>>>"
    ).lower()
    options = ["c", "e", "s", "p", "exit"]
    if player_choice not in options:
        print("You dont have any other choices.")
    elif player_choice == "c":
        print(
            f"The {current_car.model} by {current_car.brand} has a speed of {current_car.base_speed}, "
            f"an acceleration of {current_car.acceleration}, the wind resistance of "
            f"{current_car.base_wind_resistance} all while weighing only {current_car.weight}kg."
        )
        print(
            f"The parts that it has installed are:\n{current_car.nitro}\n{current_car.tire}\n{current_car.motor}\n{current_car.spoiler}\n"
        )

    elif player_choice == "e":
        parts_options = ["n", "t", "m", "s", "g"]
        part_select = input(
            "What kind of part are you looking to change?\n[N]Nitro\n[T]Tires\n[M]Motor\n[S]Spoiler\n[G]Go back\n>>>"
        ).lower()
        if part_select not in parts_options:
            print("You dont have any other options, please try again.")

        elif part_select == "n":
            while True:
                i = 0
                for nitro in NITROS:
                    print(f"[{i}] {nitro}")
                    i += 1
                selection_nitro = input("Which Nitro do you want to choose?\n")
                try:
                    current_car.nitro = NITROS[int(selection_nitro)]
                    break
                except ValueError:
                    print("Only numbers, try again.")
                except IndexError:
                    print("That wasn't a choice, try again.")
        elif part_select == "t":
            while True:
                i = 0
                for tire in TIRES:
                    print(f"[{i}] {tire}")
                    i += 1
                selection_tires = input("Which Tires do you want to choose?\n")
                try:
                    current_car.tire = TIRES[int(selection_tires)]
                    break
                except ValueError:
                    print("Only numbers, try again.")
                except IndexError:
                    print("That wasn't a choice, try again.")
        elif part_select == "m":
            while True:
                i = 0
                for motor in MOTORS:
                    print(f"[{i}] {motor}")
                    i += 1
                selection_motor = input("Which Motor do you want to choose?\n")
                try:
                    current_car.motor = MOTORS[int(selection_motor)]
                    break
                except ValueError:
                    print("Only numbers, try again.")
                except IndexError:
                    print("That wasn't a choice, try again.")
        elif part_select == "s":
            while True:
                i = 0
                for spoiler in SPOILERS:
                    print(f"[{i}] {spoiler}")
                    i += 1
                selection_spoiler = input("Which Spoiler do you want to choose?\n")
                try:
                    current_car.spoiler = SPOILERS[int(selection_spoiler)]
                    break
                except ValueError:
                    print("Only numbers, try again.")
                except IndexError:
                    print("That wasn't a choice, try again.")
    elif player_choice == "s":
        while True:
            i = 0
            for car in CARS:
                print(f"[{i}] {car}")
                i += 1
            selection_car = input("Which car would you like to start with?\n>>>")
            try:
                current_car = CARS[int(selection_car)]
                break
            except ValueError:
                print("Only numbers, try again.")
            except IndexError:
                print("That wasn't a choice, try again.")
    elif player_choice == "exit":
        exit()

    elif player_choice == "p":
        opponent_car = random.choice(CARS)
        opponent_car.nitro = random.choice(NITROS)
        opponent_car.motor = random.choice(MOTORS)
        opponent_car.tire = random.choice(TIRES)
        opponent_car.spoiler = random.choice(SPOILERS)
        print(
            f"The opponents car has been selected, here it is:"
            f"The {opponent_car.model} by {opponent_car.brand} has a speed of {opponent_car.base_speed}, "
            f"an acceleration of {opponent_car.acceleration}, the wind resistance of "
            f"{opponent_car.base_wind_resistance} all while weighing only {opponent_car.weight}kg."
        )
        print(
            f"The parts that it has installed are:\n{opponent_car.nitro}\n{opponent_car.tire}\n{opponent_car.motor}\n{opponent_car.spoiler}\n"
        )
        player_time = speed_calculation(current_car)
        opponent_time = speed_calculation(opponent_car)

        print("...")
        print(
            f"Race Results:\nYour time:{player_time}seconds\nOpponents Time:{opponent_time}\n"
        )
        if player_time < opponent_time:
            print("Congratulations! You won the race!")
        elif player_time > opponent_time:
            print("You lost the race! But don't worry, you can try again!")
        else:
            print("It's a Tie!")