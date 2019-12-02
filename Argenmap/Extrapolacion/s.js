
const execSync = require('child_process').execSync;
const output = execSync('python3 lagrange.py', { encoding: 'utf-8' });  
console.log('Output was:\n', output);
//node s.js (script de js para correr el algoritmo de lagrange en python)
//poner dentro de una funcion que se ejecute cuando se toque un boton en algun mapa 
//Y ejecute el programa en python