#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);
const printC = (quantity) => {
  for (; quantity > 0; quantity--) console.log('C is fun');
};

Number.isInteger(num) ? printC(num) : console.log('Missing number of occurrences');
