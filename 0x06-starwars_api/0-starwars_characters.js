#!/usr/bin/node

// Imports the request module for making HTTP requests
const request = require('request');

// Recursively requests and prints character names from an array of URLs
const fetchCharacterNames = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    fetchCharacterNames(characters, index + 1);
  });
};

// Fetches character URLs from the Star Wars API for a given movie ID
request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    fetchCharacterNames(characters, 0);
  }
);
