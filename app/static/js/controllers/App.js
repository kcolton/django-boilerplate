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

  self.loadContentAjax = function(url, options, $container) {
    options = options || {};
    $container = $container || dom.$content;

    console.log('loadContentAjax:', url, options);
    options.dataType = options.dataType || 'html';

    $.ajax(url, options).always(function(dataOrXhr, textStatus, errorOrXhr) {


      var success = textStatus == 'success',
        error = success ? null : errorOrXhr,
        xhr = success ? errorOrXhr : dataOrXhr,
        statusCode = xhr.status,
        contentType = xhr.getResponseHeader('content-type'),
        location = xhr.getResponseHeader('location'),
        release = xhr.getResponseHeader('x-release'),
        requestPath = xhr.getResponseHeader('x-request-path');

      var currentState = History.getState();

      var currentUri = new URI(currentState.url);
      var newUri = new URI(requestPath).removeQuery('_bare');

      if (newUri.resource() != currentUri.resource()) {
        // Disconnect between where browser thinks it is, and how it got there. Probably redirect
        console.log('REDIRECT:', currentUri.resource(), '=>', newUri.resource());
        History.replaceState({_stateChangeComplete: true}, document.title, newUri.resource());
      }

      self.loadContent(xhr.responseText);

      console.log('loadContentAjax - complete - status:', statusCode, 'requestPath:', requestPath,
        'current uri:', currentUri.resource(), 'new uri:', newUri.resource(), 'xhr:', xhr,
        'statusCode:', 'contentType:', contentType, 'location:', location, 'release:', release);
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

    // This state change has already been taken care of
    if (state.data._stateChangeComplete) return;

    var uri = new URI(state.hash)
      .addQuery('_bare', 'true')
      .removeQuery('_suid'); // remove history.js internal identifier before sending to server

    var options = null;

    if (state.data && !History.isEmptyObject(state.data)) {
      options = {
        type: 'POST',
        data: state.data
      };
    }

    self.loadContentAjax(uri.toString(), options); // todo - refactor is still in order I think
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