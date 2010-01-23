<%inherit file="/main.mako"/>
<h1>Opret mig som bruger!</h1>
<p>
    Hvis du ikke har en bruger endnu,
    
    kan du ved hjælp af din <strong>billetkode</strong> selv
    <a href="${h.url_for(controller="user", action="register")}"> 
    oprette dig i systemet.</a>
</p>
<!--<p style="text-align:center;margin-top:10px;">
    
    <img src="/images/have-ticket.gif"/>
    </a>
</p>-->

<h1>Log Ind</h1>
<form method="post" action="${h.url_for(controller="user", action="dologin")}">
    <table>
        <tr>
            <th class="login_th_username"><label for="input_username">Brugernavn:</label></th>
            <td><input type="text" id="input_username" name="username"></td>
        </tr>
        <tr>
            <th class="login_th_password"><label for="input_password">Adgangskode:</label></th>
            <td><input type="password" id="input_password" name="password"></td>
        </tr>
        <tr>
            <td colspan="2" class="login_submit_cell"><input type="submit" value="Login"></td>
        </tr>
    </table>
</form>