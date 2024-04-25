#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

const request = require('request');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
