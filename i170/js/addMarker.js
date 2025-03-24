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

            // Creamos el modelo 3D
            var model = document.createElement("a-entity");
            model.setAttribute("id", `${dish.id}`);
            model.setAttribute("position", dish.model_geometry.position);
            model.setAttribute("rotation", dish.model_geometry.rotation);
            model.setAttribute("scale", dish.model_geometry.scale);
            model.setAttribute("gltf-model", dish.model_url);
            model.setAttribute("gesture-handler", {});
            marker.appendChild(model);

            // Creamos el plano principal
            var mainPlane = document.createElement("a-plane");
            mainPlane.setAttribute("id", `main-plane-${dish.id}`);
            mainPlane.setAttribute("position", { x: 0, y: 0, z: 0 });
            mainPlane.setAttribute("rotation", { x: -90, y: 0, z: 0 });
            mainPlane.setAttribute("width", 1.7);
            mainPlane.setAttribute("height", 1.5);
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
