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
            if(data['ult']>50){
                document.getElementById('title').innerHTML='Elon';
                document.getElementById('img').setAttribute('src', 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202104/20/ab7c9cda-2fca-4205-8d10-540f5851823f.jpg');
            }else{
                document.getElementById('title').innerHTML='Jeffrey';
                document.getElementById('img').setAttribute('src', 'https://i.ytimg.com/vi/zQ9Po9UDqBc/maxresdefault.jpg');
            }
        }
    });
}
setInterval(ajaxcall, 1000);