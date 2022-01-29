# ServerChecker

A simple linux server controller made in Python.

## Why there isn't any python programs?

I have the program on a computer witch right now isn't working well. I'll have to recover the program when I can.

## How does it work? 

The ServerChecker uses a Python module called paramiko, witch lets the comuter access a server via ssh. The data of the server is got via a text file. The password is asked on the spot.

## Installation

First, you will need to install Python (If you haven't already):


To use it, you will need some modules:

```
pip3 install paramiko
```

Then, you will need to download the package:

```
git clone https://github.com/EMC-prog/ServerChecker.git
```

## First steps

When you start the program, it will tell you that you haven't entered the program yet. You have to make some modifications in order to work well.

The fist thing you will have to put is the server ip and port for connecting to ssh. Then put the username that you will want to connect with. The password will be asked on the spot to avoid people for being able to get your password with the info file.

```
{
	"ip":"100.10.01.10", 
	"port":"22", 
        "user":"", 
        "custom_command":""
}
```



## Usage

To start the system, go to the folder and access it using python3

```
cd ServerChecker
python3 serverchecker.py
```

### Functions

The software comes with some commands already, like:

- Shutdown the system (You can choose between instantly and in a minute)
- Reboot the system
- Custom command

## Custom command feature
You can send a custom command into the server via ServerChecker. You can send it from the info.txt file, in the section "custom_command".

## Changelog
You can find it [here](CHANGELOG.md).



## License

This program is under the MIT license.
