AFRAME.registerComponent("move",{
    schema: {
        moveY: {type: "number", default: 1}
    },

    tick: function () {
        var pos = this.el.getAttribute("position");
        this.data.moveY = this.data.moveY + 0.01;

        pos.y = this.data.moveY;

        this.el.setAttribute("position", {x: pos.x, y: pos.y, z:pos.z});
    },
});

AFRAME.registerComponent ("camera-zoom-out", {
    schema: {
        moveZ: { type: "number", default: 10}
    },
    tick: function () {
        this.data.moveZ = this.data.moveZ + 0.01;
        var pos = this.el.getAttribute("position");
        pos.z = this.data.moveZ;
        this.el.setAttribute("position", {x: pos.x, y: pos.y, z: pos.z})
    },
});

AFRAME.registerComponent("fall-down", {
    schema:{
        moveY: {type: "number", defaul: 0}},
    tick:function () {
        window.addEventListener("click", (event)=>{
            this.data.moveY = this.data.moveY - 0.0001
        });

        var pos = this.el.getAttribute("position");
        pos.y = pos.y + this.data.moveY;
        this.el.setAttribute("position", { x: pos.x, y: pos.y, z: pos.z})
    },
});

AFRAME.registerComponent("fall-down-2",{
    schema:{
        moveY: {type: "number", default: 0}
    },
    init: function () {
        setTimeout(window.addEventListener("click", (event) =>{
            this.data.moveY = this.data.moveY - 0.001;
        }), 1000)
        ;
    },

    tick: function (){        

        var pos = this.el.getAttribute("position");
        pos.y = pos.y + this.data.moveY;
        this.el.setAttribute("position", {x: pos.x, y: pos.y, z:pos.z})
    },
});