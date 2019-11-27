
const execSync = require('child_process').execSync;
const output = execSync('python3 lagrange.py', { encoding: 'utf-8' });  
console.log('Output was:\n', output);