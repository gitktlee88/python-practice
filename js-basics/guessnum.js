$(document).ready(function() {
   var randomNum = Math.floor((Math.random() * 100) + 1),
        count = 0,
        GuessCount = $("#GuessCount");
        Hint = $("#Hint"),
        GuessInput = $("#GuessInput"),
        GuessButton = $("#GuessButton");

    $("img").hide();

    GuessButton.on("click", function() {
        count++;
        if(GuessInput.val() < randomNum) {
            GuessCount.html("Guess Count: " + count);
            Hint.html("<strong id='Incorrect'>Incorrect! Guess Higher.</strong>");
        }
        else if(GuessInput.val() > randomNum) {
            GuessCount.html("<strong>Guess Count: </strong>" + count);
            Hint.html("<strong id='Incorrect'>Incorrect! Guess Lower.</strong>");
        }
        else {
            GuessCount.html("Guess Count: " + count);
            Hint.html("<strong id='Correct'>Correct!</strong>");
            $("img").fadeIn().delay(4000).fadeOut(1000);
        }
    });
});
