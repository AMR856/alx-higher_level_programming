#!/usr/bin/node
const inheritedSquare = require('./5-square');

class Square extends inheritedSquare {
  charPrint (c) {
    let myChar = '';
    if (typeof c === 'undefined') {
      myChar = 'X';
    } else {
      myChar = c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(myChar.repeat(this.width));
    }
  }
}
module.exports = Square;
