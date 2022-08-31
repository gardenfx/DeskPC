function time(){
        var date = new Date();
        var Year = date.getFullYear(),
            month = (date.getMonth() + 1) < 10 ? '0' + (date.getMonth()+1) : (date.getMonth()+1),
            day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate(),
            hours = date.getHours() < 10 ? '0' + date.getHours() : date.getHours(),
            minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes(),
            seconds = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds()
        var time = day + '-'+month+'-'+Year+'  '+hours+':'+minutes+':'+seconds;
        document.querySelector('#time').innerHTML =time ;
    }
    setInterval(function(){
        time();
    },1);
