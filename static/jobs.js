
let numJobs = 4

for(let i = 1; i <= numJobs; i++) {
    $("#task" + i.toString() ).click(function(){
        $.ajax({
            url: '/newJob',
            data: 'jobNum=' + i.toString(),
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
}
    

