#!/usr/bin/node

if (process.argv.length <= 3) console.log('0');
else {
  let biggest = parseInt(process.argv[2]);
  let secBiggest = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      secBiggest = biggest;
      biggest = parseInt(process.argv[i]);
    }
  }
  console.log(secBiggest);
}
