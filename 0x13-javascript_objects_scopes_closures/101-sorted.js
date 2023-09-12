#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (!(occurrence in newDict)) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
}

console.log(newDict);
