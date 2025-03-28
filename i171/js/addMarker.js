AFRAME.registerComponent('create-markers', {
    schema: {
        
    },

    init: async function () {
        var mainScene = document.querySelector("#main-scene");
        var dishes = await this.getDishes();

        dishes.map(dish => {
            // Creamos el marcador
            var marker = document.createElement("a-marker");
            marker.setAttribute("id", dish.id);
            marker.setAttribute("type", "pattern");
            marker.setAttribute("url", dish.marker_pattern_url);
            marker.setAttribute("cursor", {
                rayOrigin: "mouse"
            });

            marker.setAttribute("markerhandler", {});
            mainScene.appendChild(marker);


            // Obtener el día
            var todaysDate = new Date();
            var todaysDay = todaysDate.getDay();

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

            if(!dish.unavailable_days.includes(days[todaysDay])){
                
                // Creamos el modelo 3D
                var model = document.createElement("a-entity");
                model.setAttribute("id", `model-${dish.id}`);
                model.setAttribute("position", dish.model_geometry.position);
                model.setAttribute("rotation", dish.model_geometry.rotation);
                model.setAttribute("scale", dish.model_geometry.scale);
                model.setAttribute("gltf-model", dish.model_url);
                model.setAttribute("gesture-handler", {});
                model.setAttribute("visible", false);
                marker.appendChild(model);
    
                // Contenedor de descripcion del platillo
                var mainPlane = document.createElement("a-plane");
                mainPlane.setAttribute("id", `main-plane-${dish.id}`);
                mainPlane.setAttribute("position", { x: 0, y: 0, z: 0 });
                mainPlane.setAttribute("rotation", { x: -90, y: 0, z: 0 });
                mainPlane.setAttribute("width", 1.7);
                mainPlane.setAttribute("height", 1.5);
                mainPlane.setAttribute("visible", false);
                marker.appendChild(mainPlane);
    
                // Creamos el plano del título
                var titlePlane = document.createElement("a-plane");
                titlePlane.setAttribute("id", `title-plane-${dish.id}`);
                titlePlane.setAttribute("position", { x: 0, y: 0.89, z: 0.02 });
                titlePlane.setAttribute("rotation", { x: 0, y: 0, z: 0 });
                titlePlane.setAttribute("width", 1.69);
                titlePlane.setAttribute("height", 0.3);
                titlePlane.setAttribute("material", { color: "#F0C30F" });
                mainPlane.appendChild(titlePlane);
    
                // Creamos el título del platillo
                var dishTitle = document.createElement("a-entity");
                dishTitle.setAttribute("id", `title-${dish.id}`);
                dishTitle.setAttribute("position", { x: 0, y: 0, z: 0.1 });
                dishTitle.setAttribute("rotation", { x: 0, y: 0, z: 0 });
                dishTitle.setAttribute("text", {
                    font: "monoid",
                    color: "black",
                    width: 1.8,
                    height: 1,
                    align: "center",
                    value: dish.dish_name.toUpperCase()
                });
                titlePlane.appendChild(dishTitle);
    
                // Lista de ingredientes
                var ingredients = document.createElement("a-entity");
                ingredients.setAttribute("id", `ingredients-${dish.id}`);
                ingredients.setAttribute("position", { x: 0, y: 0, z: 0.1 });
                ingredients.setAttribute("rotation", { x: 0, y: 0, z: 0 });
                ingredients.setAttribute("text", {
                    font: "monoid",
                    color: "black",
                    width: 2,
                    align: "left",
                    value: `${dish.ingredients.join("\n\n")}`
                });
                mainPlane.appendChild(ingredients);
    
                // plano del precio
                var pricePlane = document.createElement("a-image");
                pricePlane.setAttribute("id", `price-plane-${dish.id}`);
                pricePlane.setAttribute("src", "https://raw.githubusercontent.com/jadwer/3dModels/refs/heads/main/black-circle.png");
                pricePlane.setAttribute("width", 0.8);
                pricePlane.setAttribute("height", 0.8);
                pricePlane.setAttribute("position", { x: -1.3, y: 0, z: 0.3 });
                pricePlane.setAttribute("rotation", { x: -90, y: 0, z: 0 });
                pricePlane.setAttribute("visible", false);
    
                // precio del platillo
                var price = document.createElement("a-entity");
                price.setAttribute("id", `price-${dish.id}`);
                price.setAttribute("position", { x: 0.03, y: 0.05, z: 0.1 });
                price.setAttribute("rotation", { x: 0, y: 0, z: 0 });
                price.setAttribute("text", {
                    font: "mozillavr",
                    color: "white",
                    width: 3,
                    align: "center",
                    value: `$${dish.price}`
                });
    
                pricePlane.appendChild(price);
                marker.appendChild(pricePlane);

            } // Termina el if de los días

        });
    },

    getDishes: async function () {
        return await firebase
            .firestore()
            .collection("dishes")
            .get()
            .then(snap => {
                return snap.docs.map(doc => doc.data());
            });
    }
});
