function disbaleButton(){
	document.getElementById('submit').disabled = true;
}
function save() {
	var msg = document.getElementById('msg');
	msg.innerHTML = 'Your Application has been submitted';
}
