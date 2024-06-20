AFRAME.registerComponent("bullets", {
    init: function(){
        this.shootBullet();
    },


    shootBullet: function (){
        window.addEventListener("keydown", (tecla)=>{
            if(tecla.key === "z"){
                console.log("z pressed")
                var bullet = document.createElement("a-entity");
                bullet.setAttribute("geometry", {
                    primitive: "sphere",
                    radius: 0.1
                });
                bullet.setAttribute("material", {
                    color:"black"
                });

                
                // var cam = document.querySelector("#camera");
                var cam = document.getElementById("camera");
                pos = cam.getAttribute("position") // {x, y, z}
                
                bullet.setAttribute("position", {
                    x: pos.x,
                    y: pos.y,
                    z: pos.z
                });
                
                var camera = document.querySelector("#camera").object3D;
                
                var direction = new THREE.Vector3();
                camera.getWorldDirection(direction);
                
                bullet.setAttribute("velocity", direction.multiplyScalar(-10));
                
                var scene = document.querySelector("a-scene");

                bullet.setAttribute("dynamic-body", {
                    shape: "sphere",
                    mass: "0"
                });

                bullet.setAttribute("class", "#bullet")

                
                scene.appendChild(bullet);
                bullet.addEventListener("collide", this.removeBullet);
            }
        });
    },

    removeBullet: function(event){
        // Entidad original (Bala)
        console.log(event.detail.target.el);

        // Otra entidad que la bala toque
        console.log(event.detail.body.el);

        // Elemento de la bala
        var element = event.detail.target.el;

        // Elemento que es golpeado
        var elementHit = event.detail.body.el;

        if(elementHit.id.includes("box")){
            elementHit.setAttribute("material", {
                opacity: 0.6,
                transparent: true
            });

            var impulse = new CANNON.Vec3(-2,2,1);

            var worldPoint = new CANNON.Vec3().copy(elementHit.getAttribute("position"));

            elementHit.body.applyImpulse(impulse, worldPoint);

            element.removeEventListener("collide", this.shoot);

            var scene = document.querySelector("#scene");
            scene.removeChild(element);

            // remover las balas de la escena
        }

    },
});

