import random


class Robogotchi:

    def __init__(self, name):
        self.name = name
        self.data = {'battery': 100, 'overheat': 0, 'skill': 0, 'boredom': 0, 'rust': 0}
        self.old_data = self.data

    # Game of Numbers
    def numbers(self):
        data = {'robot': 0, 'user': 0, 'draw': 0}
        while True:
            self.num = input("\nWhat is your number? \n")
            random_number = random.randint(0, 1000000)
            bot = random.randint(0, 1000000)

            # Check for potential errors
            if self.num == 'exit game':
                print(f"\nYou won: {data['user']},\nThe robot won: {data['robot']},\nDraws: {data['draw']}.")
                break
            elif self.num.replace(" ", "").isalpha():
                print("A string is not a valid input!")
            elif int(self.num) > 1000000:
                print("The number can't be bigger than 1000000")
            elif int(self.num) < 0:
                print("The number can't be negative!")
            else:
                # Perform Calculations to determine winner
                print(f"\nThe robot entered the number {bot}.")
                print(f"The goal number is {random_number}.")
                if abs((random_number - int(self.num))) > abs((random_number - bot)):
                    print("The robot won!")
                    data['robot'] += 1
                elif abs((random_number - int(self.num))) < abs((random_number - bot)):
                    print("You won!")
                    data['user'] += 1
                elif int(self.num) == bot:
                    print("It's a draw!")
                    data['draw'] += 1

    # Rock Paper Scissors Game
    def rps(self):
        data = {'robot': 0, 'user': 0, 'draw': 0}
        self.result = {"win": {"rock": "scissors", "scissors": "paper", "paper": "rock"},
                       "lose": {"scissors": "rock", "paper": "scissors", "rock": "paper"}}
        while True:
            self.user = input("\nWhat is your move?\n")
            computer = random.choice(['rock', 'paper', 'scissors'])
            print(f"The robot chose {computer}")

            if self.user == "exit game":
                print(f"\nYou won: {data['user']},\nThe robot won: {data['robot']},\nDraws: {data['draw']}.")
                break
            elif self.user not in ['rock', 'paper', 'scissors']:
                print("No such option! Try again!")
            elif computer == self.user:
                print("It's a draw!")
                data['draw'] += 1
            elif self.result["win"][self.user] == computer:
                print(f"You won!")
                data['user'] += 1
            elif self.result["win"][computer] == self.user:
                print("The robot won!")
                data['robot'] += 1

    def info(self):
        print(f"\n{self.name}'s stats are:\nbattery is {self.data['battery']},\noverheat is {self.data['overheat']},\n"
              f"skill level is {self.data['skill']},\nboredom is {self.data['boredom']},\nrust is {self.data['rust']}.")

    def play(self, arg):
        if arg == 'numbers':
            self.numbers()
        elif arg == 'rock-paper-scissors':
            self.rps()
        self.stats_updater(battery=0, overheat=10, skill=0, boredom=-20)
        print(f"{self.name}'s level of boredom was {self.old_data['boredom']}. Now it is {self.data['boredom']}.")
        print(f"{self.name}'s level of overheat was {self.old_data['overheat']}. Now it is {self.data['overheat']}.")
        if self.data['boredom'] == 0:
            print(f"{self.name} is in a great mood!")
        # Occur a bad event
        self.bad_event()

    def recharge(self):
        if self.data['battery'] == 100:
            print(f"{self.name} is charged!")
        else:
            self.stats_updater(battery=+10, overheat=-5, skill=0, boredom=+5)
            print(
                f"{self.name}'s level of overheat was {self.old_data['overheat']}. Now it is {self.data['overheat']}.")
            print(
                f"{self.name}'s level of the battery was {self.old_data['battery']}. Now it is {self.data['battery']}.")
            print(
                f"{self.name}'s level of boredom was {self.old_data['boredom']}. Now it is {self.data['boredom']}.")
            print(f"\n{self.name} is recharged!")

    def sleep(self):
        if self.data['overheat'] == 0:
            print(f"{self.name} is cool!")
        else:
            self.stats_updater(battery=0, overheat=-20, skill=0, boredom=0)
            print(f"\n{self.name} cooled off!")
            print(
                f"{self.name}'s level of overheat was {self.old_data['overheat']}. Now it is {self.data['overheat']}.")

    def learn(self):
        if self.data['skill'] == 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            self.stats_updater(battery=-10, overheat=+10, skill=+10, boredom=+5)
            print(f"""\n{self.name}'s level of skill was {self.old_data['skill']}. Now it is {self.data['skill']}.
{self.name}'s level of overheat was {self.old_data['overheat']}. Now it is {self.data['overheat']}.
{self.name}'s level of the battery was {self.old_data['battery']}. Now it is {self.data['battery']}.
{self.name}'s level of boredom was {self.old_data['boredom']}. Now it is {self.data['boredom']}.
\n{self.name} has become smarter!""")

    def work(self):
        if self.data['skill'] < 50:
            print(f"\n{self.name} has got to learn before working!")
        else:
            self.stats_updater(battery=-10, overheat=+10, skill=0, boredom=+10)
            print(f"{self.name} did well!")
            print(f"""{self.name}'s level of boredom was {self.old_data['boredom']}. Now it is {self.data['boredom']}.
{self.name}'s level of overheat was {self.old_data['overheat']}. Now it is {self.data['overheat']}.
{self.name}'s level of the battery was {self.old_data['battery']}. Now it is {self.data['battery']}.""")
            # Occur a random bad_event
            self.bad_event()

    def oil(self):
        if self.data['rust'] == 0:
            print(f"\n{self.name} is fine, no need to oil!.")
        else:
            self.stats_updater(rust=-20)
            print(f"{self.name}'s level of rust was {self.old_data['rust']}. Now it is {self.data['rust']}."
                  f"{self.name} is less rusty!")

    def bad_event(self):
        events = ['sprinkler', 'puddle', 'pool', 'lucky']
        random_event = random.choices(events, weights=(25, 25, 25, 25))
        bad_event = ''.join([str(i) for i in random_event])

        if bad_event == 'sprinkler':
            self.stats_updater(rust=+30)
            print(f"\nOh, {self.name} encountered a sprinkler!")
            print(f"{self.name}'s level of rust was {self.old_data['rust']}. Now it is {self.data['rust']}")
        elif bad_event == 'pool':
            self.stats_updater(rust=+50)
            print(f"\nGuess what! {self.name} fell into the pool!")
            print(f"{self.name}'s level of rust was {self.old_data['rust']}. Now it is {self.data['rust']}")
        elif bad_event == 'puddle':
            self.stats_updater(rust=+10)
            print(f"\nOh no, {self.name} stepped into a puddle!")
            print(f"{self.name}'s level of rust was {self.old_data['rust']}. Now it is {self.data['rust']}")
        else:
            pass

    # Update statistics of robot depending on the chosen interaction
    def stats_updater(self, battery=0, overheat=0, skill=0, boredom=0, rust=0):

        self.old_data = self.data.copy()
        self.data['boredom'] += boredom
        self.data['overheat'] += overheat
        self.data['skill'] += skill
        self.data['battery'] += battery
        self.data['rust'] += rust

        # Limit the stats at 0
        for key in self.data:
            if self.data[key] < 0:
                self.data[key] = 0

    def interaction(self):

        # Yeah, you messed up!
        if self.data['overheat'] >= 100:
            print(f"The level of overheat reached 100, {self.name} has blown up! Game over. Try again?")
            exit()
        if self.data['rust'] >= 100:
            print(f"{self.name} is too rusty! Game over. Try again?")
            exit()

        print(
            "exit - Exit\ninfo - Check the vitals\nrecharge - Recharge\nsleep - Sleep mode\nplay - Play\nlearn - Learn Skills"
            "\nwork - Work\noil - Oil")
        choice = input("\nChoose:\n")

        if self.data['battery'] == 0 and choice != 'recharge':
            print(f"The level of the battery is 0, {self.name} needs recharging!")
        elif self.data['boredom'] == 100 and choice != 'play':
            print(f"{self.name} is too bored! {self.name} needs to have fun!")
        else:
            if choice == "play":
                game = input("Which game would you like to play?\n")
                if game == "numbers" or game == "rock-paper-scissors":
                    self.play(game)
                else:
                    print("Please choose a valid option: numbers or rock-paper-scissors?")
                    game = input("Which game would you like to play?\n")
                    self.play(game)

            elif choice == "info":
                self.info()
            elif choice == "recharge":
                self.recharge()
            elif choice == "sleep":
                self.sleep()
            elif choice == "learn":
                self.learn()
            elif choice == "work":
                self.work()
            elif choice == "oil":
                self.oil()
            elif choice == "exit":
                print("Game over.")
                exit()
            else:
                print("Invalid input, try again!")
            if self.data['overheat'] == 0:
                print(f"{self.name} is cool")


name_robot = input("How will you call your robot?\n")
robot = Robogotchi(name_robot)

while True:
    print(f"\nAvailable interactions with {robot.name}: ")
    robot.interaction()
