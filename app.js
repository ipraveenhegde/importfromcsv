var es = new EventSource("http://localhost:8000/")
es.onmessage = function (event) {
	console.log(event.data)
	document.getElementById('id1').innerHTML += event.data + "<br>";
}