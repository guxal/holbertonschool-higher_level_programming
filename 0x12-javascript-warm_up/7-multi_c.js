#!/usr/bin/node
function print (value) {
  console.log(value);
}

const argv = process.argv;

if (argv.length >= 3) {
  if (argv[2] > 0) {
    let i;
    for (i = 0; i < argv[2]; i++) { print('C is fun'); }
  }
} else { print('Missing number of occurrences'); }
