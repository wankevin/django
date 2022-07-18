//function start_upload_telemetry(){
//    $.ajax({
//            url: 'http://192.168.0.3:8000/show/test',
//            success: successFunction,
//        })
//};
//
//function successFunction(msg) {
//        document.getElementById("temperature").textContent="Temperature : "+ msg.temperature
//        document.getElementById("humidity").textContent="Humidity : "+ msg.humidity
//        document.getElementById("datetime_now").textContent="Update Time :"+ msg.datetime
//
//    };
//
//
//setInterval(start_upload_telemetry,1000);

console.log(window.location.host + '/ws/online_number/');
var socket = new WebSocket('ws://' + window.location.host + '/ws/online_number/');
        socket.onopen = function(e){
              console.log ("open", e);
            }
        socket.onerror = function(e){
          console.log ("error", e)
        }
        socket.onmessage = function(e){
            var data = JSON.parse(e.data);
            var message = data['message'];
            console.log("message",e);
            document.querySelector('#app').innerText = message;
        }
