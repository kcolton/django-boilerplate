App.controllers.App = function() {

  var self = this
    , $page = $('[data-app-page]');

  self.page = new DjangoHijax();
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