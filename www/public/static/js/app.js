//build the module named chatApp
var chatApp = angular.module('chatApp', ['ngRoute']);

chatApp.config(function($routeProvider) {
  $routeProvider

    .when('/', {
      templateUrl : 'public/home.html',
      controller : 'mainController'
    })

    .when('/about', {
      templateUrl : 'public/about.html',
      controller : 'aboutController'
    })

    .when('/contact', {
      templateUrl : 'public/contact.html',
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
