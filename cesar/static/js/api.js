//Crear funcion para actualizar modal
function actualizarModal(producto) {
    $('#detallesModal .modal-title').text(producto.nombre);
    $('#detallesModal .modal-body').html(`
                <p>${producto.descripcion}</p>
                <p>Precio: $${producto.precio}</p>
            `);
}
$(document).ready(function () {
    const settings = {
        async: true,
        crossDomain: true,
        url: 'https://pizzaallapala.p.rapidapi.com/productos',
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'fd0b3bbe2emsh027ad7af237662ap1c097bjsn7a3f9c7a936d',
            'X-RapidAPI-Host': 'pizzaallapala.p.rapidapi.com'
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response.productos);

        const productContainer = $('#productContainer'); //Crear contenedor de producto

        //Iterar sobre la api
        $.each(response.productos, function (index, producto) {
            //Excluir productos por ID
            if (producto.id !== 33 && producto.id !== 48 && producto.id !== 49 && producto.id !== 50 && producto.id !== 51 && producto.id !== 52 && producto.id !== 53 && producto.id !== 54 && producto.id !== 44 && producto.id !== 46) {
                //Crear Cards
                const card = $('<div class="col-md-4 mb-3"></div>');
                card.append(`
                        <div class="card">
                            <!-- Si el producto no tiene imagen, se puede mostrar una imagen predeterminada o dejarlo en blanco -->
                            <img src="${producto.linkImagen || 'imagen_predeterminada.jpg'}" class="card-img-top" alt="">
                            <div class="card-body">
                                <h5 class="card-title">${producto.nombre}</h5>
                                <p class="card-text">${producto.descripcion}</p>
                                <a href="#" class="btn btn-primary">Detalles</a>
                            </div>
                        </div>
                    `);
                card.find('.btn').click(function (event) {
                    event.preventDefault(); //Evitar que el boton haga cosas raras
                    actualizarModal(producto); //Usar la funcion y actualizar el modal
                    $('#detallesModal').modal('show'); //Mostrar el modal
                });

                productContainer.append(card); //Agregar la card al contenedor de producto
            }
        });
    });
});