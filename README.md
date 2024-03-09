
# AirBnB Clone Project - README

![App Screenshot](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240309%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240309T133127Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7452c3cbb5b78b31270d5f00f23ab07f015334eb81190e655cb10d26db1b89ed)

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


