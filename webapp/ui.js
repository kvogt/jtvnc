var mx = 0
var my = 0;
var ms = "up";
var dirty = false;
var keys = new Array();

// Point this at your the ip an port where server.py is running
var host = '10.0.1.163:8000';


function updateMouse(e) {
	e = window.event ? window.event : e;
	if (e.clientX != mx || e.clientY != my) {
		mx = e.clientX;
		my = e.clientY;
		dirty = true;
	}
}

function keyDown(e) {
	var id = (window.event) ? event.keyCode : e.keyCode;
	keys.push(id);
	call('/keydown?id=' + id);
}

function keyUp(e) {
	var id = (window.event) ? event.keyCode : e.keyCode;
	keys = keys.splice(keys.indexOf(id), 1);
	call('/keyup?id=' + id);
}

function getState() {
	var obj = document.getElementById('desktop');
	var curleft = curtop = 0;
	var pos = new Object();
	do {
		curleft += obj.offsetLeft;
		curtop += obj.offsetTop;
	} while (obj = obj.offsetParent);
	pos.x = mx - curleft;
	pos.y = my - curtop;
	if (pos.x < 0) pos.x = 0;
	if (pos.y < 0) pos.y = 0;
	return pos;
}

function call(url) {
	var req = null;
	req = new XMLHttpRequest(); 
	req.open("GET", 'http://' + host + url, true);
	req.send(null);
}
	
function mouseMove(pos) {
	call('/move?x=' + pos.x + '&y=' + pos.y);
}

function mouseUp() {
	pos = getState();
	ms = "up";
	call('/up?x=' + pos.x + '&y=' + pos.y);
}

function mouseDown() {
	pos = getState();
	ms = "down";
	call('/down?x=' + pos.x + '&y=' + pos.y);
}

function loop() {
	pos = getState();
    document.getElementById('mx').value = pos.x;
    document.getElementById('my').value = pos.y;
    document.getElementById('mouse').value = ms;
    document.getElementById('keys').value = keys.join(',');
	if (dirty) {
		mouseMove(pos);
		dirty = false;
	}
}

setInterval(loop, 100);