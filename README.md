# README Generator
I wrote this README.md generator to make writing READMEs for ALX school projects easier - keeping me from procrastinating. 

## Prerequisite
- Python3 must be installed on your machine.

## Features
- Sorts tasks in ascending order automatically.

## Installation
Fork or clone this repo to your any directory on your machine. For Linux, I recommend the root directory.

## Usage
Once you have the `README_Generator` directory on your computer:
1. `cd` to the directory
2. Open the `rdm` file, Not `rdm.py`, and fill in the relative path to the directory.
3. Copy the `rdm` file to your working directory.

From your working directory:
- Run `./rdm` to see all commands you can use to making the README.md file.
- Run `./rdm create` to create a new README.md file
- Run `./rdm task` to add a new task to the README.md file.

Note: When you open the README.md file, after using this program to create it, you'll find lots of comments - Do Not modify those. The program relies on those comments to create the README.md file. When you push the README.md file to GitHub it would appear without those comments.
## Examples
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```
