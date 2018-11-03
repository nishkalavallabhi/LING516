<!DOCTYPE html> <html> <head> <style> div.container {width: 100%;border: 1px solid gray;}header, footer {padding: 1em;color: white;
    background-color: gray; clear: left;text-align: center;}
nav {float: left; max-width: 190px; margin: 60;}
    nav ul {list-style-type: none;padding: 0;} nav ul a {text-decoration: none;}
    img {width:150%;nav {float: left; max-width: 100px; margin: 60;}
    </style></head>

    <script type="text/javascript">

     function validateForm()
     {
       var a = document.forms["Form"]["LitQ1Ans"].value;
       var b = document.forms["Form"]["LitQ2Ans"].value;
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

<body><div class="container">
    <header> <font size="6">Reading Test for <i> {{username}}</i></font></header>

     <nav>
        <br><br>
        <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="books">

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

<br>
    <center><font size="6"><b>Question Set 1 of 3 for <i> {{rows[1]}}</i></b></font><br><br>
       <font size="5"> <font color="#3366ff"><b>Answer the below questions based on the text you just read.<br><br>Please  <font color="red"><u>do NOT go back</u></font></b></font> to the previous page.
<br>
           <font size=""5">

<form action="/reorgqa" method="post" name="Form" onsubmit="return validateForm()">
   <table border="1">

            <br><br>

      <b><center>Question 1:</b></br></br>
    {{row1}} <br> <br>

        <input type="radio" name="LitQ1Ans" value="True" />True
        <input type="radio" name="LitQ1Ans" value="False" />False


   <br><br><br>
<b>Question 2:</b></br></br>
    {{row2}} <br> <br>

                <input name="LitQ2Ans" id="LitQ2Ans" style=font-size:18px;"height:25px" size="80"  >

       <br><br><br>
        <font color="#9900cc"><b> When you are ready for more questions, click "next."</b></font><br>

    <input type="hidden" value={{username}} name="username"><br>

<input type="Submit" value="Next" style="font-family: sans-serif; font-size: 15px; height:40px; width:100px"></table></form></font></center>


    <br><br><br>

<center> <footer>Copyright © Sowmya Vajjala-Balakrishna </footer></center> </div></body></html>
