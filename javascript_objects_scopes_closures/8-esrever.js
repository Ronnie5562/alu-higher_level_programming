#!/usr/bin/node

exports.esrever = function (list) {
  let newList = [];
  for (const x of list) newList.unshift(x);
  return newList;
};
