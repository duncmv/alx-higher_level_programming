#!/usr/bin/node

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let j = 0; j < this.width; j++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
