(function($) {
  var hijaxNot = ':not([data-app-no-hijax],[target])'
    , hijaxLinks = 'a[href]' + hijaxNot
    , hijaxForms = 'form' + hijaxNot;

  $(document).on('click', hijaxLinks, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;
    return !app.page.get($(this).attr('href'));
  });

  $(document).on('submit', hijaxForms, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;

    $(this).ajaxSubmit({
      data: {'_bare': true },
      complete: function(xhr, status) {
        console.log('hijaxForm ajaxSubmit complete', arguments);
        app.page.loadFromXhr(xhr);
      }
    });

    return false;
  });

})(jQuery);