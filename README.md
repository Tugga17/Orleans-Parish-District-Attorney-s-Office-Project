# Orleans-Parish-District-Attorney-s-Office-Project
//Ghostbusters-Themed Dashboard for Server Monitoring
As part of my Summer 2024 internship with the Orleans Parish District Attorney's Office as a Database Admin Intern, I designed and implemented a Python-based dashboard to monitor the status of servers from other organizations during emergencies.

//Project Overview
The primary goal of this project was to develop a proof of concept that showcased the feasibility of a server monitoring system. Once presented, the data-sharing agencies involved could evaluate and sign off on its implementation, as the system would require their approval to be fully operational.

To demonstrate this concept, I tested the system by monitoring two entities:

The DA's Office: Predictably shown as "online" (green) since I was pinging the servers internally.
Orleans Parish Sheriff's Office (OPSO): Expectedly displayed as "offline" (red) due to lack of access to their servers for verification.

//Design and Features
Inspired by my supervisor's suggestion, I adopted the visual aesthetic of the classic Ghostbusters video game for the Commodore 64:

Visual Design: I incorporated iconic elements from the game, including the generic ghost and buildings. Using Adobe tools, I customized the buildings to represent specific organizations by adding their names and altering their color scheme to dynamically change based on server status:
Green: Server online.
Red: Server offline.
Core Functionality: The dashboard pings servers, waits for responses, and updates the organization status in a dictionary where:
Key = Organization name.
Value = Server status (up or down).
Interactive Features: Over the course of the project, I expanded functionality to include:
Player movement.
Randomly spawning ghosts.
Ghostbusting mechanics (ability to "kill" ghosts).
Integration of Ghostbusters theme music.
These additions made the dashboard both functional and engaging, exceeding my supervisor's expectations.

//Impact and Presentation
This project was entirely self-led, from concept to completion. By the end of the summer, I successfully presented the dashboard to the data-sharing agencies, demonstrating its potential as an emergency server-monitoring tool. This proof of concept laid the groundwork for further development, pending agency approval for full implementation.

The combination of technical ingenuity and creative design showcased my ability to independently lead a project and deliver results that balance practicality and innovation.

