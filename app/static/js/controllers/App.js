App.controllers.App = function() {

  var self = this
    , $page = $('[data-app-page]');

  self.page = new App.controllers.Page();
  self.view = new App.controllers.View();

  self.loadPage = function(content, contentType) {
    contentType = contentType || 'text/html';

    console.log('loadContent:', content.length, contentType);

    if ($page.attr('class')) {
      // todo - can be better
      var pageClasses = $page.attr('class').split(' ');

      for (var i = 0; i < pageClasses.length; i++) {
        if (pageClasses[i].indexOf('app-page-type') === 0) {
          $page.removeClass(pageClasses[i]);
        }
      }
    }

    var pageClass = 'app-page-type-' + contentType.replace('/', '-');
    $page.addClass(pageClass).html(content.toString());

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