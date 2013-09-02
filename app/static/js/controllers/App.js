App.controllers.App = function($content, $spinner) {

  var self = this,
    own = {},
    dom = {};

  /* ***** GRAB DOM REFERENCES ***** */
  dom.$content = $content;
  dom.$spinner = $spinner;

  /**********************************************************************
   * CONTENT LOADING
   **********************************************************************/

  self.loadAjaxContent = function(urlOrOptions, method, $container) {
    if (!$container) { $container = dom.$content; }
    if (!method) { method = 'GET'; }

    console.log('loadAjaxContent:', urlOrOptions);

    $U.ajax.request(method, urlOrOptions).done(function(data, status, xhr) {
      self.loadContent(data);
    });
  };

  self.loadContent = function(content, $container) {
    if (!$container) { $container = dom.$content; }
    console.log('loadContent:', content.length);

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

    // Scroll back to top
    $(document).scrollTop(0);

    self.instantiateContentViews($content);
  };

  self.instantiateContentViews = function($content) {

    console.log('instantiateContentViews:', $content);

    // Look view views to instantiate, including self. Do this in the most optimized way possible
    $content.find('._meta-view').andSelf().filter('._meta-view').each(function() {
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

  self.instantiateContentViews(dom.$content);

  History.Adapter.bind(window, 'statechange', function(e) {
    var state = History.getState();
    var uri = new Uri(state.hash)
      .addQueryParam('_bare', '1')
      .deleteQueryParam('_suid').deleteQueryParam(''); // No need to send the History.js identifier over to our server. Also remove the crap blank one History added
      
    self.loadAjaxContent(uri.toString());
  });


  $(document).on('click', 'a:not(.no-hijax)', function() {
    History.pushState(null, document.title, $(this).attr('href'));
    return false;
  });

  $(document).on('submit', 'form.hijax', function() {
    // Forms are the opposite. By default = no-hijax
    console.log('hijax this form!');

    var $form = $(this);
    $form.ajaxSubmit({
      data: {'_bare': true },
      success: function(content) {
        console.log('AJAX SUBMIT SUCCESS:', arguments);
        self.loadContent(content);
      }
    });

    return false;
  });

  console.log('App Initialized!');
};