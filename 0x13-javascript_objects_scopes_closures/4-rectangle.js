#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if ((width && height) > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.heigth] = [this.heigth, this.width];
  }

  double () {
    [this.width, this.heigth] = [this.width * 2, this.height * 2];
  }
};
