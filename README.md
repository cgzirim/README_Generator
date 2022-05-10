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
3. Copy the `rdm` file to `/usr/bin`.

From your working directory:
- Run `rdm` to see all commands you can use to making the README.md file.
- Run `rdm create` to create a new README.md file
- Run `rdm task` to add a new task to the README.md file.

Note: When you open the README.md file, after using this program to create it, you'll find lots of comments - Do Not modify those. The program relies on those comments to create the README.md file. When you push the README.md file to GitHub it would appear without those comments.
## Examples of use
Confirm the `README_Generator` directory is in the directory you want it to be:
```
root@4332e3357bf5:~# ls
README_Generator  alx-system_engineering-devops
root@4332e3357bf5:~# cd README_Generator/
```
Update path in `rdm` file in the `README_Generator` directory:
```
root@4332e3357bf5:~/README_Generator# cat rdm
#!/bin/bash
...
python3 /[path]/README_Generator/rdm.py $1 $2

root@4332e3357bf5:~/README_Generator# pwd
/root/README_Generator

root@4332e3357bf5:~/README_Generator# vi rdm
root@4332e3357bf5:~/README_Generator# cat rdm
#!/bin/bash
...
python3 /root/README_Generator/rdm.py $1 $2
```
Copy the `rdm` file to `/usr/bin`:
```
root@4332e3357bf5:~/README_Generator# cd
root@4332e3357bf5:~# cp README_Generator/rdm /usr/bin
```
Generate README.md file in any directory with the `rdm create` command:
```
root@4332e3357bf5:~# cd alx-system_engineering-devops/0x00-shell_basics/
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics#
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# rdm create
Project's title: Shell, basics
Insert URL of this repository: https://github.com/iChigozirim/alx-system_engineering-devops/tree/master/0x00-shell_basics
Project's description: In this project, I learned how to navigate directories, how to look around, and how to manipulate file in a Linux terminal.
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics#
```
Add task to the README.md file with the `rdm task` command:
```
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# rdm task
Task's title: 0. Where am I?
file name: 0-current_working_directory
file description: Bash script that prints the absolute pathname of the current working directory.
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics#
```
Add another task:
```
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# rdm task
Task's title: 3. The long format
file name: 3-listfiles
file description: Bash script that displays current directory contents in long format.
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics#
```
Push the README.md file to the project's directory:
```
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# git add README.md
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# git commit -m "Update README.md"
[master 5502830] Update README.md
 1 file changed, 23 insertions(+), 1 deletion(-)
 rewrite 0x00-shell_basics/README.md (100%)
root@4332e3357bf5:~/alx-system_engineering-devops/0x00-shell_basics# git push

```
How the READM.md file looks on GitHub:
![result](https://user-images.githubusercontent.com/88312276/167193436-e05ac1ae-1ea1-44d4-abba-1afe5354fdc7.jpg)
