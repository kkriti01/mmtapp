"use strict";

var myApp = angular.module('myApp', []);

myApp.config(function($interpolateProvider ,$httpProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $interpolateProvider.startSymbol('{/');
        $interpolateProvider.endSymbol('/}');
    });
