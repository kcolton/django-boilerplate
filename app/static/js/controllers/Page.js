App.controllers.Page = function() {
  var self = this;

  self.get = function(url, params) {
    console.log('page.change url:', url, 'params:', params);
    if (params) {
      url = new URI(url).addQuery(params).toString();
    }
    History.pushState(null, document.title, url);
  };

  self.post = function(url, data) {
    data = data || {'_post': true}; // Empty object would not trigger post. See statechange handler
    console.log('page.change post:', url, 'data:', data);
    History.pushState(data, document.title, url);
  };

  self.loadFromXhr = function(xhr) {
    var statusCode = xhr.status
      , contentType = xhr.getResponseHeader('content-type')
      , location = xhr.getResponseHeader('location')
      , release = xhr.getResponseHeader('x-release')
      , requestPath = xhr.getResponseHeader('x-request-path')
      , title = xhr.getResponseHeader('x-title');

    document.title = title;

    var currentState = History.getState();

    var currentUri = new URI(currentState.url);
    var newUri = new URI(requestPath).removeQuery('_bare');

    if (newUri.resource() != currentUri.resource()) {
      // Disconnect between where browser thinks it is, and how it got there. Probably redirect
      console.log('REDIRECT:', currentUri.resource(), '=>', newUri.resource());
      History.ignoreNextChange = true; // todo - gah! fix this!
      History.replaceState(null, title, newUri.resource());
    }

    console.log('loadContentFromXhr - status:', statusCode, 'requestPath:', requestPath,
      'current uri:', currentUri.resource(), 'new uri:', newUri.resource(), 'xhr:', xhr,
      'statusCode:', 'contentType:', contentType, 'location:', location, 'release:', release);

    app.loadPage(xhr.responseText);
  };

  History.Adapter.bind(window, 'statechange', function(e) {
    var state = History.getState();

    // Todo - kill
    // This state change has already been taken care of
    if (History.ignoreNextChange) {
      History.ignoreNextChange = false;
      return;
    }

    var uri = new URI(state.hash)
      .addQuery('_bare', 'true')
      .removeQuery('_suid'); // remove history.js internal identifier before sending to server

    var options = {
      'dataType': 'html'
    };

    if (state.data && !History.isEmptyObject(state.data)) {
      options.type = 'POST';
      options.data = state.data;
    }

    console.log('history stateChange - loading uri:', uri, 'options:', options);
    options.dataType = options.dataType || 'html';

    $.ajax(uri.toString(), options).always(function(dataOrXhr, textStatus, errorOrXhr) {
      var success = textStatus == 'success'
        , error = success ? null : errorOrXhr
        , xhr = success ? errorOrXhr : dataOrXhr;

      self.loadFromXhr(xhr);
    });
  });


};