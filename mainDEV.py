from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)
#FZN SITE CODE #2343 (JJOKE-S)
@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>James wanted this</title>
            <style>
                img {
                    width: 300px; /* Adjust the width as needed */
                    height: auto;
                }
                .content {
                    text-align: center;
                    margin-top: 20px;
                }
                #bankThing {
                    width: 700px;
                    height: 100px;
                    background-color: white;
                    color: black;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    cursor: pointer;
                    margin: 20px auto;
                }
            </style>
        </head>
        <body>
            <div class="content">
                <h1>Jamie you were sent this domain that i spent £10 on because your being a nob. (: so please stop</h1>
                <img src="/static/photo.jpg" alt="Photo">
                <hr>
                <p>I was asked to remove the mug and to avoid being tight i have granted that wish</p>
                <p>in replacement i'm just going to put some songs here instead!</p>
                <p>Also i'm not paying for this domain next year so ill just buy a diffrent one</p>
                <p>if you have a idea for it theres a contact email at the bottom of all the songs</p>
                <hr>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/2DaxqgrOhkeH0fpeiQq2f4?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/6FlOCziOXI157pvUREAh3E?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/35L2mk5sX8odYilmk8I251?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/72NIcEinjlDjxXfWIaXIv1?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4pbEwQiDjPln3oYlijXuOE?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/5yzGKcmGJAYDP7r1KmOcQ7?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>                 
                <p>This is a site hosted by FZN LLC any questions? gmp9cbed@duck.com</p>
                <p>©2024 FZN LLC</p>
                <hr>
                <video width="640" height="360" controls>
                    <source src="/static/4kcat.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <div id="bankThing">4K samsung recored video above</div>
            </div>
            <script>
                let clickCount = 0;
                let firstClickTime = 0;

                document.getElementById('bankThing').addEventListener('click', function() {
                    const currentTime = new Date().getTime();

                    if (clickCount === 0) {
                        firstClickTime = currentTime;
                    }

                    if (currentTime - firstClickTime <= 2000) { // 5 seconds window
                        clickCount++;
                        if (clickCount === 20) {
                            window.location.href = 'https://jamiesampsonisanob.com/static/jamie1.jpg'; // THIS WONT WORK IF YOUR HOSTING LOCALY
                        }
                    } else {
                        clickCount = 1;
                        firstClickTime = currentTime;
                    }
                });
            </script>
        </body>
        </html>
    ''')

@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=False)

#THIS CODE BELONGS TO FZN LLC MODDING OF THIS CODE IS ALLOWED AS THIS PROGECT IS DISCONDINUED
#IF YOU USE THIS CODE!!
#FZN HAVE NOTHING!! TO DO WITH THE MODS YOU MADE TO SAID CODE
#DO NOT!! MENTION FZN AS THE OWNER OF THE WEBSITE OR CODE IF YOU HAVE MODDED IT!
#DO NOT!! CONTACT FZN FOR SUPPORT WITH THIS CODE EVERYTHING DONE WITH THIS CODE IS YOUR RESPONSIBILITY!!!!!
#DO NOT!! USE THIS CODE UNDER THE DOMAIN "Jamiesampsonisanob.com"
#DO NOT!! PUT FZN MEMBERS NAMES ON THIS CODE (taylor, kal, james, max, etc..)
#DO NOT!! USE THIS AS HATE SPEECH TO ANY PERSON THIS IS A JOKE SITE CODE NOT A HARRASSMENT SITE!
# -need more info or have a question? contact FZN at fzncte@gmail.com-
