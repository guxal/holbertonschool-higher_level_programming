#!/usr/bin/node

exports.converter = function (base) {
  const number = base;

  return function (base) {
    return parseInt(number, base);
  };
};
