#!/usr/bin/node
function uniq (a) {
  return a.sort(function (a, b) { return a - b; }).filter(function (item, pos, ary) {
    return !pos || item !== ary[pos - 1];
  });
}

let argv = process.argv;

argv.shift();
argv.shift();

argv = argv.map((x) => { return parseInt(x); });

if (argv.length > 1) {
  const result = uniq(argv).reverse();
  if (result[1]) { console.log(result[1]); } else { console.log(result[0]); }
} else { console.log(0); }
