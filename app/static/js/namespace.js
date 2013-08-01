var $ = jQuery,
    BOOT = BOOT || {};

/* Global namespaces */
var App = {
  
  api: {},
  controllers: {},
  services: {},
  views: {},
  utils: {},
  ui: {},

  runtime: {
    controllers: {},
    services: {},
    views: {}
  }
};

/* Shortcuts */
var $A  = App.api,
    $C  = App.controllers,
    $S  = App.services,
    $U  = App.utils,
    $V  = App.views,
    $UI = App.ui,

    $RC = App.runtime.controllers, 
    $RS = App.runtime.services, 
    $RV = App.runtime.views;

// We don't like this guy 'round these "Web 4.0" parts.
document.write = $.noop;

// Logging and debugging

window.DEBUG = (window.DEBUG || BOOT.env != 'prod');

// todo - console.log