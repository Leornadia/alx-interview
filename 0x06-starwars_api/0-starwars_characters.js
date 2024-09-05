#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Define the API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to make a GET request and return a promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Main function to fetch and print character names
async function printCharacterNames() {
  try {
    // Fetch movie data
    const movieData = await makeRequest(apiUrl);
    
    // Fetch character data for each character URL
    const characterPromises = movieData.characters.map(characterUrl => makeRequest(characterUrl));
    const characters = await Promise.all(characterPromises);
    
    // Print character names
    characters.forEach(character => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run the main function
printCharacterNames();
