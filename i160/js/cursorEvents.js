
AFRAME.registerComponent("cursor-listener", {
  schema: {
    selectedItemId: { default: "", type: "string" }
  },
  init: function() {
    this.handleClickEvents();
    this.handleMouseEnterEvents();
    this.handleMouseLeaveEvents();
  },
  handleClickEvents: function() {
    //  Eventos de clic
    this.el.addEventListener("click", evt => {
      const placesContainer = document.querySelector("#places-container");

      const { state } = placesContainer.getAttribute("tour");

      if (state === "places-list") {

        const id = this.el.getAttribute("id");

        const placesId = [
          "taj-mahal",
          "budapest",
          "new-york-city",
          "eiffel-tower"
        ];

        if (placesId.includes(id)) {
          placesContainer.setAttribute("tour", {
            state: "view",
            selectedCard: id
          });
        }
      }

      if (state === "view") {
        this.handleViewState();
      }
      if (state === "change-view") {
        this.handleViewState();
      }
    });
  },
  handleViewState: function() {
    const el = this.el;

    const id = el.getAttribute("id");

    const placesContainer = document.querySelector("#places-container");

    const { selectedItemId } = placesContainer.getAttribute("cursor-listener");

    // Mantener todas las imágenes con el ID de las imágenes más la extensión .jpg
    const sideViewPlacesId = ["place-1", "place-2", "place-3", "place-4"];

    if (sideViewPlacesId.includes(id)) {
      
      placesContainer.setAttribute("tour", {
        state: "change-view"
      });

      const skyEl = document.querySelector("#main-container");
      
      // Establecer la imagen de 360 grados al elemento del cielo.
      skyEl.setAttribute("material", {
        src: `./assets/360_images/${selectedItemId}/${id}.jpg`,
        color: "#fff"
      });
     
    }
  },
  handleMouseEnterEvents: function() {
    // Eventos 'mouseenter' del cursor.
    this.el.addEventListener("mouseenter", () => {
      const placeContainer = document.querySelector("#places-container");
      const { state } = placeContainer.getAttribute("tour");
      if (state === "places-list") {
        this.handlePlacesListState();
      }
    });
  },
  handlePlacesListState: function() {
    const id = this.el.getAttribute("id");
    const placesId = ["taj-mahal", "budapest", "new-york-city", "eiffel-tower"];
    if (placesId.includes(id)) {
      const placeContainer = document.querySelector("#places-container");
      placeContainer.setAttribute("cursor-listener", {
        selectedItemId: id
      });
      this.el.setAttribute("material", {
        color:"#D76B30",
        opacity: 1
      });
    }
  },
  handleMouseLeaveEvents: function() {
    // Eventos 'mouseleave' del cursor.
    this.el.addEventListener("mouseleave", () => {
      const placesContainer = document.querySelector("#places-container");
      const { state } = placesContainer.getAttribute("tour");
      if (state === "places-list") {
        const { selectedItemId } = this.data;
        if (selectedItemId) {
          const el = document.querySelector(`#${selectedItemId}`);
          const id = el.getAttribute("id");
          if (id == selectedItemId) {
            el.setAttribute("material", {
              color: "#0077CC",
              opacity: 1
            });
          }
        }
      }
    });
  },
  
});
