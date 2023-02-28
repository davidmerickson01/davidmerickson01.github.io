<?php
session_start();
?>

<html>
<h1>Simple quiz page</h1>
<p>

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

<?php
$display_question = $question + 1;
echo "<h2>$display_question. $data[0]</h2>\n";
echo "<ol>\n";
echo "<li>$data[1]\n";
echo "<li>$data[2]\n";
echo "<li>$data[3]\n";
echo "<li>$data[4]\n";
echo "</ol>\n";
echo "Answer: $data[5]\n";
?>

<?php
// next question
$_SESSION["question"] = $question + 1;
?>
</html>
