#!/usr/bin/node

const fs = require('fs');
// Import Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file
  // 'utf8' specifies the encoding that the file is being read in

  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});
