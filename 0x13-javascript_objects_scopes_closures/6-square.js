#!/usr/bin/node
const ParentSquare = require('./5-square');
class Square extends ParentSquare {
  charPrint (c = 'X') {
    let text = '';
    for (let i = 0; i < this.width; i++) text = text + c;
    for (let i = 0; i < this.height; i++) console.log(text);
  }
}
module.exports = Square;
