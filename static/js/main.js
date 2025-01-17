function load_page() {
    // useful link: https://stackoverflow.com/questions/9847580/how-to-detect-safari-chrome-ie-firefox-and-opera-browser
    if (/*@cc_on!@*/false || !!document.documentMode) {
        document.getElementById('browser_alert').hidden = false
    }

    document.addEventListener("DOMContentLoaded", function(event) {
        if (localStorage.getItem('scrollloc') == window.location) {
            var scrollpos = localStorage.getItem('scrollpos');
            if (scrollpos) window.scrollTo(0, scrollpos);
            localStorage.setItem('scrollpos', 0);
        }
    });

    window.onbeforeunload = function(e) {
        localStorage.setItem('scrollpos', window.scrollY);
        localStorage.setItem('scrollloc', window.location);
    };
}

function toggle(element_id) {
    element = document.getElementById(element_id);
    element.hidden = !element.hidden;
}

function convention_mode(is_select) {
    document.getElementById('programme_selection').hidden = !is_select
    if (document.getElementById('programme_creation') != null) {
        document.getElementById('programme_creation').hidden = is_select
    }
}

load_page()