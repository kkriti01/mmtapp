myApp.controller('airportcontroller', ['$scope', '$http', function($scope, $http){
    $http.get('/api/airport').success(function(data) {
        $scope.airports = data;
    });
    $scope.sorttype = {
        elevation: 'elev',
        direct_flight:'direct_flights',
        ratings: 'rating',
    }
    $http.get('/static/js/countries.json').success(function(data) {
        $scope.country = data;
        //console.log(data);
        $scope.getImage =function(country){
            //console.log(country);
            var code = data[country];
            var path = '/static/images/';
            var url = path.concat(code);
            var image_url = url.concat('.png');
            return image_url;
        }
});
$scope.search = function () {
            var parameters = {
                search: $scope.key
            };
            var config = {
                params: parameters
            };
            $http.get('/api/airport', config)
            .success(function (data, status, headers, config) {
                $scope.airports = data;
            })
            .error(function (data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
        };


}]);
