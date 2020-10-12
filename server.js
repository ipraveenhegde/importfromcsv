var SSE = require("sse"),http = require("http");

const spawn = require("child_process").spawn;

var val = 0;

var server = http.createServer(function(req, res){	
	res.writeHead(200,{
	    'Content-Type': 'text/event-stream',
	    'Access-Control-Allow-Origin': '*'
	});  
	res.write("Python file is running now...")
    const pyProcess = spawn('python',['readfile.py']) 
	pyProcess.stdout.on('data',data => {
        res.write(data)
    });	 	
    
});

server.listen(8000,'localhost', function() { 
});