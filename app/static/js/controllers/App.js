App.controllers.App = function() {

  var self = this,
    own = {},
    dom = {};

  /* ***** GRAB DOM REFERENCES ***** */
  dom.$content = $('#content');
  dom.$spinner = $('#spinner');

  /**********************************************************************
   * PRIVATE METHODS
   **********************************************************************/

  own.loadAjaxContent = function($container, url) {

    console.log('loadAjaxContent:', url);

    $U.ajax.get(url).done(function(data, status, xhr) {
      console.log('loadAjaxContent done:', arguments);
      own.loadContent($container, data);
    });

  };

  own.loadContent = function($container, content) {

    console.log('loadContent:', content);

    var $content = $('<div class="content">' + content.toString() + '</div>');

    // Look for a title meta
    $metaPageTitle = $content.find('._meta-pageTitle');
    if ($metaPageTitle.length) {
      console.log('found page title, setting:', $metaPageTitle.text());
      document.title = $metaPageTitle.text();
      $metaPageTitle.remove();
    }

    // Inject the html
    $container.html($content);

    own.instantiateContentViews($content);
  };

  own.instantiateContentViews = function($content) {

    console.log('instantiateContentViews:', $content);

    // Look view views to instantiate, including self. Do this in the most optimized way possible
    $content.find('._meta-hasView').andSelf().filter('._meta-hasView').each(function() {
      var $viewContainer = $(this),
        viewName = $viewContainer.data('view');

      console.log('found view:', viewName);

      if ($V[viewName]) {
        $RV[viewName] = new $V[viewName]($viewContainer);
      } else {
        console.log('COULD NOT FIND VIEW NAMED:', viewName);
      }

    });

  };

  /**********************************************************************
   * INITIALIZATION
   **********************************************************************/

  $U.ajax.setSpinner(dom.$spinner);

  own.instantiateContentViews(dom.$content);

  History.Adapter.bind(window, 'statechange', function(e) {
    var state = History.getState();
    var uri = new Uri(state.hash)
      .addQueryParam('_bare', '1')
      .deleteQueryParam('_suid').deleteQueryParam(''); // No need to send the History.js identifier over to our server. Also remove the crap blank one History added
      
    own.loadAjaxContent(dom.$content, uri.toString());
  });


  $(document).on('click', 'a:not(.no-hijax)', function() {
    History.pushState(null, document.title, $(this).attr('href'));
    return false;
  });

  // Load user
  $RS.user = new $S.User();

  console.log('App Initialized!');
};