AFRAME.registerComponent("enemy-bullets", {
    init: function (){
        setInterval(this.shootEnemyBullet, 2000)
    },
    shootEnemyBullet: function(){
        var els = document.querySelectorAll(".enemy");
        //console.log(els)

        for (var i = 0; i < els.length; i++) {
            var enemyBullet = document.createElement("a-entity");

            enemyBullet.setAttribute("geometry", {
                primitive: "sphere",
                radius: 0.1
            });

            enemyBullet.setAttribute("material", {
                color: "#282B29"
            });

            var position = els[i].getAttribute("position");

            enemyBullet.setAttribute("position", {
                x: position.x + 1.5,
                y: position.y + 3.5,
                z: position.z,
            });

            var scene = document.querySelector("#scene");
            scene.appendChild(enemyBullet);

            var enemy = els[i].object3D;
            var player = document.querySelector("#weapon").object3D;

            var positionEnemy = new THREE.Vector3();
            var positionPlayer = new THREE.Vector3();

            player.getWorldPosition(positionPlayer);
            enemy.getWorldPosition(positionEnemy);

            var direction = new THREE.Vector3();

            direction.subVectors(positionEnemy, positionPlayer).normalize();

            enemyBullet.setAttribute("velocity", direction.multiplyScalar(-10));
            
            enemyBullet.setAttribute("dynamic-body", {
                shape: "sphere",
                mass: 0
            })

            var element = document.querySelector("#countLife");
            var playerLife = parseInt(element.getAttribute("text").value)

            enemyBullet.addEventListener("collide", (event) => {
                if(event.detail.body.el.id == "weapon") {
                    if(playerLife > 0) {
                        playerLife -= 1; // playerLife = playerLife - 1
                        element.setAttribute("text", {
                            value: playerLife
                        });
                    }
                    if(playerLife <= 0){
                        var txt = document.querySelector("#over");
                        txt.setAttribute("visible", true);

                        var tankEl = document.querySelectorAll(".enemy");
                        for (var i = 0; tankEl.length; i++) {
                            scene.removeChild(tankEl[i]);
                        }
                    }
                }
            });
        }
    },
});

