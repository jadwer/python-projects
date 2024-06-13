AFRAME.registerComponent("game-play",{
    schema: {
        elementId: {type:"string", default: "#ring1"}
    },

    update: function(){
        this.isCollided(this.data.elementId)
    },

    isCollided: function(elementId){

        const element = document.querySelector(elementId);
        element.addEventListener("collide", (event)=>{
            if(elementId.includes("ring")){
                console.log(elementId + ": Collision");
            }
            else if(elementId.includes("bird")){
                console.log(elementId + ": Collision")
            }
        });

    },
});


// var palabra = "estrella"
// alert(palabra.includes("ella"));

