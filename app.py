from flask import Flask, redirect, request, jsonify, json, render_template
from googletrans import Translator

app = Flask(__name__)
tr = Translator()

@app.route("/")
def home():
	if request.args.get('text') or request.args.get('lang'):
		text = request.args.get('text')
		lang = request.args.get('lang')
	else:
		return """
<!DOCTYPE html>
<html>
<head>
    <title>Google Translate | By Avazbek</title>
    <link rel="icon" href="https://www.elitetourism.com/images/languange_icon.png">
</head>
<body>
    <script type="text/javascript">
        function myFunction() {
            /* Get the text field */
            var copyText = document.getElementById("myInput");
            /* Select the text field */
            copyText.select();
            copyText.setSelectionRange(0, 99999); /* For mobile devices */
            /* Copy the text inside the text field */
            navigator.clipboard.writeText(copyText.value);
            /* Alert the copied text */
            alert("Nusxalandi: " + copyText.value);
        }
    </script>
    <style type="text/css">
        article {
            background: linear-gradient( to right, hsl(98 100% 62%), hsl(204 100% 59%));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        
        h1 {
            font-size: 10vmin;
            line-height: 1.1;
        }
        
        body {
            background: hsl(204 100% 5%);
            min-block-size: 100%;
            min-inline-size: 100%;
            box-sizing: border-box;
            display: grid;
            place-content: center;
            font-family: system-ui;
            font-size: min(200%, 5vmin);
        }
        
        h1,
        p,
        b,
        body {
            margin: 0;
        }
        
        p,
        b,
        b {
            font-family: "Dank Mono", ui-monospace, monospace;
        }
        
        html {
            block-size: 100%;
            inline-size: 100%;
        }
    </style>
    <article>
        <h1>Google Translator</h1><br>
        <p>Ushbu API orqali siz google translatorga kirmasdan turib xoxlagan tilingizdagi so`zlarni tarjima qilishingiz mumkin!</p><br>
    </article>
</body>
</html>
    """
	try:
		transl = tr.translate(text, dest=f"{lang}")
		trans = transl.text
		if text and lang and trans:
			return jsonify(soz=text, tarjima_tili=lang, succesfull=trans)
	except:
		pass

if __name__ == '__main__':
    app.run(debug=True)
