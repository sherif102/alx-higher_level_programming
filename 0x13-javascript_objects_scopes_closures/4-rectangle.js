#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let width = '';
    for (let i = 0; i < this.width; i++) width = width + 'X';
    for (let i = 0; i < this.height; i++) console.log(width);
  }

  rotate () {
    const copy = this.width;
    this.width = this.height;
    this.height = copy;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
