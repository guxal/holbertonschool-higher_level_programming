#!/usr/bin/node
var fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, contents) {
  if (err == null) {
    console.log(contents);
  } else {
    console.log(err);
  }
});
