var request = require('request'),
    _       = require('underscore'),
    moment  = require('moment');

var config  = require('../test-config')

var YMC_GAME_ID             = config.ymc_id,
    TRACKING_HOST           = config.rcvr_1_host,
    TRACKING_URL            = "http://" + TRACKING_HOST + "/ts_postback";

// TODO figure out the relevant parts and parameterize
var BARE_POSTBACK_EVENT = {
     hit_id: '',
     hit_created: '',
     hit_tags: '',
     hit_tracker_id: '',
     hit_tracker_slug: '',
     evt_wifi_mac: '',
     evt_ios_idfa: '8C5B8443-CD63-4CDA-806C-189343D1C8A1',
     evt_ios_secure_udid: '',
     evt_android_id: '',
     evt_android_device_id: '',
     evt_id: '8572494697304288797',
     evt_tracker_id: '',
     evt_tracker_slug: 'ya0birth',
     evt_timestamp: '1401485822',
     evt_ip: '198.53.191.234',
     evt_custom_parameters_uuid: '"92655955dba145a46b423c5d05115c5b"',
     evt_custom_parameters_ymc_id: '"4b5b5c2e208811e3b5a722000a97015e"',
     hit_destination_url: '',
     hit_referrer: '',
}

module.exports.sendTsPostback = sendTsPostback;
module.exports.sendTsPostbackWithProperties = sendTsPostbackWithProperties;

function sendTsPostbackWithProperties(props, done) {
    var data = _.defaults(props, BARE_POSTBACK_EVENT)
    sendEvent(data, done)
}

function sendTsPostback(done) {
    var noPropertiesSpecified = {}
    sendTsPostbackWithProperties(noPropertiesSpecified, done)
}

function sendEvent(data, done) {
    var opts = {
        method: 'GET',
        url: TRACKING_URL,
        json: data,
    }
    request(opts, done)
}
