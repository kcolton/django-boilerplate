App.controllers.App = function() {

  var self = this
    , $page = $('[data-app-page]');

  self.page = new App.controllers.Page();
  self.view = new App.controllers.View();

  self.loadPage = function(content) {
    console.log('loadContent:', content.length);
    $page.html(content.toString());

    App.activeViews = self.view.instantiate($page);
    $(document).scrollTop(0);
  };

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