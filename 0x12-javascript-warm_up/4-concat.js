#!/usr/bin/node
function print (value) {
  console.log(value);
}

let idx = 0;
process.argv.forEach((val, index) => {
  idx = index;
});

if (idx === 2) { print(process.argv[idx] + ' is undefined'); } else if (idx < 2) { print('undefined is undefined'); } else { print(process.argv[2] + ' is ' + process.argv[3]); }
