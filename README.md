# Autonomous Shooting Drone
## More information, setup and configuration :
All usefull information are here : [Autonomous Shooting Drone WIKI](https://github.com/mariusweiler/Autonomous-Shooting-Drone/wiki)

## Introduction
Configure an autonomous shooting drone, using a DJI Phantom 2 drone, 2 raspberries 3 with 3 grovepis, multiple sensor from the grovepi kit, a gyroscope and a camera.

### Goals
The Autonomous Shooting Drone purpose is to controll a DJI phantom2 drone with 2 Raspberries Pi 3, to make it takeoff, then stabilise it at 1.5 meter, then look for a person as a target, center the target and shoot with a BB gun. The Raspi is interfaced to the drone via the remote controller, which we replace the potentiometers by the raspberry's outputs.

There is 2 devices managing the flight :
- A Raspberry with a grovepi, a camera, a ultrasonic range sensor, a relay, a gyroscope and a battery to power the Raspi. All of this is on the Drone and communicates with the other device to send the height and the position of the person.
- A Raspberry with 2 grovepies, the remote board with batteries, a LCD display, a LED, a button. All of this is placed on a box, and operates as mission controll to send commands to the drone to make it fly.

### Why GitHub
Throughout the project we have stumbled upon documentation from various websites, which helped us going forward. Anyway, we did not found any project to fly a DJI drone with a Raspberry directly. With this GitHub documentation, we want to give back information, and maybe help other projects with our humble contribution.
