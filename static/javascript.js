const room_name=document.getElementById("room_name").textContent;


var socket = new WebSocket('ws://' + window.location.host + '/ws/real_time_status/'+room_name);
        socket.onopen = function(e){
              console.log ("open", e);
            }
        socket.onerror = function(e){
          console.log ("error", e)
        }

        socket.onmessage = function(message){
            console.log(message);
            var telemetry = JSON.parse(message.data);
            document.getElementById("temperature").textContent="Temperature : "+ telemetry.temperature
            document.getElementById("humidity").textContent="Humidity : "+ telemetry.humidity
            document.getElementById("datetime_now").textContent="Update Time :"+ telemetry.datetime

//            document.querySelector('#app').innerText = message;
        }
