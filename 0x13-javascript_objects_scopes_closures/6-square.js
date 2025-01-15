#!/usr/bin/node
const Squar = require('./5-square');
class Square extends Squar {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    let text = '';
    for (let i = 0; i < this.width; i++) text = text + c;
    for (let i = 0; i < this.height; i++) console.log(text);
  }
}
module.exports = Square;
