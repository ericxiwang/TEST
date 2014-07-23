var mongo = require('mongojs'),
    async = require('async');

var db = mongo('10.1.1.33:27017/ymca'),
    events = db.collection('events');

var GAME_TOKEN = '8416e32af87f11e284c212313b0ace15';

console.log('\nAdding country codes to all events for YMC SDK Test in the test database:');
events.find({'properties.YA0token': GAME_TOKEN}, function(err, allEvents) {
    handleError(err);

    async.eachSeries(allEvents, addCountryCodeToEvent, finish);
});

function addCountryCodeToEvent(event, next) {
    if (!event.properties.distinct_id) return next();
    var codeAndDid = event.properties.distinct_id.split('-'),
        countryCode = codeAndDid[0],
        distinct_id = codeAndDid[1];

    events.update(
        { _id: new mongo.ObjectId(event._id) },
        { $set: { 'properties.country': countryCode, 'properties.distinct_id': distinct_id } },
        next);
}

function handleError(err) {
    if (err) {
        console.error(err.stack, '\n');
        process.exit(1);
    }
}

function finish(err) {
    handleError(err);
    console.log('done!\n');
    process.exit(0);
}

