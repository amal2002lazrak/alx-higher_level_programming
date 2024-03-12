#!/usr/bin/node

exports.converter = function (base) {
  return function convertedNumber (number) {
    return number.toString(base);
  };
};
