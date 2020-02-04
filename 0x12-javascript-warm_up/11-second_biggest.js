#!/usr/bin/node
function uniq (a) {
  return a.sort().filter(function (item, pos, ary) {
    return !pos || item !== ary[pos - 1];
  });
}

let argv = process.argv;

argv.shift();
argv.shift();

argv = argv.map((x) => { return parseInt(x); });

if (argv.length > 1) { console.log(uniq(argv).reverse()[1]); } else { console.log(0); }
