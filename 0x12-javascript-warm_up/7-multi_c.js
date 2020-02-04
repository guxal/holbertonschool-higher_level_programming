#!/usr/bin/node
function print (value) {
  console.log(value);
}

let idx = 0;
process.argv.forEach((val, index) => {
  idx = index;
});

const argv = process.argv;

if (idx >= 2) {
  if (argv[2] > 0) {
    let i;
    for (i = 0; i < argv[2]; i++) { print('C is fun'); }
  }
} else { print('Missing number of occurrences'); }
