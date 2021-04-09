

# MLH-Ethical-Data
Creating a simple port scanner to check the open ports in your system, close them along with options to view random cool facts related to them by a simple flag.

# Reason Behind Creating MLH-Ethical-Data?
Cyber security has been one of attractive field for many people who wish to jump into something exciting. We believe this project will feed the brains of beginners with even more excitement through an easy to navigate CLI (giving haccerman vibes), features to directly interact with your system, along with options to know random facts, list the uses of common ports etc.

In essence, we aim to build a cool tool to be used as a source of common info while giving options to directly interact with your machine.


This tool is good for beginners in cyber security who just want to see what all processes run on different ports and experiment with them. We have also implemented required precautions to prevent accidental closing of an essential system process through an aesthetically pleasing CLI

# What Can MLH-Ethical-Data Do?
- **Help:** Use the help command to get a list of available flags and features you can tinker with

![unknown (3)](https://user-images.githubusercontent.com/39042025/114225289-627ffe00-992f-11eb-9954-aab5823995b8.png)

- **Check open ports:** Allowing the user to check what ports they have open for user processes. We aim to add a flag to view system processes too.

![unknown](https://user-images.githubusercontent.com/39042025/114224962-0026fd80-992f-11eb-87f6-483f8066b569.png)

- **Close ports:** Allowing the users to close ports fore different applications. For security concerns, it will not allow closing of ports running system processes.

![unknown (2)](https://user-images.githubusercontent.com/39042025/114225442-8b07f800-992f-11eb-8a1e-f7c022217314.png)
![unknown (1)](https://user-images.githubusercontent.com/39042025/114225566-b68ae280-992f-11eb-9269-699229a30005.png)

- **Random facts:** What else would be a better idea to increase engagement than a random fact? Get a random fact about security concerns by using a simple flag `-f`

- **List common ports:** It can be used as a go to tool for getting common info like what port is used for what stuff etc.

# How can MLH-Ethical-Data be used?
You just need to navigate to the directory 
```
cd MLH-Ethical-Data
```
and run the following:
```
sudo python3 main.py
```

*P.S. You will need to have `sudo` to allow the close ports command to function*

# Tools used
- Our CLI is based in **Python3** using only the packages like **psutil**, **socket** etc. to interact with the user's system

# Collaborators 
- Jack
- Kshitijaa
- Samuel

