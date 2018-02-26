# JShell
JShell - Get a JavaScript shell with XSS.

### Usages
Run <b>shell.py</b></br> and JShell will automatically try to detect your IP address, default LPORT is <b>33</b>.

<img src='https://i.imgur.com/lIXNTWv.png' />

As you can see the payload has been generated and now all you have to do is to deliver this payload to the victim.</br>
As soon as you do that, you will get a JS shell over netcat where you can execute your JavaScript code in victim's browser as soon as the injected page is open.</br>
Here's a screenshot:
<img src='https://i.imgur.com/zEW46GM.png' />

#### Credits, Disclaimer & License
This script uses the method demostrated by <a href="https://twitter.com/brutelogic">Rodolfo Assis</a></br>
<b>Disclaimer:</b> I am not responsible for the shit you do with this tool.</br>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
