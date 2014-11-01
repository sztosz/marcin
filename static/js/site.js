/**
 * Created by Bartosz on 2014-08-13.
 */
function toggle_visibility(id) {
    var e = document.getElementById(id);
    if (e.style.display == 'block')
        e.style.display = 'none';
    else
        e.style.display = 'block';
}

function service_initial_hidden() {
    var ids = ['criminal', 'economic', 'registration', 'service', 'ending', 'individual', 'family', 'bankruptcy', 'administration', 'work', 'public'];
    var length = ids.length;
    for (var i = 0; i < length; i++) {
        var e = document.getElementById(ids[i]);
        e.style.display = 'none';
    }
}

/*
 Poniższą funkcję napisal Piotr Majewski dla swoich Klientów i Czytelników CNEB.pl
 do swobodnego używania
 funkcje setCookie i getCookie zaczerpnięte ze strony http://www.w3schools.com/js/js_cookies.asp
 i prawa do nich oraz ich rozpowszechniania posiada ich właściciel.

 UWAGA: Jesli widzisz krzaki zamiast polskich znakow, przed skopiowaniem skryptu zmien
 kodowanie na UTF-8 (zwykle w ustawieniach Widok > Kodowanie)
 */
function cookies() {
    function setCookie(c_name, value, exdays) {
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + exdays);
        var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString() + ";path = /");
        document.cookie = c_name + "=" + c_value;
    }

    function getCookie(c_name) {
        var i, x, y, ARRcookies = document.cookie.split(";");
        for (i = 0; i < ARRcookies.length; i++) {
            x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
            y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
            x = x.replace(/^\s+|\s+$/g, "");
            if (x == c_name) {
                return unescape(y);
            }
        }
    }

    setCookie('cookietest', 1, 1);
    var CookieTest = getCookie('cookietest');

    if (CookieTest == '1') { // uzytkownik obsluguje cookie

        var Userlanguage = window.navigator.userLanguage || window.navigator.language;
        var CookieName = 'accept-cookies-from-' + window.location.hostname;
        var Cookie = getCookie(CookieName);

        if (Cookie == '1') {

        } else {

            if (Userlanguage == 'pl') {
                alert('Ta strona wykorzystuje pliki cookie dla lepszego działania serwisu.\nMożesz zablokować pliki cookie w ustawieniach przeglądarki.');
            } else {
                alert('This page uses cookies for better performance of the site.\nYou can disable cookies in your browser settings.');
            }

        }

        setCookie(CookieName, 1, 10000);
    }
}

function loader() {
    if (document.title == 'Usługi prawne i pomoc prawna | Marcin Andreasik') {
        service_initial_hidden();
    }
    cookies();
}

window.onload = loader();
