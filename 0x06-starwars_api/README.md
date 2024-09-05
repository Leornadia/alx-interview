# Star Wars Characters API Project

## Description
This project is part of the ALX Higher Level Programming curriculum. It involves creating a Node.js script that interacts with the Star Wars API to fetch and display character names from a specific movie.

## Project Requirements
- Environment: Ubuntu 20.04 LTS
- Node Version: 10.14.x
- Allowed editors: vi, vim, emacs
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be semistandard compliant
- All files must be executable
- Not allowed to use `var`

## Installation

### 1. Install Node.js 10.x
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 2. Install semistandard
```bash
sudo npm install semistandard --global
```

### 3. Install request module
```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Usage
To run the script, use the following command:

```bash
./0-starwars_characters.js <movie_id>
```

Replace `<movie_id>` with the ID of the Star Wars movie you want to get characters from.

Example:
```bash
./0-starwars_characters.js 3
```

This will display the names of all characters appearing in Star Wars Episode III.

## Files
- `0-starwars_characters.js`: Main script to fetch and display Star Wars characters

## Features
- Fetches movie data from the Star Wars API
- Retrieves character information for each character in the movie
- Displays character names in the order they appear in the movie's character list
- Handles errors gracefully

## Author
[Your Name]

## Acknowledgments
- ALX Software Engineering Program
- Star Wars API (SWAPI)
