#!/usr/bin/node
// Prints all characters of a Star Wars movie (by movie ID)

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(filmUrl, (err, res, body) => {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, body) => {
      if (!err) {
        const name = JSON.parse(body).name;
        console.log(name);
        printCharacter(index + 1);
      }
    });
  };

  printCharacter(0);
});
