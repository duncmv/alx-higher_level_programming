#!/usr/bin/node
const request = require('request');

const url = process.argv[2] || '';
const store = {};

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const todos = JSON.parse(body);

  for (let i = 0; i < todos.length; i++) {
    const tmp = todos[i].userId;
    if (todos[i].completed) {
      store[tmp] = (store[tmp] || 0) + 1;
    }
  }

  console.log(store);
});
