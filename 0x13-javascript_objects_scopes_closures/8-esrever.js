#!/usr/bin/node
exports.esrever = function (list) {
  let k = list.length - 1;
  for (let i = 0; i < list.length / 2; i++) {
    const temp = list[i];
    list[i] = list[k];
    list[k] = temp;
    k--;
  }
  return list;
};
