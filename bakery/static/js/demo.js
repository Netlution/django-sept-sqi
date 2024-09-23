window.onload = function() {
    var popup = document.getElementById("newsletter-popup");
    var closeBtn = document.getElementsByClassName("close")[0];

    popup.style.display = "block";

    closeBtn.onclick = function() {
        popup.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == popup) {
            popup.style.display = "none";
        }
    }
}
