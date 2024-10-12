from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
aplication = QApplication([])
janela =  QMainWindow()
janela.setWindowTitle('Melhores jogos do Playstation 2')
navegador  = QWebEngineView()
conteudo_html = '''



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    *{
        box-sizing: content-box;
        margin: 0;
        padding: 0;
        font-family: Arial, Helvetica, sans-serif;
    }
    a{
        text-decoration: none;
        color: black;
    }
    img{
        width: 100%;
        border-radius: 20px;
    }
    #image{
        background-image: url('https://wallpaperaccess.com/full/17450.jpg');
        background-size: cover;
        width: 100%;
        height: 50vh;
        margin: 0px;
        color: white;
    }
 article{
    margin: 0px auto;
    padding: 40px;
    top: -100px;
    border-radius: 20px;
    max-width: 1000px;
    position: relative;
    background-color: #ffffff;
 }

 .lista_games>li{
    margin: 50px;
 }
 .lista_games{
    display: flex;
    flex-direction: column;
    align-items: center;
 }
 p{
    text-align: justify;
 }
 #image h1{
    text-align: center;
 }
 #sh2,#black {
    display: none;
 }
 button{
    width: 200px;
    height: 60px;
    border-radius: 30px;
    background-color: #166665;
    color: white;
    font-size: 20px;
    border: 0px solid ;
    font-weight: 600;
    transition: .3s;
 }
 button:hover{
    background-color: black;
 }
 @media screen and (min-width:350px) and (max-width:720px) {
    
    article{
        background-color: white;
        top: 0px;
        border-radius: 0px;
        padding: 0px;
    }
    .list{
        margin: 50px;
    }
    img{
        max-width: 100%;
    }
 }
</style>

<body>
    <div id="image">
        <h1>TOP 5: Melhores jogos do playstation 2</h1>
        <span id="subtitulo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse ut saepe perferendis
            consequuntur. Ipsa libero qui neque, omnis aliquid perspiciatis, praesentium vero dolorum porro fugiat illo
            optio ut doloremque doloribus. Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur,
            necessitatibus eligendi? Possimus, eum molestias! Provident asperiores quae dolores! Perspiciatis provident
            eum
            quisquam voluptate doloribus labore voluptatem blanditiis assumenda iste natus. Lorem ipsum dolor sit, amet
            consectetur adipisicing elit. Laboriosam, dignissimos culpa sed, commodi ipsa itaque nihil, sequi quibusdam
            non
            excepturi autem nobis! Necessitatibus totam repellat illo enim repudiandae doloribus quibusdam!
        </span>
    </div>
    <article>
        
        
      
        <ol class="list">
            <a href="#mgs3">
                <li>Metal Gear Solid 3 (2004)</li>
            </a>
            <a href="#gtasa">
                <li>Grand Theft Auto - San Andreas (2004)</li>
            </a>
            <a href="#re4">
                <li>Resident Evil 4 (2005)</li>
            </a>
            <a href="#black">
                <li>Black (2006)</li>
            </a>
            <a href="#sh2">
                <li>Silent Hill 2 (2001)</li>
            </a>
        </ol>


        <ol class="lista_games">
            <li id="mgs3">
                <h1>Metal Gaer Solid 3 (2004)</h1>
                <img src="https://wallpapercave.com/wp/WwuOAPf.jpg" alt="metal gear solid 3">
              
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati molestiae blanditiis vero ipsa
                    fuga,
                    totam maiores perferendis autem magni odio accusamus voluptas veritatis itaque odit. Fugit aut
                    suscipit
                    quibusdam consequatur? Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure voluptatem quia perferendis, ab maxime nulla atque veniam iste sit, modi adipisci? Mollitia aliquid eveniet fugiat minima vel quidem laboriosam possimus. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt quod deleniti pariatur neque adipisci laborum voluptatibus ipsam nisi, fugit qui tempore libero alias? Et vero in illum quae repellendus dolor! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas architecto ab sint ducimus! Perferendis ullam illo provident, quas vel doloremque voluptatibus, optio ducimus suscipit enim nisi dignissimos sed ea hic? Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati iure perferendis totam rem deleniti et doloremque numquam veniam officia voluptatibus, temporibus dolore molestiae architecto eius ex sint cumque soluta laborum!</p>
            </li>
            <li id="gtasa">
                <h1>Grand Theft Auto - San Andreas (2004)</h1>
                <img src="https://th.bing.com/th/id/OIP.kZrHPVAUrOyywJ8DHybk-AHaFj?rs=1&pid=ImgDetMain" alt="gta sa">
              
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati molestiae blanditiis vero ipsa
                    fuga,
                    totam maiores perferendis autem magni odio accusamus voluptas veritatis itaque odit. Fugit aut
                    suscipit
                    quibusdam consequatur?</p>
            </li>
            <li id="re4">
                <h1>Resident Evil 4 (2005)</h1>
                <img src="https://th.bing.com/th/id/R.034af6a219ac2ebe1acf888e3d075d40?rik=YATk%2f8J13Ybbkw&pid=ImgRaw&r=0" alt="resident evil 4">
                
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati molestiae blanditiis vero ipsa
                    fuga,
                    totam maiores perferendis autem magni odio accusamus voluptas veritatis itaque odit. Fugit aut
                    suscipit
                    quibusdam consequatur?</p>
            </li>
               <button onclick="eventClick()">Ler mais</button>
            <li id="black">
                <h1>Black (2006)</h1>
                <img src="https://th.bing.com/th/id/R.a9d4ebdfe96050ff629312a26becda41?rik=ikF2qho4S%2bkZ1w&pid=ImgRaw&r=0&sres=1&sresct=1" alt="black">
              
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati molestiae blanditiis vero ipsa
                    fuga,
                    totam maiores perferendis autem magni odio accusamus voluptas veritatis itaque odit. Fugit aut
                    suscipit
                    quibusdam consequatur?</p>
            </li>
            <li id="sh2">
                <h1>Silent Hill 2 (2001)</h1>
                <img src="https://th.bing.com/th/id/R.44cfee453f1e1a98ce072af56536a5f4?rik=3eCr%2f8vsek1baQ&riu=http%3a%2f%2fwww.hardcoregaming101.net%2fwp-content%2fuploads%2f2019%2f09%2fDesktop-Screenshot-2019.04.21-13.40.23.20.jpg&ehk=72QqavhuhQBd%2fQctrlYI%2fFAIaTdLbRvlm%2bs51zRdM%2fk%3d&risl=&pid=ImgRaw&r=0" alt="silent hil 2">
               
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati molestiae blanditiis vero ipsa
                    fuga,
                    totam maiores perferendis autem magni odio accusamus voluptas veritatis itaque odit. Fugit aut
                    suscipit
                    quibusdam consequatur?</p>
            </li>
        </ol>
    </article>
<script>
    var li2 = document.getElementById('black')
    var li3 = document.getElementById('sh2')
    let buttonClick = false
   function eventClick(){
        if(!buttonClick){
            li2.style.display = 'block'
            li3.style.display = 'block'
        }
        else{
            li2.style.display = 'none'
            li3.style.display = 'none'
        }
        buttonClick = !buttonClick

    }
</script>
</body>

</html>
'''
navegador.setHtml(conteudo_html)
janela.setCentralWidget(navegador)
janela.show()
aplication.exec_()