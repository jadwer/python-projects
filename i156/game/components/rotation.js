AFRAME.registerComponent("world-rotation", {
  schema: {
    speedOfRotation: {
      type: "number",
      default: 0,
    },
  },
  init: function () {
    window.addEventListener("keydown", (keyEvent) => {
      if (keyEvent.key === "ArrowRight") {
        if (this.data.speedOfRotation < 0.1) {
          this.data.speedOfRotation += 0.01;
        }
      } else if (keyEvent.key === "ArrowLeft") {
        if (this.data.speedOfRotation > -0.1) {
          this.data.speedOfRotation -= 0.01;
        }
      }
    });
  },
  tick: function () {
    var mapRotation = this.el.getAttribute("rotation");
    mapRotation.y += this.data.speedOfRotation;

    this.el.setAttribute("rotation", {
      x: mapRotation.x,
      y: mapRotation.y,
      z: mapRotation.z,
    });
  },
});

AFRAME.registerComponent("plane-rotation", {
  schema: {
    sppedOfRotation: { type: "number", defaul: 0 },
    speedOfAscent: { type: "number", defaul: 0 },
  },
  init: function () {
    this.data.speedOfRotation = this.el.getAttribute("rotation");
    this.data.speedOfAscent = this.el.getAttribute("position");

    var planeRotation = this.data.speedOfRotation;
    var planePosition = this.data.speedOfAscent;

    window.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") {
        if (planeRotation.x < 10) {
          planeRotation.x += 0.5;
          this.el.setAttribute("rotation", planeRotation);
        }
      }
      if (e.key === "ArrowLeft") {
        if (planeRotation.x > -10) {
          planeRotation.x -= 0.5;
          this.el.setAttribute("rotation", planeRotation);
        }
      }
      if (e.key === "ArrowUp") {
        if (planeRotation.z < 20) {
          planeRotation.z += 0.5;
          this.el.setAttribute("rotation", planeRotation);
        }
        if (planePosition.y < 2) {
          planePosition.y += 0.01;
          this.el.setAttribute("position", planePosition);
        }
      }
      if (e.key === "ArrowDown") {
        if (planeRotation.z > -10) {
          planeRotation.z -= 0.5;
          this.el.setAttribute("rotation", planeRotation);
        }
        if (planePosition.y > -2) {
          planePosition.y -= 0.01;
          this.el.setAttribute("position", planePosition);
        }
      }
    });
  },
  tick: function () {},
});
