#!/usr/bin/node
const fs = require('fs');

const [, , arg] = process.argv;

fs.readFile(arg, 'utf8', (err, data) => {
  if (err) console.log(err);

  console.log(data);
});
