<!DOCTYPE html> <html> <head> <style> div.container {width: 100%;border: 1px solid gray;}
    header, footer {padding: 1em;color: white; background-color: gray; clear: left;text-align: center;}
    img {width:15%;nav {float: left; max-width: 100px; margin: 60;}
    nav ul {list-style-type: none;padding: 0;} nav ul a {text-decoration: none;}}
    </style></head>
    <header> <font size="6">Reading Test for <i> {{username}}</i></font></header>


<script type="text/javascript">
     function validateForm()
     {
       var a = document.forms["Form"]["ProfTest1"].value;
       if (a == null || a == "")
       {
          alert("Please answer the question.");
          return false;
       }
     }

</script>

<nav><center>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
    <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
    <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>

</center></nav>


    <form action="/byepage" method="post">

<br> <center><font size="6"><b>Proficiency Test for {{username}} </b> </font></center><br>

<b><center><font size="5">STEP 1: </font></center></b><br>
    <center><font size="5">Please go to the below British Council website and take their brief English language test.</font><br><br><br>
       <font size="5"> The test will open in a new window. <br><br>
          Return to <b>THIS window </b>to ENTER your language test results.  <br><br><br>
            <font color="red">Do NOT close the new window until your scores are entered in Step 2 below.</font><br><br><br>
        <a href="http://learnenglish.britishcouncil.org/en/content" target="_blank">British Council Language Test</a><br>
       </font></center> <br> <br>

        <b> <font size="5"><center>STEP 2:</center></font></b><br>
    <font size="5"><center>After taking the British Council English language test, enter your results here:<br><br><br></center>

<center><b>Your score <input type="text" name="ProfTest1"style=font-size:18px;"height:25px" size="20"> %.</b></center><br><br><br>

        <center>


 <input type="Submit" value="Next"style="font-family: sans-serif; font-size: 15px; height:25px; width:70px"><br>
    <input type="hidden" value={{username}} name="username"><br><br><br>


</center><br><br></font></form>

    <footer>Copyright © Sowmya Vajjala-Balakrishna </footer></div></body></html>
