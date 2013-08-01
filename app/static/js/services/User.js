App.services.User = function() {
  var self = this,
    own = {};

  own.initialized = false;

  self.$ = $(self);

  // User information
  self.isAuthenticated = null;
  self.id = null;
  self.username = null;

  self.E = {
    'LOAD': 'LOAD.App_services_user',
    'LOGOUT': 'LOGOUT.App_services_user'
  };

  self.onLoad = function(callback) {
    // If we are already initialized, callback immediately
    if (own.initialized) { callback(); }
    self.$.on(self.E.LOAD, callback);
  };

  own.refreshData = function() {
    
    console.log('user - refreshData');
    $U.ajax.get('/a/account/load/').done(function(data) {
          
      console.log('user - refreshData - got:', data);

      self.isAuthenticated = data['is_authenticated'];
      self.id = data['id'];
      self.username = data['username'];

      own.initialized = true;
      self.$.trigger(self.E.LOAD);
    });
  };

  own.init = function() {
    own.refreshData();
  };

  own.init();
};