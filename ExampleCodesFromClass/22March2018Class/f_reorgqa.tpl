<!DOCTYPE html>
<html> <head> <style>
div.container {width: 100%;border: 1px solid gray;}header, footer {padding: 1em;color: white;background-color: gray; clear: left;text-align: center;}
nav {float: left; max-width: 190px; margin: 60;}
nav ul {list-style-type: none;padding: 0;} nav ul a {text-decoration: none;}
img {width:150%;nav {float: left; max-width: 100px; margin: 60;}
</style></head>

<script type="text/javascript">

     function validateForm()
     {
       var a = document.forms["Form"]["ReorgQ1Ans"].value;
       var b = document.forms["Form"]["ReorgQ2Ans"].value;
       if (a == null || a == "")
       {
          alert("Please go back and answer BOTH questions.");
          return false;
       }
       if (b == null || b == "")
       {
          alert("Please go back and answer BOTH questions.");
          return false;
       }
     }

</script>

<body>

<div class="container">
    <header> <font size="6">Reading Test for <i> {{username}}</i></font></header>
    <nav>
        <br><br>
        <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com">

    <br><br>
        <font size="4">
         <center><b>READING TEST OUTLINE</b><br><br>
            <i>
            {{text1}} </i>text<br><br>
             <i>{{text2}} </i>text<br><br>
             <i>{{text3}}</i> text<br><br>
             <i>{{text4}} </i>text<br><br>
             <i>{{text5}} </i>text<br><br>
             <i>{{text6}} </i>text<br><br>
             <i>   Proficiency Test
                <br><br></i></center>
    </font></nav>

        <article>
<br>
 <center><font size="6"><b>Question Set 2 of 3 for <i>{{rows[1]}}</i></b></font></center> </br>

        <font size="5"><font color="#3366ff"><center> <b>Use the text to answer the questions below.</b></center></font><br>

        <form action="/infqa" method="post"name="Form" onsubmit="return validateForm()">
<center>
<font size="5">
<textarea readonly rows="30*" cols="100"style="font-family: sans-serif; font-size: 20px" name="txt" wrap="hard" onmousedown='return false;' onselectstart='return false;'>
{{rows[0]}}</textarea>

<table border="1">
<br><br>
    <b><center>Question 3:</center></b><br>
    <center>{{row3}}</center> <br>
 <input type="radio" name="ReorgQ1Ans" value="True" />True
        <input type="radio" name="ReorgQ1Ans" value="False" />False

   <br><br>

<b>Question 4:</b><br><br>
    {{row4}} <br> <br>

            <input name="ReorgQ2Ans" id="LitQ2Ans" style=font-size:18px;"height:25px" size="80"><br><br>

        <font color="#9900cc"><b> When you are ready for more questions, click "next."</b></font><br><br>

    <input type="hidden" value={{username}} name="username"><br>

<input type="Submit" value="Next" style="font-family: sans-serif; font-size: 20px; height:40px; width:100px">

    <br></table></font></center></form> <br><br><br></font>
</article>
 <center> <footer>Copyright © Sowmya Vajjala-Balakrishna </footer> </center></div></body></html>
