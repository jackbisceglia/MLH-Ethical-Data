# Ethical Data: Port Scanner
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)

A simple magical light-weight port scanner to be used by developers and non-developers alike

## Reason Behind Creating MLH-Ethical-Data?
Cyber security has been one of attractive field for many people who wish to jump into something exciting. We believe this project will feed the brains of beginners with even more excitement through an easy to navigate CLI (giving haccerman vibes), features to directly interact with your system, along with options to know random facts, list the uses of common ports etc.

In essence, we aim to build a cool tool to be used as a source of common info while giving options to directly interact with your machine.


This tool is good for beginners in cyber security who just want to see what all processes run on different ports and experiment with them. We have also implemented required precautions to prevent accidental closing of an essential system process through an aesthetically pleasing CLI

## Useful commands
- **Help `mlh -h`:** Use the help command to get a list of available flags and features you can tinker with

- **Check open ports `mlh -o`:** Allowing the user to check what ports they have open for user processes. We aim to add a flag to view system processes too.

- **Close ports `mlh -c <port number>`:** Allowing the users to close ports fore different applications. For security concerns, it will not allow closing of ports running system processes.

- **List common ports `mlh -l`:** It can be used as a go to tool for getting common info like what port is used for what stuff etc.

- **Random facts `mlh -f`:** What else would be a better idea to increase engagement than a random fact? Get a random fact about security concerns by using a simple flag `-f`


## How to run?
You just need to navigate to the directory 
```
cd MLH-Ethical-Data
```
install the required packages
```
pip3 install -r requirements.txt
```

and run the following:
```
sudo python3 main.py
```
*P.S. You will need to have `sudo` to allow the close ports command to function*

## :crystal_ball: Some magic
The tool also allows you to use previous three commands through history. To use, simply do the following:
- Press enter without any command
- Get the list of last three commands
- Simply press 1/2/3 according to the command you want to run and execute it woohoo!


## Tools used
- Our CLI is based in **Python3** using only the packages like **psutil**, **socket** etc. to interact with the user's system

## Collaborators 
- Jack
- Kshitijaa
- Samuel

