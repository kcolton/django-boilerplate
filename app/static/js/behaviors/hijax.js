(function($) {
  var hijaxNot = ':not([data-app-no-hijax],[target])'
    , hijaxLinks = 'a[href]' + hijaxNot
    , hijaxForms = 'form' + hijaxNot;

  $(document).on('click', hijaxLinks, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;
    app.page.get($(this).attr('href'));
    return false;
  });

  $(document).on('submit', hijaxForms, function(e) {
    if (e.isDefaultPrevented() || e.isPropagationStopped()) return;

    console.log('hijax this form submit!');

    var $form = $(this);

    $form.ajaxSubmit({
      data: {'_bare': true },
      complete: function(xhr, status) {
        console.log('hijaxForm ajaxSubmit complete', arguments);
        app.page.loadFromXhr(xhr);
      }
    });

    return false;
  });

})(jQuery);