#!/usr/bin/node
function print (value) {
  console.log(value);
}

const argv = process.argv;

if (argv.length >= 4) {
  print(parseInt(argv[2]) + parseInt(argv[3]));
} else { print('NaN'); }
