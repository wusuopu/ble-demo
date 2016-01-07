var bleno = require('bleno');
var BlenoPrimaryService = bleno.PrimaryService;

var EchoCharacteristic = require('./characteristic');

console.log('smart lock');

bleno.on('stateChange', function(state) {
  console.log('on -> stateChange: ' + state);

  if (state === 'poweredOn') {
    // FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFF0
    bleno.startAdvertising('Lock Device', ['fffffffffffffffffffffffffffffff0']);
  } else {
    bleno.stopAdvertising();
  }
});

bleno.on('advertisingStart', function(error) {
  console.log('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));

  if (!error) {
    bleno.setServices([
      new BlenoPrimaryService({
        // FFFFFFFF-FFFF-4FFF-8FFF-FFFFFFFFFFF1
        uuid: 'FFFFFFFFFFFF4FFF8FFFFFFFFFFFFFF1',
        characteristics: [
          new EchoCharacteristic()
        ]
      })
    ]);
  }
});
