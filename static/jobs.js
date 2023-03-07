$("#task1").click(function(){
    $.ajax({
        url: '/newJob',
        data: 'jobNum=1',
        type: 'POST',
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    });
});