/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
var express = require('express');
app = express();// instruct the app to use the `bodyParser()` middleware for all routes
var http = require('http');
var server = app.listen(8010, function() {
    console.log('Web server listening on localhost: 8010');
});
//var server = http.createServer().listen(4000);
var io = require('socket.io').listen(server);


//Subscribe to the Redis chat channel

//Configure socket.io to store cookie set by Django

io.on('connection', function (socket) {
    //Client is sending message through socket.io
    socket.on('enviar sqlquery', function (message) {
        console.log('Message: ' + message);
    });
    socket.on('enviar proyecto', function (proyecto,parametros) {
        socket.broadcast.emit('recibir proyecto', proyecto,parametros);
    });
    socket.on('enviar propiedades nodo', function (nodo) {
        //se manda a esperar un segundo en lo que el formulario crea el iframe
        setTimeout(function () {
            console.log('he recibido una peticion de enviar: ' + nodo);
            socket.broadcast.emit('enviar propiedades a cliente', nodo);
        }, 1200);
    });
    socket.on('propiedades actualizadas nodo', function (nodo) {
        console.log('he recibido una peticion actualizadas de enviar: ' + nodo);
        socket.broadcast.emit('enviar propiedades actualizadas a cliente', nodo);
    });
    socket.on('cancelar propiedades nodo', function (idnodo) {
        console.log('he recibido una peticion de cancelar propiedades : ' + idnodo);
        socket.broadcast.emit('cancelar iframe', idnodo);
    });
});

console.log("mi servidor" );