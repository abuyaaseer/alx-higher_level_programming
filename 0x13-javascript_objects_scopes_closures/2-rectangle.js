#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if ((width && height) > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
