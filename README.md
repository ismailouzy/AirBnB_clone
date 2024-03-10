
# AirBnB Clone Project - README

![App Screenshot](https://camo.githubusercontent.com/0abfd1a3534470d279dd6eaca57e0b4b81e23fb77afd81483d470c2f63ab51d3/68747470733a2f2f692e696d6775722e636f6d2f4d5171334142632e706e67)

The AirBnB Clone project is about creating a fantastic web application. At this moment, we're building the first part - a unique tool known as a command interpreter. This tool helps us manage things like users, places, and more in our AirBnB system. Think of it as the captain steering the ship, guiding and instructing the team towards a successful voyage



# Deployment

## Getting Started
#### Interactive Mode:
Run the console using the following command:
```bash
$ ./console.py
```

#### Non-Interactive Mode:
You can use non-interactive mode by piping commands directly to the console script.

```bash
$ echo "help" | ./console.py
```
## Basic Commands
#### Quit:
To exit the console, type:
```bash
(hbnb) quit
```
#### Display Help:
To get help for a specific command, use:
```bash
(hbnb) help <command>
```
#### Create Object:
Create a new object of a specified class and print its ID:

```bash
(hbnb) create <class>
```
#### Show Object:
Display details of a specific object:
```bash
(hbnb) show <class> <id>
```
#### Destroy Object:
Remove a specific object from the system:
```bash
(hbnb) destroy <class> <id>
```
#### Show All Objects:
Display all objects or instances of a specific class:
```bash
(hbnb) all
```
#### Update Attribute:
Modify an attribute of a specific object:
```bash
(hbnb) update <class> <id> <attribute_name> "<attribute_value>"
```
## Examples

#### Interactive Mode
```bash
$ ./console.py
(hbnb) help
# Displayed help commands
(hbnb) quit
$
```
#### Non-Interactive Mode
```bash
$ echo "help" | ./console.py
# Displayed help commands without entering interactive mode
(hbnb)
$
```



## Authors

- [@ismail Ouzal](https://github.com/ismailouzy)
- [@Brahim El hajji](https://github.com/BrahimElhajji/)


