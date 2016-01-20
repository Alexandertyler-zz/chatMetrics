//build the module named chatApp
var chatApp = angular.module('chatApp', ['ngRoute']);

chatApp.config(function($routeProvider) {
  $routeProvider

    .when('/', {
      templateUrl: '/templates/home.html',
      controller : 'mainController'
    })

    .when('/about', {
      templateUrl: '/templates/about.html',
      controller : 'aboutController'
    })

    .when('/contact', {
      templateUrl: '/templates/contact.html',
      controller : 'contactController'
    });
});

//create the controller and inject $scope into it
chatApp.controller('mainController', function($scope) {
  $scope.message = 'Test main injection';
});

chatApp.controller('aboutController', function($scope) {
  $scope.message = 'Test about injection';
});

chatApp.controller('contactController', function($scope) {
  $scope.message = 'Test contact injection';
});
