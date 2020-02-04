#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) { return (1); }
  return (factorial(num - 1) * num);
}

const argv = process.argv;

if (argv.length >= 3) { console.log(factorial(argv[2])); } else { console.log(1); }
