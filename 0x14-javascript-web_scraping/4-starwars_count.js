#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body).results;

  let filmsNumber = 0;
  for (const result of data) {
    const filmschars = result.characters;

    for (const film of filmschars) {
      if (film.includes(characterId)) {
        filmsNumber++;
      }
    }
  }
  console.log(filmsNumber);
});
