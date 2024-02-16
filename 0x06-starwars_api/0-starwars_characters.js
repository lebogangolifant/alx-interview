#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character details
function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        // Create a new Error object with the reason for rejection
        reject(new Error('Failed to fetch character details.'));
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Make an HTTP GET request to fetch movie details
request(url, async (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie details.');
    return;
  }

  // Parse movie details from the response body
  const movie = JSON.parse(body);

  try {
    // Fetch character details for each character in the movie
    for (const characterUrl of movie.characters) {
      const characterName = await fetchCharacter(characterUrl);
      console.log(characterName);
    }
  } catch (err) {
    // Log the error message from the Error object
    console.error(err.message);
  }
});
