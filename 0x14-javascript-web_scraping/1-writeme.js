#!/usr/bin/node
const fs = require('fs');

// write to a new file named 2pac.txt
fs.writeFile(process.argv[2], process.argv[3], (err) => {
  // throws an error, you could also catch it here
  if (err) throw err;
  // success case, the file was saved
  // console.log('Lyric saved!');
});
