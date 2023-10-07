#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (!err) {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach(task => {
      if (task.completed && completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else if (task.completed) {
        completed[task.userId] += 1;
      }
    });
    console.log(completed);
  }
});
