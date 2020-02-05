#!/usr/bin/node

exports.callMeMoby = function (size, callback) {
  for (let i = 0; i < size; i++) { callback(); }
};
