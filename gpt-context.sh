#!/bin/bash
# Check if it's a poetry project

if [ -f pyproject.toml ]
then
 echo "Running poetry project commands..."
 echo -e "Project tree: \n$(tree -L 2 ./src)" > temp.txt
 echo -e "\nPackages: \n$(cat pyproject.toml)" >> temp.txt
 pbcopy < temp.txt
 rm temp.txt
 echo "Copied to clipboard, now you can paste this in ChatGPT!"
# Check if it's a nodejs project
elif [ -f package.json ]
then
 echo "Running nodejs project commands..."
 echo -e "Project tree: \n$(tree -L 2 ./src)" > temp.txt
 echo -e "\nPackages: \n$(cat package.json)" >> temp.txt
 pbcopy < temp.txt
 rm temp.txt
 echo "Copied to clipboard, now you can paste this in ChatGPT!"
else
 echo "Neither poetry nor nodejs project found."
fi
