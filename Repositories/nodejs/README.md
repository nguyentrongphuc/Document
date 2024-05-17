
## 1. What is Node?
Nodejs itself is not a programming language but rather a runtime that allows you to run javascript on a server (you see when javascript first came around in the 1990s) - we saw the inital release of node.js in 2009 now up until this time it was impossible to write javascript code on the server.

What can node do?


## 2. How do you install Node?
nvm install xx.xx.x 
nvm & npm

## 3. Hello World
## 4. Know the Runtime
process.env.user
global that existed in node


## 5. Events
``` nodejs
process.on('exit', function(){
    // callback
} )

const { EventEmitter } = require('events') ;
const eventEmitter = new EventEmitter();
eventEmitter.on('lunch' , () => {
    console.log('yum')
})

eventEmitter.emit('lunch');

```

## 6. File System
``` nodejs
// ---------------------
// sync === blocking
const { readFile, readFileSync } = require('fs');
const txt = readFileSync('./hello.txt', 'utf8');
console.log(txt);

// assync === non-blocking
readFile('./hello.txt', 'utf8', (err, txt) => {
    console.log(txt);
})
console.log('do this ASAP');

// Otherway
const { readFile } = require('fs').promises;

async function hello() {
    const file = await readFile('./hello.txt', 'utf8');
}
```

## 7. Modules
https://nodejs.org/api/modules.html


## 8. Build & Deploy 
npm init -y

```nodejs
const express = require('express');
const app = express();

app.get('/', (request, response) => {
    readFile('./home.html', 'utf8', (err, html) => {
        if (err) {
            response.status(500).send('sorry, out of order');
        }
        response.send(html);
    })
})

app.listien(process.env.PORT || 3000, () => console.log('app available on httml://localhost:3000'))
```