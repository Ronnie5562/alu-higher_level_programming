#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) theFunction();
};
