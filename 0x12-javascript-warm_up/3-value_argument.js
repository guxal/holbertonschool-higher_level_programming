#!/usr/bin/node
function print (value) {
  console.log(value);
}

let idx = 0;
process.argv.forEach((val, index) => {
  idx = index;
});

if (idx === 2) { print(process.argv[idx]); } else if (idx < 2) { print('No argument'); } else { print(process.argv[2]); }
