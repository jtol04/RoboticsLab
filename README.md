# RoboticsLab

Here's a professional and engaging `README.md` file for your personal GitHub account that documents your code:

---

# ROS Joystick Teleoperation for Robots

This repository contains a ROS (Robot Operating System) node designed to convert joystick inputs into motion commands for robots. Originally developed for turtlesim by Andrew Dai, this code was adapted and enhanced by **Amir Hossain** and **Jary Tolentino** at the **Fordham Robotics Lab** for use with the **Logitech ATK3 Joystick**.

---

## Features

- **Joystick Control**: Translates joystick inputs (`/joy` topic) into velocity commands for robots.
- **Customizable Robot Selection**: Pair with a robot of your choice at runtime.
- **Logitech ATK3 Joystick Support**: Special modifications for compatibility with the Logitech ATK3 joystick.
- **Graceful Shutdown**: Ensures safe termination of robot motion when the node shuts down.

---

## How It Works

1. **Joystick Input**: The node subscribes to the `/joy` topic, receiving joystick data.
2. **Command Conversion**: The joystick data is processed into `Twist` messages for controlling robot motion.
   - **Linear Speed**: Controlled by the vertical axis of the left joystick (axis 1).
   - **Angular Speed**: Controlled by the horizontal axis of the left joystick (axis 0).
3. **Safe Shutdown**: Publishes zero-motion commands to halt the robot safely during shutdown.

---

## Code Highlights

### Key Functions

- **`joyCallback(data)`**: Processes joystick inputs and publishes `Twist` messages based on button states and axis values.
- **`callback_shutdown()`**: Handles the shutdown process by stopping robot motion.
- **`start()`**: Initializes publishers and subscribers, and starts the ROS spin loop.

---

## Setup and Usage

### Prerequisites
- ROS (Robot Operating System) installed and properly configured.
- Logitech ATK3 joystick connected to your system.
- Ensure the robot you want to control supports `/RosAria/cmd_vel` topic for velocity commands.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ros-joystick-teleop.git
   cd ros-joystick-teleop
   ```
2. Launch the node:
   ```bash
   python3 joystick_teleop.py
   ```
3. Enter the robot name when prompted:
   ```bash
   Which robot would you like to pair with?: robot_name
   ```

---

## Dependencies

- Python 3
- ROS (Robot Operating System)
- `geometry_msgs` for `Twist` messages
- `sensor_msgs` for `Joy` messages

---

## Contribution

Feel free to fork this repository, submit issues, or create pull requests if you'd like to improve this project.

---

## Acknowledgments

- Original code by **Andrew Dai**
- Modified by **Amir Hossain** and **Jary Tolentino**
- Developed at **Fordham Robotics Lab**

---

## License

This project is licensed under the [MIT License](LICENSE).

---

This `README.md` is structured to provide a clear overview, highlight features, and ensure anyone can understand and run the project. Let me know if you'd like any edits!
