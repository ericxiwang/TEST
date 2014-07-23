var mongo = require('mongojs'),
    async = require('async');

var db = mongo('10.1.1.33:27017/ymca'),
    events = db.collection('events');

var GAME_TOKEN = '8416e32af87f11e284c212313b0ace15';

console.log('\nRemoving all events for YMC SDK Test in the test database:');
events.remove({'properties.YA0token': GAME_TOKEN}, function(err) {
    if (err) {
        console.error(err.stack, '\n');
        process.exit(1);
    } else {
        console.log('done!\n');
        process.exit(0);
    }
});

