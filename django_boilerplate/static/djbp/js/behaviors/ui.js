(function($) {

  // Let any kind of element trigger a page change
  $(document).on('click.app', '[data-app-href]', function() {
    return !app.page.get($(this).data('appHref'));
  });

  // Datepickers
  $(document).on('focus.app.app-datepicker', 'input[data-app-datepicker]', datepickerHandler);
  $(document).on('click.app.app-datepicker', '[data-app-datepicker]:not(input)', datepickerHandler);

  function datepickerHandler(e) {
    var $this = $(this)
      , datepickerFor = $this.data('appDatepicker')
      , $el = datepickerFor ? $(datepickerFor) : $this;

    var options = {
      onSelect: function() {
        // Blur gets triggered before date gets updated so we need an additional event
        $el.trigger('update.app.app-datetime-field');
      }
    };

    $el.datepicker(options).datepicker('show');
  }

  // Datetime fields
  var dtUpdateEvents = [
    'blur.app.app-datetime-field',
    'keypress.app.app-datetime-field',
    'update.app.app-datetime-field'
  ];

  var dtFieldSelector = 'input[data-app-datetime-time],input[data-app-datetime-date]';

  $(document).on(dtUpdateEvents.join(' '), dtFieldSelector , dtFieldHandler);

  function dtFieldHandler(e) {
    if (e.which && e.which != 13) return;

    var $field = $(this).parents('[data-app-datetime-field]'),
      $prettyDate = $field.find('input[data-app-datetime-date]'),
      $prettyTime = $field.find('input[data-app-datetime-time]'),
      $input = $field.find('input[data-app-datetime]'),
      combined = $prettyDate.val().replace(' ', '') + ' ' + $prettyTime.val().replace(' ', '');

    var fieldMoment = moment(combined, 'MM/DD/YYYY hh:mmA');

    if (fieldMoment.isValid()) {
      $input.val(fieldMoment.format('YYYY-MM-DD HH:mm'))

      $prettyDate.val(fieldMoment.format('MM/DD/YYYY'));
      $prettyTime.val(fieldMoment.format('hh:mm A'));
    }
  }

})(jQuery);