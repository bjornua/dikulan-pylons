<%inherit file="/main.mako"/>
<h1>Hjemmesidetilmelding</h1>
<p>
    Følgende <strong>kræver</strong> at du har en
    <strong>billetkode</strong> til det kommende arrangement.
    Billetkoden står på billetten.
</p>
<form method="post" action="${h.url_for(controller="user", action="doregister")}">
    <table>
        <tr>
            <th class="register_th_username"><label for="input_username">Ønsket brugernavn:</label></th>
            <td><input type="text" id="input_username" name="username"></td>
        </tr>
        <tr>
            <th class="register_th_password"><label for="input_password">Ønsket adgangskode:</label></th>
            <td><input type="password" id="input_password" name="password"></td>
        </tr>
        <tr>
            <th class="register_th_ticketcode"><label for="input_ticketcode">Billetkode:</label></th>
            <td><input type="password" id="input_ticketcode" name="ticketcode"></td>
        </tr>
        <tr>
            <td colspan="2" class="register_submit_cell"><input type="submit" value="Opret mig"></td>
        </tr>
    </table>
</form>