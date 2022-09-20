const express = require('express');
const webpack = require('webpack');
const webpackDevMiddleware = require('webpack-dev-middleware');
const socketio = require('socket.io');
const io = require('socket.io-client');

const Constants = require('../shared/constants');
//const Game = require('./game');
const webpackConfig = require('../../webpack.dev.js');
//const robots = require('./robotsrouter.js');

const socket = io("ws://localhost:3000");

// Setup an Express server
const app = express();
app.use(express.static('public'));

if (process.env.NODE_ENV === 'development') {
  // Setup Webpack for development
  const compiler = webpack(webpackConfig);
  app.use(webpackDevMiddleware(compiler));
} else {
  // Static serve the dist/ folder in production
  app.use(express.static('dist'));
}

// Listen on port
const port = process.env.PORT || 8765;
const server = app.listen(port);
console.log(`Server listening on port ${port}`);

console.log(`Emmitting test msg`);
socket.emit(Constants.JOIN_ROBOT);
