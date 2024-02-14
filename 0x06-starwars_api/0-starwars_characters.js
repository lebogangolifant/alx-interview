#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make an HTTP GET request to fetch movie details
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie details.');
    return;
  }

  // Parse movie details from the response body
  const movie = JSON.parse(body);

  // For each character in the movie, fetch and print their details
  movie.characters.forEach(characterUrl => {
    // Make an HTTP GET request to fetch character details
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error('Failed to fetch character details.');
        return;
      }

      // Parse character details from the response body and print the name
      console.log(JSON.parse(body).name);
    });
  });
});
