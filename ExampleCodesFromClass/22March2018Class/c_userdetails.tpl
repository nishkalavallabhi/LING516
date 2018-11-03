<!DOCTYPE html> <html> <head> <style> div.container {width: 100%;border: 1px solid gray;}
    header, footer {padding: 1em;color: white; background-color: gray; clear: left;text-align: center;}
    img {width:15%;nav {float: left; max-width: 100px; margin: 60;}
    nav ul {list-style-type: none;padding: 0;} nav ul a {text-decoration: none;}}
    </style></head>

<script type="text/javascript">

     function validateForm()
     {
       var a = document.forms["Form"]["L1"].value;
       var b = document.forms["Form"]["YearsofEnglish"].value;
       var c = document.forms["Form"]["Otherdetails"].value;
       if (a == null || a == "")
       {
          alert("Please answer ALL 3 questions.");
          return false;
       }
       if (b == null || b == "")
       {
          alert("Please answer ALL 3 questions.");
          return false;
       }
        if (c == null || c == "")
       {
          alert("Please answer ALL 3 questions.");
          return false;
       }
     }
</script>

    <header> <font size="6">Reading Test</font></header>

<nav><center>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
<img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
    <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>
    <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"> <a href="#"></a>

</center></nav>

    <center><font size="6"><b>Login successful</b></font></center><br><br>

<font size="5"><font color="#3366ff"><i><center><b>Please tell us something about yourself by completing the below information.</b></center></i></font></font><br>

<form action="/readingonly" method="post" name="Form" onsubmit="return validateForm()"><center>

<br><font size="5">

1. What is your mother tongue? (mother tongue=first language)<br> <br><input type="text" name="L1" id="L1"style=font-size:18px;"height:25px"> <br>

<br><br>
2. How many years have you studied English?<br> <br><input type="text" name="YearsofEnglish" id="YearsofEnglish" style=font-size:18px;"height:25px"> <br> <br><br>

3. How would you rate your English language skills on a scale of 1-10 <br>
    (1=lowest, 10=highest). <br><br><input type="text" name="Otherdetails" id="Otherdetails" style=font-size:18px;"height:25px"> <br><br><br>


<input type="Submit" value="Next" style="font-family: sans-serif; font-size: 15px; height:40px; width:100px">
</font>
    <br><br>
    <input type="hidden" value={{username}} name="username"><br><br>
<footer>Copyright © Sowmya Vajjala-Balakrishna </footer></div></center></form>

</body></html><br><br><br>
