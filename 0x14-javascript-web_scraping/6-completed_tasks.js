#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (error, response, data) => {
  if (error) {
    console.error(error);
    return;
  }

  const task = {};

  for (const user of data) {
    if (user.completed) {
      if (task[user.userId]) {
        task[user.userId]++;
      } else {
        task[user.userId] = 1;
      }
    }
  }
  console.log(task);
});
