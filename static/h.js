 
function imgags(){


                my = 0
                var xhr = new XMLHttpRequest();

                xhr.open('GET', '/static/hjjjj.json', true);

                xhr.send(); // (1)

                xhr.onreadystatechange = function() { // (3)
                    if (xhr.readyState != 4) return;


                    if (xhr.status != 200) {
                        alert(xhr.status + ': ' + xhr.statusText);
                    } else {
                        var b = xhr.responseText;
                        var h = JSON.parse(b)
                        my = h[0]['enter'][0];
                        console.log(my)
                        nu = h[0]['enter'][1]
                        console.log(nu)
                        var con = document.getElementById('con')
                        while (con.firstChild) {
                            con.removeChild(con.firstChild);
                        }

                        for (var i = 0; i < nu.length; i++) {

                            var big = document.createElement('div')
                            big.className = 'main'
                            var inner = document.createElement('div')
                            inner.className = 'inner'
                            big.appendChild(inner)
                            var imgcontainer = document.createElement('div')
                            imgcontainer.className = 'imgcontainer'
                            inner.appendChild(imgcontainer)
                            var img = document.createElement('img')

                            var k = nu[i]

                            img.setAttribute('src', k)
                            if (img.height > 400) {
                                img.className = 'img500'
                            }
                             img.setAttribute('id', 'img')

                            imgcontainer.appendChild(img)
                            console.log(i)
                            con.appendChild(big)
                            console.log(img)


                        }


                    }

                }

        }
imgags()
 j = [];
 ida = []
var images = document.getElementById('ju')
var gifs = document.getElementById('ju1')
if (window.matchMedia("(min-width: 400px)").matches) {
  /* the viewport is at least 400 pixels wide */
} else {
  /* the viewport is less than 400 pixels wide */
}
var gifs = document.getElementById('ju1')
var imgs = document.getElementById('ju')
imgs.setAttribute('data-active', '')
imgs.addEventListener('click', koll)
    gifs.addEventListener('click', koll  )
function koll(e) {
     loll(e.target.id)
    sravnenie()
}
function loll(id){
     switch (id){
         case 'ju':
             gifs.removeAttribute('data-active', '')
             imgs.setAttribute('data-active', '')
         case 'ju1':
             imgs.removeAttribute('data-active', '')
             gifs.setAttribute('data-active', '')
     }
}
 