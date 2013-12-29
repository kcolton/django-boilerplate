App.views.Home = function($container) {
  var self = this,
    dom = {};

  dom.$container = $container;

  $container.find('.get-params').on('click', function() {
    debug.log('page change get w/ params');
    app.page.get('/info/', {'foo': 'bar'});
  });

  $container.find('.get-no-params').on('click', function() {
    debug.log('page change get no params');
    app.page.get('/info/');
  });

  $container.find('.post-data').on('click', function() {
    debug.log('page change post w/ data');
    app.page.post('/info/', {'coffee': 'good'});
  });

  $container.find('.post-no-data').on('click', function() {
    debug.log('page change post w/ no data');
    app.page.post('/info/');
  });
};