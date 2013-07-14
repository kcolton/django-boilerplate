/**
 * Returns a curried function.
 * See http://ejohn.org/blog/partial-functions-in-javascript/
 */
Function.prototype.curry = function() {
  var fn = this,
      args = Array.prototype.slice.call(arguments);
  
  return function() {
    return fn.apply(this, args.concat(Array.prototype.slice.call(arguments)));
  };
};

/**
 * Returns a partial function.
 * See http://ejohn.org/blog/partial-functions-in-javascript/
 */
Function.prototype.partial = function() {
  var fn = this,
      args = Array.prototype.slice.call(arguments);
  return function() {
    var arg = 0;
    for (var i = 0; i < args.length && arg < arguments.length; i++)
      if (args[i] === undefined)
        args[i] = arguments[arg++];
    return fn.apply(this, args);
  };
};