#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (const x of list) newList.unshift(x);
  return newList;
};
