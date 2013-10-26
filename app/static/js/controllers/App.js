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
    $container = $container || dom.$content;
    method = method || 'GET';

    console.log('loadAjaxContent:', urlOrOptions);

    $U.ajax.request(method, urlOrOptions).done(function(data, status, xhr) {
      console.log('loadAjaxContent success - ', arguments);
      self.loadContent(data);
    }).fail(function(xhr, textStatus, error) {
      console.log('loadAjaxContent fail - ', arguments);
      if (xhr.responseText) {
        self.loadContent(xhr.responseText);
      }
    }).always(function() {
      console.log('loadAjaxContent always - ', arguments);
    });
  };

  self.loadContent = function(content, $container) {
    $container = $container || dom.$content;
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
    $content.find('[data-app-view]').andSelf().filter('[data-app-view]').each(function() {
      var $viewContainer = $(this),
        viewName = $viewContainer.data('appView');

      console.log('found view:', viewName);

      if ($V[viewName]) {
        $RV[viewName] = new $V[viewName]($viewContainer);
      } else {
        console.log('COULD NOT FIND VIEW NAMED:', viewName);
      }

    });

  };

  self.changePage = function(url, postData) {
    History.pushState(postData, document.title, url);
  };

  self.startSpinning = function() {
    dom.$spinner.addClass('spinning');
  };

  self.stopSpinning = function() {
    dom.$spinner.removeClass('spinning');
  };

  /**********************************************************************
   * INITIALIZATION
   **********************************************************************/

  $U.ajax.setSpinner(dom.$spinner);

  self.instantiateContentViews(dom.$content);

  History.Adapter.bind(window, 'statechange', function(e) {
    var state = History.getState();


    // No need to send the History.js identifier over to our server. Also remove the crap blank one History added
    var uri = new Uri(state.hash)
      .addQueryParam('_bare', '1')
      .deleteQueryParam('_suid').deleteQueryParam('');

    var method = 'GET';
    var options = {
      url: uri.toString()
    };

    if (state.data && !History.isEmptyObject(state.data)) {
      options.data = state.data;
      method = 'POST';
    }

    self.loadAjaxContent(options, method); // todo - refactor is still in order I think
  });


  $(document).on('click', 'a[href]:not([data-app-no-hijax],[target])', function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;
    self.changePage($(this).attr('href'));
    return false;
  });

  $(document).on('submit', 'form[data-app-hijax]', function() {
    // Forms are the opposite. By default = no hijaxing
    console.log('hijax this form submit!');

    var $form = $(this);
    $form.ajaxSubmit({
      data: {'_bare': true },
      success: function(content) {
        console.log('hijaxForm ajaxSubmit success');
        self.loadContent(content);
      },
      error: function(xhr) {
        console.log('hijaxForm ajaxSubmit error', arguments);
        if (xhr.responseText) {
          self.loadContent(xhr.responseText);
        }
      }
    });

    return false;
  });

  console.log('App Initialized!');
};