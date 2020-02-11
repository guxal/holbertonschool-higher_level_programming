#!/usr/bin/node
const data = require('./100-data').list;

const map1 = data.map((x, idx) => x * idx);
console.log(data);
console.log(map1);
