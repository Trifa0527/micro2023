function ajaxcall(){
    $.ajax({
        url : 'update',
        type : 'GET',
        datatype: 'json',
        success: function(data){
            var u = "Distance from the Thing : ";
            var t = "Today's temperature : ";
            var g = "Rotate : ";
            document.getElementById('ult').innerHTML=u+data['ult'] + 'cm';
            document.getElementById('tem').innerHTML=t+data['tem'] + '°C';
            document.getElementById('gyro').innerHTML=g+data['gyro'] + '°';
        }
    });
}
setInterval(ajaxcall, 1000);