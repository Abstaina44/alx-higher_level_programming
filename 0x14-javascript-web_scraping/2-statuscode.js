#!/usr/local/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then((response) => {
    console.log(`code: ${response.status}`);
  })
  .catch((error) => {
    console.log(error.message);
  });
