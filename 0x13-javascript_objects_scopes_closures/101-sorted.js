#!/usr/bin/node
const importeddic = require('./101-data').dict;
let myFinalDict = {};
for (const [value, key] of Object.entries(importeddic)) {
  myFinalDict[key] = value;
}
console.log(myFinalDict);

// Write a script that imports a dictionary of occurrences by user id 
// and computes a dictionary of user ids by occurrence.

// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end

// guillaume@ubuntu:~/0x13$ cat 101-data.js
// #!/usr/bin/node
// exports.dict = {
//   89: 1,
//   90: 2,
//   91: 1,
//   92: 3,
//   93: 1,
//   94: 2
// };
// guillaume@ubuntu:~/0x13$ ./101-sorted.js 
// { '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
// guillaume@ubuntu:~/0x13$ 