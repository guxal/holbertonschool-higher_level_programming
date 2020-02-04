#!/usr/bin/node
function print (value) {
  console.log(value);
}

const argv = process.argv;

if (argv.length >= 3) {
  if (argv[2] > 0) {
    let i;
    let j;
    for (i = 0; i < argv[2]; i++) {
      let c = '';
      for (j = 0; j < argv[2]; j++) { c += 'X'; }
      print(c);
    }
  } else { print('Missing size'); }
} else { print('Missing size'); }
