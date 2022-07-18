function start_upload_telemetry(){
    $.ajax({
            url: 'http://192.168.0.3:8000/show/test',
            success: successFunction,
        })
};

function successFunction(msg) {
        document.getElementById("temperature").textContent="Temperature : "+ msg.temperature
        document.getElementById("humidity").textContent="Humidity : "+ msg.humidity
        document.getElementById("datetime_now").textContent="Update Time :"+ msg.datetime

    };


setInterval(start_upload_telemetry,1000);
