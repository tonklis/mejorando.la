$(document).on('ready', onReady);

function onReady(){
  $('#enviar-mensaje').on('click', clickHandler);
  messagesRequest();
}

var clickHandler = function(){
  console.log($("#mensaje").val());

  var xhr = $.post('/mensajes/new/', {
    mensaje: $("#mensaje").val()
  });

  xhr.done(function(data){
    console.log("funcione bien", data);
  });

  xhr.fail(function(data){
    console.log(data);
    throw 'Error';
  });

  $("#mensaje").val('');
}

function messagesRequest(){
  var xhr = $.get('/mensajes/list');
  xhr.done(function(data){
    $("#chat").html('');
    data.forEach(function(mensaje){
      $('<li>' + mensaje + '</li>').appendTo( $("#chat") );
    });
    messagesRequest();
  });
}
