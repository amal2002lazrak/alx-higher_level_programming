#!/usr/bin/node

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];

  a = parseInt(a);
  b = parseInt(b);

  if (isNaN(a) | isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = a + b;
    console.log(sum);
  }
}
add();
