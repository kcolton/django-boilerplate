Django Hijax
===============================================================================

Alpha!

## Required Statics:

*   django_hijax/hijax.js
*   django_hijax/hijax.js
*   Third-Party:
    *   jQuery
    *   URI.js
        *   django_hijax/ext/URI.js
        *   http://medialize.github.io/URI.js/
    *   History.js
        *   django_hijax/ext/jquery.history.js
        *   https://github.com/browserstate/history.js/

## Using:

*   Add django_hijax to installed apps
*   Add django_hijax.context_processor
*   Add django_hijax.Middleware
*   Use the @set_title middleware to set a title
    *   Pick up in your template using TITLE context, injected by the context processor
