{%if word.pronoun_form == 'der'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">der</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">den</button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">dem</button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">die</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">das</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{% elif word.pronoun_form == 'ein'%}

<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">ein</button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">eine </button>
<button type="button" id="fill-button1" onclick="updateTextb()">einen</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">einer </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">einem </button>

</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>

{% elif word.pronoun_form == 'kein'%}

<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

    <td>
    <button type="button" id="fill-button1-4" onclick="updateTextb4()">kein</button>
    <button type="button" id="fill-button1-3" onclick="updateTextb3()">keine </button>
    <button type="button" id="fill-button1" onclick="updateTextb()">keinen</button>
    <button type="button" id="fill-button1-1" onclick="updateTextb1()">keinem</button>
    <button type="button" id="fill-button1-2" onclick="updateTextb2()">keiner</button>
    </td>

    </tr>  

<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'mein'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">meiner</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">meinen </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">meinem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">meine</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">mein</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'dein'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">deiner</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">deinen </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">deinem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">deine</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">dein</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'sein'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">seiner</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">seinen </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">seinem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">seine</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">sein</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'ihr'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">ihrer</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">ihren </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">ihrem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">ihre</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">ihr</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>

{%elif word.pronoun_form == 'unser'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">unserer</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">unseren </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">unserem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">unsere</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">unser</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'euer'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">eurer</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">euren </button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">eurem </button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">eure</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">euer</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'dies'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">dieser</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">diesen</button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">diesem</button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">diese</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">dieses</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'jede'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">jeder</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">jeden</button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">jedem</button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">jede</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">jedes</button>
</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>
{%elif word.pronoun_form == 'derselbe'%}
<form id="my-form" action='/checkwordspg/' method = "POST">

#{{word.id}} {{word.prep}}<input type="text" id="my-input-field-1" name="article">{{word.adj}} {{word.noun}}
<input type="hidden" id="custId" name="hidden_article" value="{{ word.pronoun }}">
<input type="hidden" id="custId" name="hidden_id" value="{{ word.id }}">

<table>
<tr>
    <th>Article</th>
    <th>Adj</th>

</tr>
<tr>

<td>
<button type="button" id="fill-button1" onclick="updateTextb()">derselben</button>
<button type="button" id="fill-button1-1" onclick="updateTextb1()">denselben</button>
<button type="button" id="fill-button1-2" onclick="updateTextb2()">demselben</button>
<button type="button" id="fill-button1-3" onclick="updateTextb3()">dieselben</button>
<button type="button" id="fill-button1-4" onclick="updateTextb4()">dasselbe</button>
<button type="button" id="fill-button1-5" onclick="updateTextb5()">dieselbe</button>

</td>

</tr>   
<button type="submit" id="submit-button">Answer</button>


</table>
</form>

function updateTextb1() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-1");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb2() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-2");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb3() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-3");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb4() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-4");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb5() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-5");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb6() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-6");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb7() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-7");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb8() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-8");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb9() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-9");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }

    function updateTextb10() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-10");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }


    function updateTextb11() {
        // Get the form field by its id
        var inputField = document.getElementById("my-input-field-1");
        var button = document.getElementById("fill-button1-11");
        // Update the form field with the button text
        inputField.value = button.innerHTML;
    }