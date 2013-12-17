App.controllers.App = function($page) {

  var self = this;

  if (typeof DjangoHijax != 'undefined') {
    // DjangoHijax app was included
    self.page = new DjangoHijax($page);
  }
  self.view = new App.controllers.View();

  $(document).on('page-loaded.django-hijax', function() {
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