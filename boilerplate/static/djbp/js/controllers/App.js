App.controllers.App = function($page) {

  var self = this;

  if (typeof Hijax != 'undefined') {
    // hijax app was included
    self.page = new Hijax($page);
  }
  self.view = new App.controllers.View();

  $(document).on('page-loaded.hijax', function() {
    debug.log('page-loaded.hijax');
    App.activeViews = self.view.instantiate($page);
  });

  App.activeViews = self.view.instantiate($page);

  self.showSpinner = function() {
    $('body').addClass('spinning');
  };

  self.hideSpinner = function() {
    $('body').removeClass('spinning');
  };

  $(document).ajaxStart(self.showSpinner);
  $(document).ajaxStop(self.hideSpinner);
};