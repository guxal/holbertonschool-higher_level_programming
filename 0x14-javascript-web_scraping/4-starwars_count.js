#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;

    data.forEach((v, i) => {
      v.characters.forEach((v, i) => {
        if (v.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
