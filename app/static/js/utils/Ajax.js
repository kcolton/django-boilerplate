App.utils.ajax = new function() {

  var self = this;

  self.request = function(method, urlOrOptions, data) {

    var options;

    if (typeof urlOrOptions == 'string') {
      options = {
        url: urlOrOptions,
        data: data
      };
    } else {
      options = urlOrOptions;
    }

    options.type = method;

    var xhr = $.ajax(options);

    return xhr;
  };

  self.setSpinner = function($spinner) {

    console.log('setSpinner!', $spinner.length);

    var $doc = $(document);

    $doc.ajaxStart(function() {
      console.log('ajaxStart');
      $spinner.addClass('spinning');
    });

    $doc.ajaxStop(function() {
      console.log('ajaxStop');
      $spinner.removeClass('spinning');
    });

  };

  self.get = self.request.curry('GET');
  self.post = self.request.curry('POST');
};

$A