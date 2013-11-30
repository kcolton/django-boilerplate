App.controllers.View = function() {
  var self = this
    , VIEW_SELECTOR = '[data-app-view]';

  // Search content for views to instantiate
  self.instantiate = function($content) {
    debug.log('instantiate view from content:', $content);

    var $views = $content.find(VIEW_SELECTOR).andSelf().filter(VIEW_SELECTOR),
      instantiatedViews = [];

    $views.each(function() {
      var $viewContainer = $(this)
        , viewName = $viewContainer.data('appView');

      debug.log('found view:', viewName);

      if (App.views[viewName]) {
        instantiatedViews.push(new App.views[viewName]($viewContainer));
      } else {
        debug.error('COULD NOT FIND VIEW NAMED:', viewName);
      }
    });

    return instantiatedViews;
  };

};