window.addEventListener("load", function (){
    $(".trash").on("click", function() { trash( $(this).val() ); });
    $("#submit_edit").on("click", function() { edit(); });
    
    let date    = $(".date").val();
    let config_date = {
        locale: "ja",
        dateFormat: "Y-m-d",
        defaultDate: date
    }
    flatpickr(".date", config_date);
});

function trash(id){

    if(!confirm("本当に削除しますか？")){
        return false;
    }

    let url = DELETE_URL.replace("1", id);

    $.ajax({
        url: url,
        type: "DELETE",
        dataType: 'json'
    }).done( function(data, status, xhr){
        if(!data.error){
            window.location.href = RETURN_URL;
        }else{
            console.log("DELETE ERROR");
        }
    }).fail( function(xhr, status, error){
        console.log(status + ":" + error );
    });
}

function edit(){

    let form_elem   = "#news_edit_form";
    let data        = new FormData( $(form_elem).get(0) );
    let url         = $(form_elem).prop("action");

    $.ajax({
        url: url,
        type: "PUT",
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr){
        if(!data.error){
            // location.reload();
            console.log(url);
        }else{
            console.log("EDIT ERROR");
        }
    }).fail( function(xhr, status, error){
        console.log(status + ":" + error );
    });
}