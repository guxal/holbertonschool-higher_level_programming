#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c) {
    if (this.width === undefined) {
      return;
    }
    for (let i = 0; i < this.width; i++) {
      if (c !== undefined) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
