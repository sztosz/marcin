(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date();
    a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

ga('create', 'UA-53241332-1', 'auto');
ga('send', 'pageview');
function initialize() {
    var map_canvas = document.getElementById('map_canvas');
    var myLatlng = new google.maps.LatLng(51.101933, 17.002238);
    var map_options = {
        center: myLatlng,
        zoom: 15,
    };
    var map = new google.maps.Map(map_canvas, map_options);
    var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: 'Kancelaria'
    });
}
google.maps.event.addDomListener(window, 'load', initialize);
