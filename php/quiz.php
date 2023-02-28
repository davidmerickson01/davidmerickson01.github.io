<?php
session_start();
?>
<!DOCTYPE html>
<html>

<?php
// what question are we on?
if (isset($_SESSION["question"])) {
    $question =$_SESSION["question"];
}
else {
    $question = 0;
}

// find our question
$file_to_read = fopen('quiz.csv', 'r');
if($file_to_read !== FALSE){
    $n = 0;
    while (TRUE) {
        $data = fgetcsv($file_to_read, 100, ',');
        if ($data == FALSE) {
            // loop around to the beginning, which we remembered
            $question = 0;
            $data = $first_question;
            break;
        }
        if ($n == 0) {
            $first_question = $data; // remember it
        }
        if ($question == $n) break;
        $n = $n + 1;
    }
    fclose($file_to_read);
}
?>

<head>
<style>

body {
    background: #dFb687;
    font-size: 35pt;
    color: #ffffff;
}

.quizpanel {
    margin-left: auto;
    margin-right: auto;
    width: 1000px;
}

.answer_section {
    display: flex;
    /* default is row */
}

.bubble {
    border-radius: 25px;
    padding: 20px; 
    margin: 10px; 
    width: 200px;
    height: 150px; 
}

#question {
    /* TODO: I wanted to set width: 100%, but something wasn't working */
    width: 940px;
    background: #6F1D1B;
}

#answer1 {
    background: #99582A;
}
#answer2 {
    background: #432818;
}
#answer3 {
    background: #BB9457;
}
#answer4 {
    background: #FFE6A7;
}

/* I had to set the :hover selector for each id. unfortunate. */
#answer1:hover {
    background: #101010;
}
#answer2:hover {
    background: #101010;
}
#answer3:hover {
    background: #101010;
}
#answer4:hover {
    background: #101010;
}

#result_section {
    /* TODO: color: #101010; */
}

</style>
<script>
var correct_answer = <?php echo $data[5]; ?>;
function select(num)
{
    if (num == correct_answer) {
        text = "Right!";
    }
    else {
        text = "Wrong. Try again.";
    }
    document.getElementById("result_section").innerText = text;
}
</script>
</head>
<body>

<div class=quizpanel>
<h1>VSA Quiz Machine</h1>
<div class=bubble id=question><?php echo $data[0]; ?></div>

<div class=answer_section>
<div class=bubble id=answer1 onclick="select(1)"><?php echo $data[1]; ?></div>
<div class=bubble id=answer2 onclick="select(2)"><?php echo $data[2]; ?></div>
<div class=bubble id=answer3 onclick="select(3)"><?php echo $data[3]; ?></div>
<div class=bubble id=answer4 onclick="select(4)"><?php echo $data[4]; ?></div>
</div>

<div id=result_section></div>
</div>

<?php
// next question
$_SESSION["question"] = $question + 1;
?>

</body>
</html>
