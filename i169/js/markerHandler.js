AFRAME.registerComponent("markerhandler", {
    init: async function () {
  
      this.el.addEventListener("markerFound", () => {
        console.log("Se encontró el marcador");
        this.handleMarkerFound();
      });
  
      this.el.addEventListener("markerLost", () => {
        console.log("Se perdió el marcador");
        this.handleMarkerLost();
      });
    },
    handleMarkerFound: function () {
        let buttonDiv = document.getElementById("button-div");
        buttonDiv.style.display = "flex";

        var ratingButton = document.getElementById("rating-button");
        var orderButton  = document.getElementById("order-button");

        ratingButton.addEventListener("click", () => {
            console.log("clic")
            swal({
                icon: "warning",
                title: "Calificar platillo",
                text: "Procesando calificación"
            });
        });
        orderButton.addEventListener("click", () => {
            swal({
                icon: "https://imagenes.heraldo.es/files/image_990_556/uploads/imagenes/2016/07/12/_ok477504960720_74a1f9b1.png",
                title: "¡Gracias por tu orden",
                text: "¡Recibirás tu orden pronto"
            });
        });
    },
    handleMarkerLost: function () {
        let buttonDiv = document.getElementById("button-div");
        buttonDiv.style.display = "none";

    },
});
  