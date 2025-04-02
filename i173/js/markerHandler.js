var tableNumber = null;
AFRAME.registerComponent("markerhandler", {

    init: async function () {
        if(tableNumber === null){
            this.askTableNumber();        }

        // obtener la colección de platillos
      var dishes = await this.getDishes();
  
      this.el.addEventListener("markerFound", () => {
        if(tableNumber !== null){
            var markerId = this.el.id;
            this.handleMarkerFound(dishes, markerId);
        }
      });
  
      this.el.addEventListener("markerLost", () => {
        console.log("Se perdió el marcador");
        this.handleMarkerLost();
      });
    },

    askTableNumber: function () {
        var iconUrl = "https://raw.githubusercontent.com/jadwer/3dModels/refs/heads/main/hunger.png";

        swal({
            text: "¡Bienvenido a nuestro restaurante 'El Antojo'! ¿Cuál es tu número de mesa?",
            icon: iconUrl,
            content: {
                element: "input",
                attributes: {
                    placeholder: "Tu número de mesa",
                    type: "number",
                    min: 1
                }
            }, // <form><input type="number" min=1 placeholder="Tu número de mesa"><button type="submit">Confirmar</button></form>
            closeOnClickOutside: false,
        }).then(inputValue => {
            tableNumber = inputValue;
            swal({
                icon: "success",
                title: "¡Mesa confirmada!",
                text: `Tu número de mesa es: ${tableNumber}`
            });
        });
    },

    handleMarkerFound: function (dishes, markerId) {
        // Obtener el día
        var todaysDate = new Date(); // "2021-06-01"
        var todaysDay = todaysDate.getDay(); // 4

        // De Domingo a Sábado: 0 - 6
        var days = [
            "Domingo",
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado"
        ];

        var dish = dishes.filter(dish => dish.id === markerId)[0];

        // dish.unavailable_days // ["Domingo", "Jueves"]
        if(dish.unavailable_days.includes(days[todaysDay])){ 
            swal({
                icon: "warning",
                title: dish.dish_name.toUpperCase(),
                text: "¡Este platillo no está disponible hoy! 😢",
                timer: 2500,
                buttons: false
            });
        } else {

            var model = document.querySelector(`#model-${dish.id}`);

            // Actualizar el contenido UI de VISIBILIDAD de la escena AR (MODELO, INGREDIENTES Y PRECIO)
            console.log(model)
            model.setAttribute("visible", true);

            var ingredientsContainer = document.querySelector(`#main-plane-${dish.id}`);
            ingredientsContainer.setAttribute("visible", true);

            var pricePlane = document.querySelector(`#price-plane-${dish.id}`);
            pricePlane.setAttribute("visible", true);
            

            let buttonDiv = document.getElementById("button-div");
            buttonDiv.style.display = "flex";

        }


        var ratingButton = document.getElementById("rating-button");
        var orderButton  = document.getElementById("order-button");
        var orderSummaryButton = document.getElementById("order-summary-button");
        var payButton = document.getElementById("pay-button");

        // Manejo de eventos para los botones
        ratingButton.addEventListener("click", () => { this.handleRatings(dish)});
        orderButton.addEventListener("click", () => {
            var tNumber;
            tableNumber <= 9 ? (tNumber = `T0${tableNumber}`) : (tNumber = `T${tableNumber}`);
            this.handleOrder(tNumber, dish);

            swal({
                icon: "https://imagenes.heraldo.es/files/image_990_556/uploads/imagenes/2016/07/12/_ok477504960720_74a1f9b1.png",
                title: "¡Gracias por tu orden!",
                text: "¡Pronto recibirás lo que mereces!",
                timer: 2000,
                buttons: false
            });
        });

        orderSummaryButton.addEventListener("click", () => {
            this.handlerOrderSummary(/* tableNumber*/);
        });

        payButton.addEventListener("click", () => this.handlePayment());

    },
    handlePayment: function () {
        // Cerrar el modal
        document.getElementById("modal-div").style.display = "none";

        // Obtener el número de mesa
        var tNumber;
        tableNumber <= 9 ? (tNumber = `T0${tableNumber}`) : (tNumber = `T${tableNumber}`);

        // Restablecer la orden actual en la base de datos
        firebase
            .firestore()
            .collection("tables")
            .doc(tNumber)
            .set({
                    current_orders: {}, // Restablecer la orden actual
                    total_bill: 0,
                    id: tNumber
            })
            .then(() => {
                swal({
                    icon: "success",
                    title: "¡Gracias por su compra!",
                    text: "¡Esperemos que haya recibido todo lo que se merece!",
                    timer: 2500,
                    buttons: false
                });
            });
    },
    getOrderSummary: async function (tNumber) {
        return await firebase
            .firestore()
            .collection("tables")
            .doc(tNumber)
            .get()
            .then(doc => {
                return doc.data();
            });
    },

    handlerOrderSummary: async function () {
     var tNumber;
     tableNumber <= 9 ? (tNumber = `T0${tableNumber}`) : (tNumber = `T${tableNumber}`);

     // Obtener el resumen de la orden
     var orderSummary = await this.getOrderSummary(tNumber);

     // Cambiar la visibilidad del div modal
     var modalDiv = document.getElementById("modal-div");
        modalDiv.style.display = "flex";

        var tableBodyTag = document.getElementById("bill-table-body");

        // Eliminar datos antiguos de tr (Table row - fila de tabla)
        tableBodyTag.innerHTML = "";

        // Obtener la clave de current_orders
        var currentOrders = Object.keys(orderSummary.current_orders);

        console.log("current_orders: ")
        console.log(currentOrders);

        currentOrders.map(i => {
            if (i !== "total_bill" && i !== "id") {

                // Crear la fila de la mesa
                var tr = document.createElement("tr");
    
                // Crear celdas/columnas para ITEM, Precio, Cantidad y Total
                var item = document.createElement("td");
                var price = document.createElement("td");
                var quantity = document.createElement("td");
                var subtotal = document.createElement("td");
    
                // Añadir contenido HTML
    
                item.innerHTML = orderSummary.current_orders[i].name;
    
                price.innerHTML = `$${orderSummary.current_orders[i].price}`;
                price.setAttribute("class", "text-center");
    
                quantity.innerHTML = orderSummary.current_orders[i].quantity;
                quantity.setAttribute("class", "text-center");
    
                subtotal.innerHTML = `$${orderSummary.current_orders[i].subtotal}`;
                subtotal.setAttribute("class", "text-center");
    
                // Añadir las celdas a la fila
                tr.appendChild(item);
                tr.appendChild(price);
                tr.appendChild(quantity);
                tr.appendChild(subtotal);
    
                // Añadir la fila a la tabla
                tableBodyTag.appendChild(tr);

                // crear una fila para el precio total
                var totalTr = document.createElement("tr");

                // Crea una celda vacía (para no tener datos);
                var td1 = document.createElement("td");
                td1.setAttribute("class", "no-line");

                // Crear una celda vacíua para no tener datos
                var td2 = document.createElement("td");
                td2.setAttribute("class", "no-line");

                // Crear una ceda para el TOTAL
                var td3 = document.createElement("td");
                td3.setAttribute("class", "no-line text-center");

                // Crear un elemento <Strong> para enfatizar el texto
                var strongTag = document.createElement("strong");
                strongTag.innerHTML = "TOTAL:";
                td3.appendChild(strongTag);

                // Crear una celda para el precio total
                var td4 = document.createElement("td");
                td1.setAttribute("class", "no-line text-right");
                td4.innerHTML = `$${orderSummary.total_bill}`;

                // Añadir cerdas a la fila

                totalTr.appendChild(td1);
                totalTr.appendChild(td2);
                totalTr.appendChild(td3);
                totalTr.appendChild(td4);

                // Añadir la fila a la tabla
                tableBodyTag.appendChild(totalTr);
            } // if que filtra solo los platillos


        });
   
    },

    handleOrder: function (tNumber, dish) {
        firebase
        .firestore()
        .collection("tables")
        .doc(tNumber)
        .get()
        .then(doc => {
            var details = doc.data();

            if(details["current_orders"][dish.id]){ // si ya existe el platillo en la orden actual
                //incrementar la cantidad actual
                details["current_orders"][dish.id]["quantity"] += 1;

                //calcular el subtotal de un elemento
                var currentQuantity = details["current_orders"][dish.id]["quantity"];
                details["current_orders"][dish.id]["subtotal"] = currentQuantity * dish.price;
            } else {
                details["current_orders"][dish.id] = {
                        name: dish.dish_name,
                        price: dish.price,
                        quantity: 1,
                        subtotal: dish.price
                };
            }

            details["total_bill"] += dish.price;


            // Actualizar la orden en la base de datos
            firebase
            .firestore()
            .collection("tables")
            .doc(doc.id)
            .update(details)
            .then(() => {
                swal({
                    icon: "success",
                    title: "¡Platillo añadido a la orden!",
                    text: `${dish.dish_name} ha sido añadido a tu orden.`
                });
            });
        });
    },
    handleMarkerLost: function () {
        let buttonDiv = document.getElementById("button-div");
        buttonDiv.style.display = "none";

    },

    getDishes: async function () {
        return await firebase
            .firestore()
            .collection("dishes")
            .get()
            .then(snap => {
                return snap.docs.map(doc => doc.data());
            });
    },
    getTempOrder: async function (tNumber) {
        return await firebase
            .firestore()
            .collection("tables")
            .doc(tNumber)
            .get()
            .then(doc => {
                return doc.data();
            });
    },

    handleRatings: async function (dish) {
        console.log("Llamó a handleRatings")
        // Obtener el número de mesa
        var tNumber;
        tableNumber <= 9 ? (tNumber = `T0${tableNumber}`) : (tNumber = `T${tableNumber}`);

        // Obtener el resumen de la orden desde la base de datos
        var orderSummary = await this.getOrderSummary(tNumber);
        
        var currentOrders = Object.keys(orderSummary.current_orders);

        if( currentOrders && currentOrders.includes(dish.id)) {

            // Mostramos el modal de calificación limpio
            document.getElementById("rating-modal-div").style.display = "flex";
            document.getElementById("rating-input").value = 0; // Calificación por defecto
            document.getElementById("feedback-input").value = ""; // Comentario por defecto

            // Evento de clic del botón de calificación
            var saveRatingButton = document.getElementById("save-rating-button");
            saveRatingButton.addEventListener("click", () => {
               document.getElementById("rating-modal-div").style.display = "none"; // Cerrar el modal
                var ratingValue = document.getElementById("rating-input").value;
                var feedbackValue = document.getElementById("feedback-input").value;

                // Guardar la calificación y el comentario en la base de datos
                firebase
                    .firestore()
                    .collection("ratings")
                    .doc(dish.id)
                    .update({
                        num_votes: firebase.firestore.FieldValue.increment(1),
                        sum_votes: firebase.firestore.FieldValue.increment(ratingValue),
                        reviews: firebase.firestore.FieldValue.arrayUnion(feedbackValue) 
                   })
                    .then(() => {
                        swal({
                            icon: "success",
                            title: "¡Gracias por tu calificación!",
                            text: "¡Esperamos que hayas disfrutado de tu platillo!"
                        });
                    });
            });

            // Obtener los valores de entrada

            // Actualizar la calificación en la base de datos
        } else {
            swal({
                icon: "warning",
                title: "¡No puedes calificar este platillo!",
                text: "¡No has ordenado este platillo aún! 😢",
                timer: 2500,
                buttons: false
            })
            // Mostrar un mensaje de advertencia
        }
    },

});
  