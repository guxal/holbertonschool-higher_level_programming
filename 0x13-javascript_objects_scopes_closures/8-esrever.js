#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  let count = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newlist[count] = list[i];
    count++;
  }
  return newlist;
};
