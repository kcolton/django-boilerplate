window.App = {
  controllers: {},
  views: {},
  activeViews: null
};

if (typeof console === 'undefined') {
  console = {
    log: debug.log
  };
}

