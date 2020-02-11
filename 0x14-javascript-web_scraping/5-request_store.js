#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    // write to a new file named 2pac.txt
    fs.writeFile(process.argv[3], body, (err) => {
      // throws an error, you could also catch it here
      if (err) throw err;
      // success case, the file was saved
      // console.log('Lyric saved!');
    });
  }
});
