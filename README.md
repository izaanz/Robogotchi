# Robogotchi: Virtual Robot Pet Simulator

## About

Robogotchi is an interactive, text-based virtual pet simulator implemented in Python. This project showcases the power of Object-Oriented Programming (OOP) to create a dynamic and engaging user experience. Players can interact with their virtual robot pet, managing its various needs and playing games.

## Features

- **Object-Oriented Design**: The entire game is built around the `Robogotchi` class, demonstrating key OOP principles such as encapsulation and abstraction.
- **Dynamic Pet Status**: Manage your robot's battery, temperature, skill level, boredom, and rust.
- **Interactive Games**: Play "Numbers" or "Rock Paper Scissors" with your robot.
- **Various Interactions**: Recharge, sleep, learn, work, and oil your robot to maintain its well-being.
- **Random Events**: Experience unexpected events that can affect your robot's condition.

## OOP Highlights

1. **Class-based Structure**: The `Robogotchi` class encapsulates all robot attributes and behaviors.
2. **Encapsulation**: Robot's state (battery, overheat, etc.) is managed internally within the class.
3. **Method Organization**: Different robot actions are organized into separate methods (e.g., `play()`, `recharge()`, `learn()`).
4. **State Management**: The `stats_updater()` method provides a centralized way to modify the robot's attributes.

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:

  `git clone https://github.com/yourusername/robogotchi.git`

3. Navigate to the project directory:

  `cd robogotchi`

4. Run the script:
  `python robogotchi.py`


## Gameplay

1. Start by naming your robot.
2. Choose from various interactions:
- `exit`: End the game
- `info`: Check robot's vitals
- `recharge`: Recharge the robot's battery
- `sleep`: Put the robot in sleep mode
- `play`: Play games (Numbers or Rock Paper Scissors)
- `learn`: Improve the robot's skills
- `work`: Make the robot work
- `oil`: Oil the robot to prevent rust

## Contributing

Contributions to Robogotchi are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).
