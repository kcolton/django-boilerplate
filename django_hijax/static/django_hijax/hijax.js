window.DjangoHijax = function() {

  var self = this
    , hijaxNot = ':not([data-django-hijax-ignore],[target])'
    , hijaxLinks = 'a[href]' + hijaxNot
    , hijaxForms = 'form' + hijaxNot;

  $(document).on('click', hijaxLinks, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;
    return !self.get($(this).attr('href'));
  });

  $(document).on('submit', hijaxForms, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;

    $(this).ajaxSubmit({
      data: {'_bare': true },
      complete: function(xhr, status) {
        console.log('hijaxForm ajaxSubmit complete', arguments);
        self.loadFromXhr(xhr);
      }
    });

    return false;
  });

  self.get = function(url, params) {
    console.log('page.change url:', url, 'params:', params);
    if (!self.isInternalUrl(url)) return false;

    if (params) {
      url = new URI(url).addQuery(params).toString();
    }
    History.pushState(null, document.title, url);

    return true;
  };

  self.post = function(url, data) {
    data = data || {'_post': true}; // Empty object would not trigger post. See statechange handler
    console.log('page.change post:', url, 'data:', data);
    if (!self.isInternalUrl(url)) return false;
    History.pushState(data, document.title, url);
  };

  self.isInternalUrl = function(url) {
    var newUri = new URI(url)
      , currentUri = new URI(History.getState().url);
    return !newUri.hostname() || newUri.hostname() == currentUri.hostname();
  };

  self.loadFromXhr = function(xhr) {
    var statusCode = xhr.status
      , contentType = xhr.getResponseHeader('content-type')
      , externalRedirect = xhr.getResponseHeader('x-external-redirect')
      , release = xhr.getResponseHeader('x-release')
      , requestPath = xhr.getResponseHeader('x-request-path')
      , title = xhr.getResponseHeader('x-title')
      , currentUri = new URI(History.getState().url).absoluteTo()
      , newUri = requestPath ? new URI(requestPath).removeQuery('_bare').absoluteTo() : null;

    if (externalRedirect) {
      window.location = externalRedirect;
      return;
    }

    if (title) {
      document.title = title;
    }

    if (!newUri) {
      console.log('warning: received no x-request-path header:', xhr);
    }

    if (newUri && newUri.resource() != currentUri.resource()) {
      // Disconnect between where browser thinks it is, and how it got there. Probably redirect
      console.log('REDIRECT:', currentUri.resource(), '=>', newUri.resource());
      History.ignoreNextChange = true; // todo - gah! fix this!
      History.replaceState(null, title, newUri.resource());
    }

    console.log('loadContentFromXhr - status:', statusCode, 'requestPath:', requestPath,
      'current uri:', currentUri, 'new uri:', newUri, 'xhr:', xhr,
      'statusCode:', 'contentType:', contentType, 'release:', release);

    var content = xhr.responseText;

    console.log('loadContent:', content.length, contentType);

    $('body').html(content.toString()).toggleClass('django-hijax-content-type-text-plain', contentType != 'text/html');
    $(document).scrollTop(0);
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
      type: 'GET'
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