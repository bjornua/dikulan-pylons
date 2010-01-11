<%inherit file="/xhtml11.mako"/>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title>DIKULAN - The Challenge</title>
        <link media="screen" rel="stylesheet" type="text/css" href="/css/underside/screen.css"/>
        <link media="print" rel="stylesheet" type="text/css" href="/css/underside/print.css"/>
    </head>
    <body>
        <div id="main">
            <div id="top">
                <img alt="" src="/images/page-top.png"/>
            </div>
            <div id="middle">
                <div id="middle-content">                    
                    <ul id="menu">
                        <li class="menu-item"><a href="/"            >Forside           </a></li>
                        <li class="menu-item"><a href="/information" >Information       </a></li>
                        <li class="menu-item"><a href="/food-options">Madmuligheder     </a></li>
                        <li class="menu-item"><a href="/tournaments" >Turneringer/events</a></li>
                        <li class="menu-item"><a href="/rules"       >Regler            </a></li>
                        <li class="menu-item"><a href="/seatbooking">Pladsreservation  </a></li>
                        <li class="menu-item"><a href="/gallery"     >Galleri           </a></li>
                        <li class="menu-item"><a href="/contact"     >Kontakt           </a></li>
                        <li class="menu-item"><a href="/news"        >Nyheder           </a></li>
                    </ul>
                    <div id="main-content">
                        ${next.body()}
                    </div>
                </div>
            </div>
            <div id="bottom">
                <img id="top" alt="" src="/images/page-bottom.png"/>
            </div>
        </div>
    </body>