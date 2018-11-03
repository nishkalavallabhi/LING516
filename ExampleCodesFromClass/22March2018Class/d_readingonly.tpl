<!DOCTYPE html> <html>
<head><style>
    div.container {width: 100%;border: 1px solid gray}
    p{padding-top: 0px;padding-right: 20px;padding-bottom: 20px;padding-left: 12px;}
    header, footer {color: white; background-color: gray; clear: left;text-align: center;}

    nav {float: left; max-width: 190px; margin: 60;}
    nav ul {list-style-type: none;padding: 0;}
    nav ul a {text-decoration: none;}

    article {margin-center: 100px;border-left: 1px solid gray;overflow: hidden;}
    img {width:150%;nav {float: left; max-width: 100px; margin: 60;}
    myclass {font-family: Verdana;color: black;}

<style type="text/css">
textarea {
   font-size: 20pt;
   font-family: Arial;
}
</style>

 <script type="text/javascript">

     function function1() {
     startTime = new Date(); //Starts the clock
     }

     function function2()
     {
       duration = (new Date() - startTime);
       document.getElementById("timespent").value = duration;
     }

</script>
</head>

<body onload="function1()"><div class="container">

    <header> <font size="6">Reading Test for <i> {{username}}</i></font></header>

    <nav>
        <br><br>
        <img src="http://seriousreading.com/wp-content/uploads/2015/12/wooden-bookshelf-full-of-books-800.jpg" alt="W3Schools.com"><br>
    <br>
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
    <font size="6"><center><b>Reading Preview : <i>{{textname}}</i></b></center></font><br>

 <center><font size="5"><font color="#3366ff"><b>
Read the below text. The next page will include questions about this reading.<br><br>
     You can take notes during the test BUT please <font color="red"><u> do NOT use the back button</u></font></b></font></font></center><br>

<font size="5">
       <form action="/litqa" method="post">

<input type="hidden" name="timespent" id="timespent" value=timespent> <center>

        <textarea readonly rows="30*" cols="100"style="font-family: sans-serif; font-size: 20px" name="txt" wrap="hard" onmousedown='return false;' onselectstart='return false;'>
{{rows[0]}}</textarea><br>

          <font color="#9900cc"><b> <br>When you are ready to answer questions, click "next."</b></font><br><br>

           </center></table><font size="5">

             <center>
                 <input type="Submit" value="Next" onclick="function2()" style="font-family: sans-serif; font-size: 15px; height:40px; width:100px">


      <br></center></font>
    <input type="hidden" value={{username}} name="username"><br>

            </form></body></html><br>

    </article><footer>Copyright © Sowmya Vajjala-Balakrishna </footer></div></body></html>
