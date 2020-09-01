
// $( document ).ready(function() {
//     console.log( "ready!" );
//     $('#pills-ngo').load('../charityapp/templates/users/ngo_signup.html');

// })
function load_home (e) {
    (e || window.event).preventDefault();

    fetch("/acc/ngo/register" /*, options */)
    .then((response) => response.text())
    .then((html) => {
        document.getElementById("content").innerHTML = html;
    })
    .catch((error) => {
        console.warn(error);
    });
}