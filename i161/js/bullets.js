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
                scene.appendChild(bullet);
            }
        });
    },
});

