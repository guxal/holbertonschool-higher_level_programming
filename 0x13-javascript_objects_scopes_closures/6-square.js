#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
