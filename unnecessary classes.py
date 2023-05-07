import random
class Human:
    height = 180
    weight = 55

    def sleep(self):
        time = random.randint(1, 12)
        print(f'Slept for {time} hours')

    def walk(self):
        walking_time = random.randint(2, 4)
        walking_distance = random.randint(2, 8)
        speed = walking_distance / walking_time
        print(f'Time taken: {walking_time} hours\n'
              f'Distance walked: {walking_distance} miles\n'
              f'Speed: {speed} miles per hour')

    def calculate_weight_change(self):
        calories_consumed = float(input("Enter calories consumed: "))
        calories_burnt = float(input("Enter calories burnt: "))
        weight_change = (calories_consumed - calories_burnt) / 3500
        self.weight += weight_change
        print(f'Weight change: {weight_change:.2f} kg')

    def track_size(self):
        print("Size tracker")
        class SizeSpecifics:
            length = float(input("Enter specific height: "))
            weight = float(input("Enter specific weight: "))
            shoe_size = float(input("Enter specific shoe size: "))
##