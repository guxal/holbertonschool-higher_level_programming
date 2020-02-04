#!/usr/bin/node
function print (value) {
  console.log(value);
}

let idx = 0;
process.argv.forEach((val, index) => {
  idx = index;
});

if (idx < 2) {
  print('Not a number');
} else {
  const number = parseInt(process.argv[2]);
  if (number) {
    print('My number ' + number);
  } else { print('Not a number'); }
}
