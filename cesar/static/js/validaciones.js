//Validacion formulario
$(document).ready(function(){

    $("#formulario").submit(function(event){
        var nombre = $("#itNombre");
        var contrasena = $("#itContrasena");
        var valido = true;

        // Verificar si los campos están vacíos y mostrar mensajes de error
        // Verificacion del nombre
        if(nombre.val().trim() === "") {
            $("#mensaje1").text("Por favor, escribe tu nombre de usuario.").show();
            nombre.addClass("error-input");
            valido = false;
        } else {
            $("#mensaje1").hide();
            nombre.removeClass("error-input");
        }
        // Verificacion del apellido
        if(contrasena.val().trim() === "") {
            $("#mensaje2").text("Por favor, ingresa tu contraseña.").show();
            contrasena.addClass("error-input");
            valido = false;
        } else {
            $("#mensaje2").hide();
            contrasena.removeClass("error-input");
        }

        // Si todos los campos están completos y válidos, mostrar el alert de confirmacion
        if(valido) {
            alert("Todos los campos están completos y válidos. ¡Gracias por registrarte!");
        }

        // Si algún campo está vacío, detener el envío del formulario y mostrar el alert de error
        if(!valido) {
            event.preventDefault();
            alert("Error! Algun campo no está completo o no es válido. (Asegurese de que estén completos o este validado correctamente)");
        }
    });
});

$(document).ready(function() {
    $('#btnGuardar').click(function() {
        const itemsLength = parseInt($('#itemsLength').val());
        if (itemsLength == 0) {
            $('#errorCarritoModal').modal('show');
        } else {
            $('#compraExitosaModal').modal('show');
        }
    });
});