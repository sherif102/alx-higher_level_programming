var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
}); 
fs.open(file1, 'r', (err, filea) => {
  if (err) throw (err);
  fs.readFile(filea, (err, data) => {
    if (err) throw (err);
    fs.appendFile(file3, data, () => console.log('Done'));
  });
});
fs.open(file2, 'r+', (err, filea) => {
  if (err) throw (err);
  fs.readFile(filea, (err, data) => {
    if (err) throw (err);
    fs.appendFile(file3, data, () => console.log('Done'));
  });
});
