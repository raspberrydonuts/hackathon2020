function initMap() {
    // Checks if navigator is enabled for the browser
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            // Stores the position as latitude and longitude
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            // setting geocoder to be able to get the address using latitude and longitude
            var geocoder = new google.maps.Geocoder();
            var latLng = new google.maps.LatLng(pos.lat, pos.lng);

            if (geocoder) {
                geocoder.geocode({ 'latLng': latLng }, function (results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                        console.log(results[0].formatted_address);
                    }
                    else {
                        console.log("Geocoding failed: " + status);
                    }
                });
            }
        });
    } else {
        console.log("Unable to get address")
    }
}

